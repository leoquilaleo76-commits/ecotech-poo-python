"""Conexión a la base de datos usando la librería oficial sqlite3."""
import sqlite3


class ConexionBD:
    def __init__(self, ruta: str = "ecotech.db"):
        self._ruta = ruta
        self._conn = None

    def conectar(self) -> sqlite3.Connection:
        try:
            self._conn = sqlite3.connect(self._ruta)
            self._conn.execute("PRAGMA foreign_keys = ON")
            return self._conn
        except sqlite3.Error as e:
            raise ConnectionError(f"No se pudo conectar a la base de datos: {e}")

    def probar_conexion(self) -> str:
        """Prueba de conexión: abre la BD y ejecuta una consulta simple."""
        conn = self.conectar()
        version = conn.execute("SELECT sqlite_version()").fetchone()[0]
        return f"Conexión exitosa a '{self._ruta}' (SQLite {version})"

    def crear_tablas(self) -> None:
        conn = self._conn or self.conectar()
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS empleado (
                rut TEXT PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT NULL,
                correo TEXT NOT NULL, cargo TEXT, sueldo_base REAL);
            CREATE TABLE IF NOT EXISTS cliente (
                rut TEXT PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT NULL,
                correo TEXT NOT NULL, direccion TEXT, telefono TEXT);
            CREATE TABLE IF NOT EXISTS proyecto (
                id_proyecto TEXT PRIMARY KEY, nombre TEXT NOT NULL,
                descripcion TEXT, fecha_inicio TEXT, estado TEXT);
            CREATE TABLE IF NOT EXISTS proyecto_empleado (
                id_proyecto TEXT REFERENCES proyecto(id_proyecto),
                rut_empleado TEXT REFERENCES empleado(rut),
                PRIMARY KEY (id_proyecto, rut_empleado));
        """)
        conn.commit()

    def cerrar(self) -> None:
        if self._conn:
            self._conn.close()
            self._conn = None
