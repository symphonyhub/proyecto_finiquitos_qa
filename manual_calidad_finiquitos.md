# Manual de Calidad SGC - "Sistema Generador de Finiquitos"

El presente es un documento rector normativo. La Política de Calidad subyace en que cada emisión documental (PDF) expedida por nuestra plataforma está vinculada y verificada matemáticamente sin posibilidad a intervención humana posterior (Poka-Yoke).

## 1. Alcance del SGC
Este manual abarca la "Lógica Matemática Descontadora de Previsión Chilena" así como la "Garantía de Retención Permanente de Datos Laborales" gestionada en nuestro back-end para el cliente Corporativo.

## 2. Objetivos de Calidad Transaccional
1. **Precisión Matemática Legal (0.00% Defectos Aritméticos):** Toda deducción y emisión de sueldo líquido debe ser trazada de forma correcta según % actualizando así la Matriz Trazabilidad.
2. **Estabilidad y Blindaje Base de Datos:** Los anexos (Fotografías y Docs en formato multipart/form-data) subidos por RRHH deben encriptarse dentro del servidor (`/uploads`), proscribiendo rutas públicas peligrosas y vulnerabilidades XSS.
3. **Disponibilidad Front-End (UI 99% Uptime):** Las interfaces deben cargar a 60FPS, sin deformarse de manera *Responsive* minimizando el umbral de estrés emocional del Operador de RRHH.

## 3. Revisión Directiva
Cada actualización de las tasas Previsionales deberá someterse estrictamente a QA mediante los protocolos "Caja Blanca" delineados en la Matriz `RF-FIN-03` para re-aprobar este Sistema de Gestión de Calidad.
