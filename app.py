"""
API REST - Sistema de Proveedores
CRUD completo con SQLite
"""
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)
DB_PATH = "proveedores.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS proveedores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            contacto TEXT NOT NULL,
            telefono TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            direccion TEXT,
            categoria TEXT NOT NULL,
            estado TEXT DEFAULT 'activo',
            fecha_registro TEXT DEFAULT (datetime('now'))
        )
    """)
    c.execute("SELECT COUNT(*) FROM proveedores")
    if c.fetchone()[0] == 0:
        sample_data = [
            ("TechSupply S.A.","Carlos Méndez","507-6000-1234","carlos@techsupply.pa","Calle 50, Panamá","Tecnología","activo"),
            ("Distribuidora Global","Ana Torres","507-6000-5678","ana@distglobal.pa","Vía España, Panamá","Insumos","activo"),
            ("Papelería Nacional","Luis Rodríguez","507-6000-9012","luis@papnacional.pa","El Cangrejo, Panamá","Papelería","activo"),
            ("LogiPanamá","María González","507-6000-3456","maria@logipm.pa","Tocumen, Panamá","Logística","inactivo"),
            ("MediSupplies","Pedro Herrera","507-6000-7890","pedro@medisupplies.pa","Marbella, Panamá","Médico","activo"),
        ]
        c.executemany("INSERT INTO proveedores (nombre,contacto,telefono,email,direccion,categoria,estado) VALUES (?,?,?,?,?,?,?)", sample_data)
    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=["GET"])
def index():
    return send_from_directory(".", "index.html")

@app.route("/api/proveedores", methods=["GET"])
def get_all():
    conn = get_db()
    rows = conn.execute("SELECT * FROM proveedores ORDER BY id").fetchall()
    conn.close()
    return jsonify({"success":True,"total":len(rows),"data":[dict(r) for r in rows]})

@app.route("/api/proveedores/<int:id>", methods=["GET"])
def get_one(id):
    conn = get_db()
    row = conn.execute("SELECT * FROM proveedores WHERE id=?", (id,)).fetchone()
    conn.close()
    if not row:
        return jsonify({"success":False,"error":"No encontrado"}), 404
    return jsonify({"success":True,"data":dict(row)})

@app.route("/api/proveedores", methods=["POST"])
def create():
    data = request.get_json()
    try:
        conn = get_db()
        cur = conn.execute("INSERT INTO proveedores (nombre,contacto,telefono,email,direccion,categoria,estado) VALUES (?,?,?,?,?,?,?)",
            (data["nombre"],data["contacto"],data["telefono"],data["email"],data.get("direccion",""),data["categoria"],data.get("estado","activo")))
        new_id = cur.lastrowid
        conn.commit()
        row = conn.execute("SELECT * FROM proveedores WHERE id=?", (new_id,)).fetchone()
        conn.close()
        return jsonify({"success":True,"message":"Proveedor creado","data":dict(row)}), 201
    except sqlite3.IntegrityError:
        return jsonify({"success":False,"error":"Email ya registrado"}), 409

@app.route("/api/proveedores/<int:id>", methods=["PUT"])
def update(id):
    conn = get_db()
    existing = conn.execute("SELECT * FROM proveedores WHERE id=?", (id,)).fetchone()
    if not existing:
        conn.close()
        return jsonify({"success":False,"error":"No encontrado"}), 404
    data = request.get_json()
    cur = dict(existing)
    conn.execute("UPDATE proveedores SET nombre=?,contacto=?,telefono=?,email=?,direccion=?,categoria=?,estado=? WHERE id=?",
        (data.get("nombre",cur["nombre"]),data.get("contacto",cur["contacto"]),data.get("telefono",cur["telefono"]),
         data.get("email",cur["email"]),data.get("direccion",cur["direccion"]),data.get("categoria",cur["categoria"]),
         data.get("estado",cur["estado"]),id))
    conn.commit()
    row = conn.execute("SELECT * FROM proveedores WHERE id=?", (id,)).fetchone()
    conn.close()
    return jsonify({"success":True,"message":"Actualizado","data":dict(row)})

@app.route("/api/proveedores/<int:id>", methods=["DELETE"])
def delete(id):
    conn = get_db()
    existing = conn.execute("SELECT * FROM proveedores WHERE id=?", (id,)).fetchone()
    if not existing:
        conn.close()
        return jsonify({"success":False,"error":"No encontrado"}), 404
    conn.execute("DELETE FROM proveedores WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"success":True,"message":f"Proveedor '{existing['nombre']}' eliminado"})

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5000)
