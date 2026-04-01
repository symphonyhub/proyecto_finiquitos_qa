# Informe Técnico: Método Cascada (SDLC Finiquitos)

La programación secuencial Cascada ha sido elegida para modelar matemáticamente los expedientes de finiquito debido al carácter legal e inmutable (normativo) de los cálculos chilenos.

## 1. Fase de Análisis de Requerimientos
Identificado el problema de la emisión manual de finiquitos. El usuario solicitó el registro de perfiles con horas, sueldo líquido, previsión, y la emisión de contratos en Formato Documento Portable `*.pdf`. Se evaluó, permitiendo identificar la necesidad de integrar la biblioteca `FPDF`.

## 2. Fase de Diseño y Arquitectura
- **UI/UX Alta Gama:** Formulario basado en CSS semántico corporativo, con sombras neutras y modales (Dialog) puros HTML5.
- **Backend Model:** Servidor con capacidad C-Load en OS local (`Flask`) conectado a un SQLite embebido con tablas `empleados` conteniendo URLs apuntando a nuestro FileSystem (`/uploads`).

## 3. Fase de Codificación Integral
Programación rígida por hitos. Se inició programando el algoritmo matemático del Líquido Neto desde Python, aislando ese modelo antes de pasar a programar Jinja2 e inyectar un esqueleto visual PDF (Fase lineal, no interactiva AGILE).

## 4. Pruebas de Software (Testing QA)
Cumplidos los requerimientos Front-end, se cruzaron los puntos con la Matriz de Trazabilidad `RF-FIN-01`, validando bloqueos estáticos a archivos `.txt` maliciosos camuflados de imagen, evitando que se inyectaran a nuestro FileSystem.

## 5. Documentación
Incrustada en este y otros anexos paralelos, constituyendo evidencia física empírica de un Sistema de Gestión de la Calidad para fines pre-formativos evaluativos.

## 6. Mantenimiento y Cierre
Despliegue local y migración de Datos Vivos. Actualización futura del `app.py` quedará ligada a eventuales cambios tributarios que emanen del Ministerio Público en materia de Salud y AFP.
