import sqlite3
import os

def init_db():
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
        
    conn = sqlite3.connect('finiquitos.db')
    with open('schema.sql') as f:
        conn.executescript(f.read())
        
    cur = conn.cursor()
    # Dummy worker to avoid empty table
    cur.execute('''INSERT INTO trabajadores 
                (nombre, rut, afp, salud, cargo, horas_semanales, sueldo_bruto, sueldo_liquido) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                ('Juan Empleado', '11.111.111-1', 'Modelo', 'Fonasa', 'Ingeniero', 40, 1000000, 830000))
    conn.commit()
    conn.close()
    print("DB Finiquitos Inicializada.")

if __name__ == '__main__':
    init_db()
