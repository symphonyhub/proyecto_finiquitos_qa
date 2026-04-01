DROP TABLE IF EXISTS trabajadores;

CREATE TABLE trabajadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    rut TEXT UNIQUE NOT NULL,
    afp TEXT NOT NULL,
    salud TEXT NOT NULL,
    cargo TEXT NOT NULL,
    horas_semanales INTEGER NOT NULL,
    sueldo_bruto REAL NOT NULL,
    sueldo_liquido REAL NOT NULL,
    foto_path TEXT,
    doc_path TEXT,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);
