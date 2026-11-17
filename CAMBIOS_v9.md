# Cambios v9 — auditoría de usabilidad y ES/FR

**Cambio de orientación:** de una hoja técnica completa a una guía visual que explica primero el propósito y la siguiente acción.

- Inicio nuevo con mensaje «¿Dónde va cada palo?», esquema y tres entradas: recibir una pauta, demostración o terapeuta.
- Nada de ejercicios demostrativos sin avisar: el ejemplo no se presenta como una prescripción.
- Solo un ejercicio a la vez, con su acción principal y agujeros; botones anterior/siguiente; selector de pasos secundario.
- Configuración del terapeuta, posición, espuma, instrucciones detalladas y tabla de todos los agujeros plegadas por defecto en la vista del paciente.
- Prioridad de acción antes del dibujo en móvil; dibujo con menos contraste de agujeros no utilizados.
- Eliminación de la opción de inglés: selector ES/FR. PDF y textos predeterminados en ambos idiomas. Los textos libres del terapeuta no se traducen automáticamente.
- HTML sin Google Fonts ni peticiones de librerías externas; apto para abrir localmente sin conexión.
- Mantiene importación `TABLA1`, comprobaciones de dosis, colisiones, revisión clínica, medidas, editor de ejercicios, plantillas, vista 3D y exportaciones PDF/SVG/DXF.
- El diario de sesiones sigue ausente y los registros anteriores no se borran automáticamente.

**Sin modificar:** cinemática, valores y reglas de progresión de los ejercicios originales. La seguridad del montaje físico sigue requiriendo validación clínica y técnica presencial.

**QA:** 42 comprobaciones automatizadas de regresión, más inspección visual de capturas de escritorio y móvil en ES/FR. Esto no sustituye pruebas de usabilidad con personas reales.
