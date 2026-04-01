# 💼 Sistema Generador de Finiquitos (Auditoría QA)

![Estatus](https://img.shields.io/badge/Proyecto-Completado-success) ![Framework](https://img.shields.io/badge/Tecnología-Flask-green) ![PDF](https://img.shields.io/badge/Reportes-FPDF-red) 

Bienvenido al repositorio oficial del **Software de Finiquitos**, un proyecto Full-Stack diseñado para calcular, deducir imposiciones legales y emitir documentos PDF descargables, construido bajo el paradigma estricto de Aseguramiento de Calidad (Norma ISO 9001).

---

## 🛠️ Requisitos Técnicos
Para evaluar este programa, el equipo docente/evaluador debe poseer:
- **Python 3.x** instalado en su sistema operativo.
- Una consola de comandos (Terminal, CMD o PowerShell).

---

## 🚀 Guía de Instalación y Puesta en Marcha (Para el Profesor)

Siga este paso a paso para levantar el sistema en su propia máquina en menos de 2 minutos y probar los diagramas de *Caja Blanca* y *Caja Negra*.

### 1. Clonar el repositorio y Entrar a la Carpeta
Si descargó este proyecto como `.zip`, extráigalo. Luego, abra su consola y colóquese directamente dentro de la carpeta raíz del proyecto:
```bash
cd ruta/de/tu/pc/proyecto_finiquitos_qa
```

### 2. Instalar Librerías Claves (Dependencias)
El sistema requiere el motor web `Flask` y el motor de PDF `FPDF`. Ejecute el comando mágico para instalarlos usando nuestro archivo de configuración:
```bash
pip install -r requirements.txt
```

### 3. Crear la Base de Datos "Dummy" (Sembrado Inicial)
Para que no empiece con un sistema vacío, he dejado preparado un comando que autoconfigura SQLite3 y crea sus respectivas carpetas virtuales de imágenes (Uploads). Ejecute:
```bash
python init_db.py
```
*(Debería ver el mensaje verde: "DB Finiquitos Inicializada").*

### 4. Encender el Servidor QA
Levante la aplicación ejecutando el archivo rector del back-end:
```bash
python app.py
```

### 5. Acceso y Evaluación
Con el servidor anterior encendido y la consola abierta, ingrese desde el navegador (Chrome, Firefox, Safari) a la siguiente URL:

👉 **URL de Acceso:** [http://localhost:5002](http://localhost:5002)

*(Nota: Hemos usado el puerto 5002 para garantizar que el aplicativo de finiquitos no sufra de colisiones "Port In Use" con otros proyectos que el profesor se encuentre revisando)*.

---

### ⭐ Criterios a Evaluar (Puntos Extra Logrados)
- **Subida Multipart:** Intentar enviar una imagen de retrato (".jpg") simulando adjuntarla legalmente en el formulario. 
- **Salida Dinámica FPDF:** Al culminar su registro, haga clic en la ventana *Auditar Base de Datos* y pruebe darle clic al botón "Descargar Legal". El sistema le retornará un PDF perfectamente identado a su computadora sin tenerlo guardado en disco.
