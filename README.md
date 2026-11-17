# Tabla canadiense — movimiento primero

**Una aplicación visual para entender cómo se mueve el índice y dónde se colocan los palos de una tabla de rehabilitación.** La simulación es orientativa: **no es una pauta de ejercicios**. Los ejercicios y el montaje real deben estar autorizados y revisados por el terapeuta de mano.

[Français](README.fr.md) · [Cambios de la v10](CAMBIOS_v10.md) · [Revisión de usabilidad](REVISION_UX_v10.md)

## Abrir

Abre `index.html` directamente en un navegador moderno. No necesitas instalar nada, conectar a Internet ni compilar. Toda la aplicación es **un solo archivo HTML**, con CSS, JavaScript y SVG integrados; no tiene librerías externas.

### La nueva experiencia

Al entrar, **la mano se mueve en el propio tablero**. La primera acción es **«Ver demostración»**. Esto abre el ejemplo de **«Diana con bola»** directamente, en movimiento, sin pasar por la pantalla de preparación estática. Puedes:

- **Pausar / reproducir** el movimiento con un botón visible sobre el tablero.
- **Mover el dedo manualmente** usando la barra «Explora el recorrido» (también con teclado).
- Cambiar entre **planta** y **montaje 3D**, y consultar los agujeros de los palos y los pasos de la serie.
- Elegir **«Tengo una pauta»** y pegar el código `TABLA1` recibido del terapeuta.
- Abrir **«Soy terapeuta»** para ajustar medidas, ejercicios, plantillas y exportaciones.

**Los movimientos de demostración no deben imitarse como tratamiento.** Al cargar una pauta real, la animación **no comienza automáticamente**. Si el sistema indica «reducir movimiento», la reproducción automática queda desactivada.

## Idiomas

La interfaz, la demostración y las etiquetas dinámicas se ofrecen en **español y francés** (ES / FR), incluido el PDF exportado. Los textos libres escritos por un profesional nunca se traducen automáticamente para evitar cambios de sentido clínico.

## Tablero y archivos

- Tablero **400 × 300 mm**, 165 agujeros, 15 columnas A–O y 11 filas 1–11, centros a 25 mm.
- Exportación de **SVG a tamaño 1:1** y **DXF en milímetros** con agujeros de Ø12,2 mm (por defecto) u Ø12,0 mm.
- PDF A4 de una página cuando la pauta cabe legiblemente.
- Pautas con código `TABLA1`, incluida compatibilidad con códigos previos. La suma de comprobación detecta cambios accidentales, **no autentica al terapeuta**.
- Plantillas del profesional en `localStorage`. No hay diario de dolor ni gráfico de progreso. Si existen registros de versiones anteriores, se ofrecen opciones de exportación y borrado manual.

## Seguridad clínica y privacidad

Este visualizador **no sustituye al cirujano ni al terapeuta de mano**, ni valida la fase postoperatoria, la estabilidad de una reparación o los puntos reales de contacto. La silueta y el movimiento están calculados para el índice; las alturas de la vista 3D son orientativas. Los controles de la app no pueden descartar todas las compresiones o interferencias físicas. La colocación de palos y espuma debe comprobarse en la tabla real.

El calor y el masaje requieren herida cerrada/seca y autorización del terapeuta. No realizar ejercicios ni progresar de nivel por el mero hecho de ver la animación. Si aparece chasquido, nueva pérdida de extensión, dolor o hinchazón inesperados, suspender y consultar al equipo tratante.

Los datos de `localStorage` permanecen en el navegador y no se sincronizan. **No publiques pautas reales de pacientes** en repositorios ni en GitHub Pages.

## GitHub Pages

1. Sube los archivos del repositorio a la rama `main`.
2. En **Settings → Pages**, selecciona **Deploy from a branch**, `main` y `/(root)`.
3. Una vez publicada, podrás abrir la página desde la URL de GitHub Pages del repositorio.

## Pruebas

Las dependencias de desarrollo no forman parte de la aplicación web.

```bash
python -m pip install -r requirements-test.txt
python -m playwright install chromium
python tests/smoke.py
```

Se prueban los movimientos, pausa, barra manual, prioridad de la demostración, lectura móvil, modo de movimiento reducido, idioma francés, compatibilidad de pautas y los exportadores SVG/DXF/PDF. Para usar Chromium instalado por el sistema, define `CHROMIUM_PATH`.

## Licencia

MIT; consulta [`LICENSE`](LICENSE). Sin garantía de eficacia clínica.
