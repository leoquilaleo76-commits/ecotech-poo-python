from datetime import date

from cliente import Cliente
from config.database import ConexionBD
from empleado import Empleado
from proyecto import Proyecto


def probar_modelo() -> None:
    """Pasos 1 y 2: clases del UML, herencia, relaciones y encapsulamiento."""
    emp1 = Empleado("Camila", "Rojas", "11.111.111-1", "camila@ecotech.cl",
                    "Jefa de Proyecto", 1800000)
    emp2 = Empleado("Diego", "Soto", "22.222.222-2", "diego@ecotech.cl",
                    "Desarrollador", 1400000)
    cli = Cliente("Marta", "Pérez", "33.333.333-3", "marta@cliente.cl",
                  "Av. Providencia 123", "+56 9 1234 5678")
    proyecto = Proyecto("P-001", "Sistema de Gestión Interna",
                        "Optimización del sistema de gestión de EcoTech",
                        date(2026, 10, 1))

    print("Asignar Camila:", proyecto.asignar_empleado(emp1))
    print("Asignar Diego:", proyecto.asignar_empleado(emp2))
    print("Asignar Diego otra vez:", proyecto.asignar_empleado(emp2))
    print("Asignar un cliente:", proyecto.asignar_empleado(cli))

    for objeto in (emp1, cli, proyecto):
        print("-" * 30)
        print(objeto)
    print("-" * 30)
    print(f"Sueldo neto de {emp2.obtener_nombre_completo()}: "
          f"${emp2.calcular_sueldo_neto():,.0f}")
    print("Equipo:", [e.obtener_nombre_completo() for e in proyecto.listar_empleados()])

    # Demostración de validación (encapsulamiento)
    try:
        emp2.sueldo_base = -100
    except ValueError as e:
        print("Validación:", e)


def probar_conexion() -> None:
    """Paso 3: conexión a la base de datos."""
    bd = ConexionBD("ecotech.db")
    try:
        print(bd.probar_conexion())
        bd.crear_tablas()
        print("Tablas creadas correctamente.")
    except ConnectionError as e:
        print(e)
    finally:
        bd.cerrar()


def main() -> None:
    probar_modelo()
    print("=" * 30)
    probar_conexion()


if __name__ == "__main__":
    main()
