# Revisión heurística de usabilidad — v10

17 de noviembre de 2026. Revisión del flujo v9 y aplicación de ajustes sobre el HTML. **No es una prueba de usabilidad con usuarios reales.**

## Hallazgos principales

| Antes (v9) | Problema para una primera visita | Solución v10 |
|---|---|---|
| «Ver un ejemplo» abría «Preparación» | La primera pantalla de la demo no mostraba movimiento | La demostración abre «Diana con bola» y la anima |
| Portada con ilustración inmóvil | No se percibía de inmediato la función de mover el dedo | Portada con animación real del índice, trayectoria y bola |
| «Ver el movimiento» estaba dentro de instrucciones | La acción principal competía con otros botones y quedaba lejos del dibujo | Pausa/Reproducir + recorrido manual en una barra **antes** del tablero |
| En móvil aparecían antes las instrucciones que el plano | El usuario no veía el movimiento sin desplazarse | El tablero y sus controles aparecen antes del panel de instrucciones |
| Dependencia del ratón o del botón Reproducir para explorar | Imposibilidad de inspeccionar un instante exacto del movimiento | Barra de recorrido accesible también por teclado |
| Animación continua sin controles claros en portada | Distracción y dificultad para usuarios sensibles al movimiento | Botón de pausa y respeto de `prefers-reduced-motion` |

## Recorrido esperado (menos de un minuto)

1. El visitante entra y ve un índice moverse hacia una bola roja.
2. Lee que es una **simulación, no una pauta**.
3. Pulsa «Ver demostración», ve de inmediato la flexión del dedo y puede pausarla.
4. Arrastra la barra para inspeccionar el recorrido, ve la posición de los palos y los agujeros.
5. Si tiene una pauta real, vuelve al inicio y selecciona «Tengo una pauta».

## Verificación interna

54 comprobaciones automatizadas superadas en Chromium, incluidas animación automática, pausa, barra, movimiento reducido, ES/FR, vista 3D, paso activo, editor, importación, límites, SVG, DXF, PDF y visualización móvil sin desbordamientos. Se han inspeccionado capturas en 1350 px y 390 px.

## Riesgos abiertos

- El recorrido no se ha observado con terapeutas de mano ni con usuarios nuevos; no debe afirmarse «intuitivo» o «wow» como resultado probado.
- La ilustración y la animación no permiten inferir el montaje anatómico correcto ni validar los contactos reales de los palos.
- La simulación anatómica sigue siendo solo del índice, y la aplicación no es un protocolo clínico autónomo.
- Próxima validación sugerida: 5 usuarios sin contexto, sin explicaciones previas. Preguntar «¿para qué sirve?», «¿cómo veo el movimiento?» y «¿cómo abro mi pauta?» y observar errores, retrocesos y tiempo hasta la primera acción.
