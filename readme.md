# 🏭 Sistema de Gestión de Proveedores — API REST

## Descripción
API REST completa con operaciones **CRUD** (Create, Read, Update, Delete) para la gestión de proveedores, desarrollada con **Python Flask** y **SQLite**. Incluye un frontend interactivo y documentación de pruebas con Postman.

---

## 📁 Estructura del Proyecto

```
proveedores-api/
│
├── app.py              # API REST (Flask + SQLite)
├── proveedores.db      # Base de datos SQLite (se genera automáticamente)
├── index.html          # Frontend interactivo con CRUD completo
├── README.md           # Este archivo
└── .gitignore
```

---

## ⚙️ Tecnologías

| Tecnología | Uso |
|---|---|
| Python 3 | Lenguaje principal |
| Flask | Framework web / API REST |
| Flask-CORS | Manejo de CORS para el frontend |
| SQLite | Base de datos embebida |
| HTML/CSS/JS | Frontend interactivo |

---

## 🚀 Cómo ejecutar

### 1. Instalar dependencias
```bash
pip install flask flask-cors
```

### 2. Ejecutar la API
```bash
python app.py
```
La API correrá en: `http://localhost:5000`

### 3. Abrir el Frontend
Abre `index.html` en tu navegador.

---

## 🔗 Endpoints de la API

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/api/proveedores` | Obtener todos los proveedores |
| `GET` | `/api/proveedores/<id>` | Obtener un proveedor por ID |
| `POST` | `/api/proveedores` | Crear nuevo proveedor |
| `PUT` | `/api/proveedores/<id>` | Actualizar proveedor existente |
| `DELETE` | `/api/proveedores/<id>` | Eliminar proveedor |

---

## 📮 Parte II — Pruebas con Postman

### Configuración inicial
- **Base URL:** `http://localhost:5000`
- **Headers:** `Content-Type: application/json`

### 1️⃣ GET — Consultar todos los proveedores
```
GET http://localhost:5000/api/proveedores
```
**Respuesta:**
```json
{
  "success": true,
  "total": 5,
  "data": [...]
}
```

### 2️⃣ POST — Insertar nuevo proveedor
```
POST http://localhost:5000/api/proveedores
Content-Type: application/json

{
  "nombre":    "Distribuidora XYZ",
  "contacto":  "Juan Pérez",
  "telefono":  "507-6100-0000",
  "email":     "juan@distribxyz.pa",
  "direccion": "Betania, Panamá",
  "categoria": "Insumos",
  "estado":    "activo"
}
```

### 3️⃣ PUT — Actualizar proveedor
```
PUT http://localhost:5000/api/proveedores/1
Content-Type: application/json

{
  "telefono": "507-7000-9999",
  "estado":   "inactivo"
}
```

### 4️⃣ DELETE — Eliminar proveedor
```
DELETE http://localhost:5000/api/proveedores/6
```

---

## 🏪 Parte III — Caso de Uso

### Sistema de Gestión de Proveedores Médicos — MedPanamá S.A.

**Actores:** Departamento de Compras  
**Objetivo:** Gestionar proveedores médicos de forma eficiente

#### Flujo del Caso de Uso:

1. **Consultar (SELECT):** El encargado de compras consulta los proveedores activos de categoría "Médico" para evaluar opciones antes de una compra.

2. **Registrar (INSERT):** Llega una oferta de un nuevo proveedor "Equipos Médicos del Istmo". El encargado lo registra en el sistema con todos sus datos de contacto.

3. **Actualizar (UPDATE):** El proveedor "MediSupplies" notifica un cambio de número telefónico. Se actualiza la información en el sistema.

4. **Consultar detalle (SELECT por ID):** Antes de realizar un pedido, se consulta la información completa de un proveedor específico para verificar que está activo y tiene datos correctos.

5. **Eliminar (DELETE):** Un proveedor cierra operaciones. Se elimina del sistema para mantener la base de datos limpia.

---

## 🗄️ Esquema de la Base de Datos

```sql
CREATE TABLE proveedores (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre          TEXT    NOT NULL,
    contacto        TEXT    NOT NULL,
    telefono        TEXT    NOT NULL,
    email           TEXT    NOT NULL UNIQUE,
    direccion       TEXT,
    categoria       TEXT    NOT NULL,
    estado          TEXT    DEFAULT 'activo',
    fecha_registro  TEXT    DEFAULT (datetime('now'))
);
```

---

## 📝 Datos de muestra incluidos

| # | Nombre | Categoría | Estado |
|---|---|---|---|
| 1 | TechSupply S.A. | Tecnología | Activo |
| 2 | Distribuidora Global | Insumos | Activo |
| 3 | Papelería Nacional | Papelería | Activo |
| 4 | LogiPanamá | Logística | Inactivo |
| 5 | MediSupplies | Médico | Activo |

---

## 📌 Notas para el repositorio Git

```bash
# Comandos para subir al repositorio
git init
git add .
git commit -m "feat: API REST CRUD de Proveedores con Flask y SQLite"
git branch -M main
git remote add origin https://github.com/usuario/proveedores-api.git
git push -u origin main
```