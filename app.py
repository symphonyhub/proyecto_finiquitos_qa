import os
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, send_file
from werkzeug.utils import secure_filename
from fpdf import FPDF

app = Flask(__name__)
app.config['SECRET_KEY'] = 'finiquito_secret_qa'
app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS_IMG = {'png', 'jpg', 'jpeg'}
ALLOWED_EXTENSIONS_DOC = {'pdf', 'txt', 'docx'}

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def get_db():
    conn = sqlite3.connect('finiquitos.db')
    conn.row_factory = sqlite3.Row
    return conn

def allowed_file(filename, allowed_set):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_set

# Algoritmo (Caja Blanca) RF-FIN-03
def calcular_liquido(bruto):
    descuento_afp = bruto * 0.10
    descuento_salud = bruto * 0.07
    return bruto - (descuento_afp + descuento_salud)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form['nombre']
    rut = request.form['rut']
    afp = request.form['afp']
    salud = request.form['salud']
    cargo = request.form['cargo']
    horas = int(request.form['horas'])
    bruto = float(request.form['bruto'])
    
    # Validaciones Legales (Caja Negra)
    if horas > 45:
        flash('Error QA: Las horas semanales superan el máximo legal (45 hrs).', 'error')
        return redirect(url_for('index'))

    # Puntos Extras: Adjuntar Foto y Docs
    foto = request.files.get('foto')
    doc = request.files.get('documento')
    
    foto_path = ""
    doc_path = ""
    
    if foto and allowed_file(foto.filename, ALLOWED_EXTENSIONS_IMG):
        f_name = secure_filename(f"foto_{rut}_{foto.filename}")
        foto.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
        foto_path = f_name
        
    if doc and allowed_file(doc.filename, ALLOWED_EXTENSIONS_DOC):
        d_name = secure_filename(f"doc_{rut}_{doc.filename}")
        doc.save(os.path.join(app.config['UPLOAD_FOLDER'], d_name))
        doc_path = d_name

    liquido = calcular_liquido(bruto)
    
    # Inserción segura a BD
    db = get_db()
    try:
        db.execute('''INSERT INTO trabajadores 
            (nombre, rut, afp, salud, cargo, horas_semanales, sueldo_bruto, sueldo_liquido, foto_path, doc_path) 
            VALUES (?,?,?,?,?,?,?,?,?,?)''',
            (nombre, rut, afp, salud, cargo, horas, bruto, liquido, foto_path, doc_path))
        db.commit()
        flash('Trabajador y datos procesados exitosamente en la Matriz.', 'success')
    except sqlite3.IntegrityError:
        flash('Error: El trabajador con ese RUT ya se encuentra registrado.', 'error')
    finally:
        db.close()
        
    return redirect(url_for('listar'))

@app.route('/listar')
def listar():
    db = get_db()
    lista = db.execute('SELECT * FROM trabajadores ORDER BY id DESC').fetchall()
    db.close()
    return render_template('listar.html', trabajadores=lista)

@app.route('/generar_pdf/<int:t_id>')
def generar_pdf(t_id):
    db = get_db()
    t = db.execute('SELECT * FROM trabajadores WHERE id = ?', (t_id,)).fetchone()
    db.close()
    
    if not t:
        flash('Trabajador no encontrado.', 'error')
        return redirect(url_for('listar'))
        
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    
    # Membrete
    pdf.cell(200, 10, txt="SISTEMA GENERADOR DE FINIQUITOS (QA)", ln=1, align='C')
    pdf.set_font("Arial", '', 10)
    pdf.cell(200, 10, txt="Documento con validez de Control Interno RRHH", ln=1, align='C')
    pdf.ln(10)
    
    # Cuerpo del Finiquito
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt=f"COMPROBANTE RESUMEN DEL TRABAJADOR: {t['nombre']}", ln=1, align='L')
    pdf.set_font("Arial", '', 12)
    pdf.cell(200, 10, txt=f"R.U.T. : {t['rut']}", ln=1, align='L')
    pdf.cell(200, 10, txt=f"Cargo Desempenado: {t['cargo']} ({t['horas_semanales']} Hrs Semanales)", ln=1, align='L')
    
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="DESGLOSE INSTITUCIONAL:", ln=1, align='L')
    pdf.set_font("Arial", '', 12)
    pdf.cell(200, 10, txt=f"Institucion Previsional (AFP): {t['afp']} (-10%)", ln=1, align='L')
    pdf.cell(200, 10, txt=f"Sistema de Salud: {t['salud']} (-7%)", ln=1, align='L')
    
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="LIQUIDACION MATEMATICA:", ln=1, align='L')
    pdf.set_font("Arial", '', 12)
    pdf.cell(200, 10, txt=f"Sueldo Base Imponible: ${t['sueldo_bruto']:,.0f}", ln=1, align='L')
    pdf.set_font("Arial", 'B', 14)
    pdf.set_text_color(0, 100, 0) # Verde
    pdf.cell(200, 10, txt=f"TOTAL LIQUIDO A PAGAR: ${t['sueldo_liquido']:,.0f}", ln=1, align='L')
    
    # Pie de pagina Firma
    pdf.set_text_color(0, 0, 0)
    pdf.ln(30)
    pdf.cell(95, 10, txt="____________________________", align='C')
    pdf.cell(95, 10, txt="____________________________", ln=1, align='C')
    pdf.cell(95, 10, txt="Firma Empleador/Representante", align='C')
    pdf.cell(95, 10, txt=f"Firma Trabajador: {t['nombre']}", ln=1, align='C')
    
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], f"Finiquito_{t['rut']}.pdf")
    pdf.output(pdf_path)
    
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
