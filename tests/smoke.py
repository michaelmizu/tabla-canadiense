from playwright.sync_api import sync_playwright
from pathlib import Path
import base64, json, tempfile, shutil, os, re
import xml.etree.ElementTree as ET
import fitz

REPO=Path(__file__).resolve().parents[1]
HTML_PATH=REPO/'index.html'
s=HTML_PATH.read_text()
marker='  templates=readTemplates();refreshTemplates();\n  render();renderExerciseList();'
assert marker in s
probe='''  window.__qa={code:()=>code(),state:()=>({L:{...L},w:W(),ballN,manualBall,errors:planProblems(),sequence:serializeSequence()}),fixed:()=>fixedPegsAt(+ui.wrist.value,W(),new Set()).map(p=>({n:p.n,H:p.H?hname(p.H):null,A:p.A}))};\n'''
s=s.replace(marker,probe+marker)
results=[]
def ck(cond,label,info=''):
 good=bool(cond);results.append((good,label,info));print(('OK' if good else 'FAIL')+' | '+label+(' | '+str(info)[:180] if info else ''),flush=True)
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path=os.environ.get('CHROMIUM_PATH') or shutil.which('chromium'),args=['--no-sandbox','--disable-dev-shm-usage'])
 ctx=b.new_context(accept_downloads=True,viewport={'width':1280,'height':900})
 pg=ctx.new_page();pg.set_default_timeout(12000)
 pg.on('dialog',lambda d:d.accept())
 errors=[];pg.on('pageerror',lambda e:errors.append(str(e)))
 pg.evaluate('''Object.defineProperty(window,'localStorage',{configurable:true,value:{db:{},getItem(k){return this.db[k]??null},setItem(k,v){this.db[k]=String(v)},removeItem(k){delete this.db[k]}}});''')
 pg.set_content(s,wait_until='domcontentloaded',timeout=40000)
 ck(not errors,'JS sin errores',errors)
 ck(pg.locator('#welcome').is_visible() and not pg.locator('#workbench').is_visible(),'Inicio claro, vista clínica oculta')
 ck(pg.locator('#hero-motion').is_visible() and pg.locator('#hero-finger line').count()==6,'Vista previa dibujada con la cinemática del índice')
 before=pg.locator('#hero-fingertip').get_attribute('cx')
 pg.wait_for_timeout(500)
 after=pg.locator('#hero-fingertip').get_attribute('cx')
 ck(before!=after,'La vista previa realmente se anima sin hacer clic')
 pg.locator('#hero-toggle').click()
 paused_at=pg.locator('#hero-fingertip').get_attribute('cx')
 pg.wait_for_timeout(220)
 ck(paused_at==pg.locator('#hero-fingertip').get_attribute('cx'),'Pausar vista previa detiene el movimiento')
 pg.locator('#hero-toggle').click()
 ck(pg.locator('#hero-toggle').get_attribute('aria-pressed')=='true','Vista previa se puede reanudar')

 ck(pg.locator('#start-load').is_visible() and pg.locator('#start-demo').is_visible() and pg.locator('#start-therapist').is_visible(),'Tres caminos de entrada')
 ck(pg.locator('#progress-chart').count()==0,'Sin gráficos de progreso')
 ck(pg.locator('#lang-fr').count()==1 and pg.locator('#lang-en').count()==0,'Francés reemplaza inglés')
 # Demo: visible first action and board; large settings folded
 pg.locator('#start-demo').click()
 ck(pg.locator('#workbench').is_visible() and not pg.locator('#welcome').is_visible(),'Demostración abre entorno')
 ck(pg.locator('#motion-transport').is_visible() and pg.locator('#play').get_attribute('aria-pressed')=='true','Demostración inicia el movimiento automáticamente')
 ck(pg.evaluate("document.querySelector('#motion-transport').getBoundingClientRect().top < document.querySelector('#plan').getBoundingClientRect().top"),'Controles de movimiento por encima del dibujo')
 pg.locator('#play').click()
 ck(pg.locator('#play').get_attribute('aria-pressed')=='false','Pausa de movimiento')
 pg.locator('#motion-scrub').fill('0');pg.locator('#motion-scrub').dispatch_event('input')
 point0=pg.evaluate("({x:document.querySelector('#plan [data-drag-hand]')?.getBBox()?.x, t:document.querySelector('#motion-scrub').value})")
 pg.locator('#motion-scrub').fill('100');pg.locator('#motion-scrub').dispatch_event('input')
 point1=pg.evaluate("({x:document.querySelector('#plan [data-drag-hand]')?.getBBox()?.x, t:document.querySelector('#motion-scrub').value})")
 ck(point0['t']=='0' and point1['t']=='100' and pg.locator('#play').get_attribute('aria-pressed')=='false','Barra permite explorar el recorrido sin reproducir')

 ck(pg.locator('#workspace-eyebrow').inner_text()=='DEMOSTRACIÓN' and pg.locator('#ex-main-action').inner_text().startswith('Quita'),'Modo ejemplo claramente indicado')
 ck(not pg.locator('#advanced-tools').evaluate('(e)=>e.open') and not pg.locator('#exercise-settings').evaluate('(e)=>e.open'),'Opciones clínicas plegadas')
 ck(pg.locator('#step-tabs button').count()==4 and pg.locator('#step-count').inner_text()=='Ejercicio 3 de 4','Serie original conservada; demo abre ejercicio con movimiento')
 pg.locator('#next-step').click()
 ck('Estirar' in pg.locator('#ex-title').inner_text() and 'Ejercicio 4' in pg.locator('#step-count').inner_text(),'Avanza y muestra una sola acción')
 pg.locator('#prev-step').click()
 ck('Diana con bola' in pg.locator('#ex-title').inner_text(),'Regresa con botón anterior')
 pg.locator('#lang-fr').click()
 ck(pg.locator('#welcome').is_hidden() and 'À FAIRE' in pg.locator('.current-action').inner_text(),'Cambio ES a FR sin perder ejercicio')
 pg.locator('#next-step').click()
 ck('Extension' in pg.locator('#ex-title').inner_text() and 'tige 7' in pg.locator('#ex-main-action').inner_text() and pg.locator('#step-count').inner_text()=='Exercice 4 sur 4','Instrucciones originales traducidas')
 pg.locator('#exercise-instructions summary').click()
 ck('tige 7' in pg.locator('#ex-how').inner_text(),'Detalles de ejercicio en francés')
 pg.locator('#view-montage').click()
 ck(pg.locator('#mount-3d').is_visible(),'Perspectiva 3D')
 pg.locator('#view-plan').click()
 ck(pg.locator('#plan').is_visible(),'Regresa a planta')
 pg.locator('#return-home').click()
 ck(pg.locator('#welcome').is_visible() and 'Regardez le doigt bouger.' in pg.locator('#welcome-title').inner_text(),'Inicio francés traducido')
 ck('Voir la démonstration' in pg.locator('#start-demo').inner_text(),'Acción principal en francés')
 ck('guider le mouvement' in pg.locator('.welcome-lede').inner_text(),'Descripción francesa completa, sin mezcla española')
 # invalid import should not make patient mode available
 pg.locator('#start-load').click()
 ck(pg.locator('#quick-load').is_visible() and pg.locator('#in').is_visible(),'Pauta se abre desde inicio')
 pg.locator('#in').fill('CODIGO INVENTADO');pg.locator('#load').click()
 ck(pg.locator('#welcome').is_visible(),'Importación inválida no abre la pauta')
 # therapist mode for safe artifact exports
 pg.locator('#start-therapist').click()
 ck(pg.locator('#advanced-tools').evaluate('(e)=>e.open'),'Modo terapeuta abre opciones')
 ck(pg.locator('#copy').is_disabled(),'Sin revisión no permite compartir')
 first=pg.evaluate('__qa.fixed()')
 pg.locator('#dim-meta').fill('35');pg.locator('#dim-meta').dispatch_event('input'); new=pg.evaluate('__qa.fixed()')
 ck(first[3]['A']['x']>new[3]['A']['x'],'Apoyos ajustados al metacarpiano')
 pg.locator('#reset-measures').click()
 pg.locator('#reps').fill('999');pg.locator('#reps').dispatch_event('input')
 ck(pg.locator('#copy').is_disabled(),'Dosis inválidas bloquean compartir')
 pg.locator('#reps').fill('10');pg.locator('#reps').dispatch_event('input')
 pg.locator('#safety-phase').fill('Phase validée par le thérapeute')
 pg.locator('#safety-approval').check();pg.locator('#safety-splint').check();pg.locator('#safety-wound').check()
 ck(pg.locator('#copy').is_enabled() and not pg.evaluate('__qa.state().errors'),'Pauta revisada permite copiar',pg.evaluate('__qa.state().errors'))
 code=pg.evaluate('__qa.code()')
 decoded=json.loads(base64.b64decode(code.split(':',1)[1]).decode())
 ck(decoded['v']==4 and 'ck' in decoded,'Formato TABLA1 de v8 conservado')
 # French text and pdf export. HTML download captures real output.
 out=pg.locator('#out').input_value()
 ck('Fiche de la table canadienne' in out and 'main gauche' in out and 'séances par jour' in out and 'sesiones al día' not in out,'Pauta exportada en francés',out[:180])
 with tempfile.TemporaryDirectory() as tmp:
  saved={}
  for bid,fn in [('download-svg','out.svg'),('download-dxf','out.dxf'),('download-pdf','out.pdf')]:
   with pg.expect_download(timeout=20000) as info: pg.locator('#'+bid).click()
   path=Path(tmp)/fn;info.value.save_as(str(path));saved[fn]=path.read_bytes()
   ck(len(saved[fn])>200,bid+' descarga',len(saved[fn]))
  root=ET.fromstring(saved['out.svg']);ns={'s':'http://www.w3.org/2000/svg'}
  ck(root.attrib.get('width')=='400mm' and len(root.findall('.//s:circle',ns))==165,'SVG 400mm y 165 taladros')
  try:
   import ezdxf
   cad=ezdxf.readfile(str(Path(tmp)/'out.dxf'))
   ck(cad.header.get('$INSUNITS')==4 and len(cad.modelspace().query('CIRCLE'))==165,'DXF CAD con 165 círculos en milímetros')
  except Exception as e:ck(False,'DXF importable',str(e))
  pdf=fitz.open(stream=saved['out.pdf'],filetype='pdf');text=pdf[0].get_text()
  ck(pdf.page_count==1 and 'EXERCICES' in text and 'FICHE' in text and 'main: gauche' in text.lower() and 'séances par jour' in text and 'Muñeca' not in text,'PDF A4 en francés, una página',text[:250])
 # Fr<->Es toggling shouldn't affect code or user-entered text
 pg.locator('#lang-es').click()
 ck('Sigue tu pauta' not in pg.locator('#workspace-title').inner_text() and 'Preparar la pauta' in pg.locator('#workspace-title').inner_text(),'Volver a español')
 # exercise editor (the bug from v4), core name preserves user strings
 pg.locator('#exercise-list .exercise-row').nth(0).get_by_role('button',name='Editar').click()
 pg.locator('#custom-title').fill('Ejercicio de prueba');pg.locator('#custom-instructions').fill('No forzar el dedo.');pg.locator('#save-exercise-edit').click()
 ck('Ejercicio de prueba' in pg.locator('#exercise-list').inner_text(),'Editor original funciona')
 pg.locator('#lang-fr').click()
 ck('Ejercicio de prueba' in pg.locator('#exercise-list').inner_text(),'Título personalizado NO traducido')
 # Return to home, reload from valid code, confirm explicit patient warning
 pg.locator('#return-home').click()
 pg.locator('#start-load').click()
 pg.locator('#in').fill(code)
 pg.locator('#load').click()
 ck(pg.locator('#workbench').is_visible() and 'FICHE REÇUE' in pg.locator('#workspace-eyebrow').inner_text(),'Importar abre lectura de paciente')
 ck(pg.locator('#patient-notice').is_visible() and 'code ne garantit pas' in pg.locator('#patient-notice').inner_text(),'Advertencia sobre código sin autenticación')
 ck(not pg.locator('#advanced-tools').evaluate('(e)=>e.open'),'Paciente no ve ajustes inicialmente')
 ck(pg.locator('#play').get_attribute('aria-pressed')=='false','La pauta del paciente no inicia ejercicios automáticamente')
 ck(not errors,'Sin errores de JS tras flujos completos',errors)
 # Mobile overflow and ordering tested in separate page
 mobile=ctx.new_page(); mobile.set_viewport_size({'width':390,'height':844})
 mobile.set_content(s,wait_until='domcontentloaded',timeout=40000)
 mobile.locator('#start-demo').click()
 rect=mobile.evaluate('''() => ({panel:document.querySelector('.panel').getBoundingClientRect().top,board:document.querySelector('.sheet').getBoundingClientRect().top,scrollWidth:document.documentElement.scrollWidth,width:window.innerWidth})''')
 ck(rect['board']<rect['panel'],'En móvil el tablero animado aparece antes que las instrucciones',rect)
 ck(rect['scrollWidth']<=rect['width']+1,'Sin desbordamiento horizontal en móvil',rect)
 mobile.close()
 reduced=ctx.new_page(reduced_motion='reduce') if False else ctx.new_page()
 reduced.emulate_media(reduced_motion='reduce')
 reduced.set_content(s,wait_until='domcontentloaded',timeout=40000)
 ck(reduced.locator('#hero-toggle').get_attribute('aria-pressed')=='false','Animación automática desactivada con movimiento reducido')
 reduced.locator('#start-demo').click()
 ck(reduced.locator('#play').get_attribute('aria-pressed')=='false','Demostración respeta reducción de movimiento')
 reduced.close();ctx.close();b.close()

passnum=sum(x[0] for x in results)
print('TOTAL',passnum,'/',len(results))

if passnum<len(results):raise AssertionError('At least one smoke test failed')
