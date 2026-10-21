# EcoTech Solutions – Evaluación Formativa Unidad 2 (TI3021)

**Integrantes:** (completar nombres)
**Líder de proyecto:** (completar)

## Descripción
Implementación en Python del diagrama UML de EcoTech Solutions
(`Persona`, `Empleado`, `Cliente`, `Proyecto`) con prueba de conexión a base de datos.

## Estructura
- `persona.py`, `empleado.py`, `cliente.py`, `proyecto.py`: una clase por archivo.
  `Empleado` y `Cliente` heredan de `Persona`; `Proyecto` se relaciona con `Empleado`.
- `config/database.py`: conexión a SQLite con la librería oficial `sqlite3`.
- `main.py`: programa de prueba (modelo + conexión).

## Cómo ejecutar
Requiere Python 3.9 o superior (no se instalan librerías externas):

    python main.py
