import sqlite3
from cliente import Cliente
from empleado import Empleado


def inicializar_base_datos():
  """Paso 3 y 4: Conexión y creación de tablas con manejo de errores (try-except)."""
  try:
    # Conexión a la base de datos oficial de Python (sqlite3)
    conexion = sqlite3.connect("ecotech.db")
    cursor = conexion.cursor()

    # Creación de tabla para Empleados
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                rut TEXT UNIQUE NOT NULL,
                correo TEXT NOT NULL,
                cargo TEXT NOT NULL,
                sueldo_base REAL NOT NULL
            )
        """)

    conexion.commit()
    print("[✔] Base de datos y tablas inicializadas correctamente.")
  except sqlite3.Error as e:
    print(f"[✘] Error al conectar o inicializar la base de datos: {e}")
  finally:
    if conexion:
      conexion.close()


def registrar_empleado():
  """Operación CRUD: CREATE (Registrar) con manejo de excepciones y validación de entradas."""
  print("\n--- REGISTRAR NUEVO EMPLEADO ---")
  try:
    nombre = input("Ingrese nombre: ").strip()
    if not nombre:
      raise ValueError("El nombre no puede estar vacío.")

    apellido = input("Ingrese apellido: ").strip()
    rut = input("Ingrese RUT: ").strip()
    correo = input("Ingrese correo: ").strip()
    cargo = input("Ingrese cargo: ").strip()

    # Validación de entrada numérica para el sueldo (evita que el programa caiga por errores de usuario)
    sueldo_base = float(input("Ingrese sueldo base: "))
    if sueldo_base < 0:
      raise ValueError("El sueldo no puede ser negativo.")

    # Instanciamos el objeto usando la clase Empleado (POO)
    nuevo_empleado = Empleado(nombre, apellido, rut, correo, cargo, sueldo_base)

    # Guardar en la Base de Datos
    conexion = sqlite3.connect("ecotech.db")
    cursor = conexion.cursor()

    cursor.execute(
        """
            INSERT INTO empleados (nombre, apellido, rut, correo, cargo, sueldo_base)
            VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            nuevo_empleado.nombre,
            nuevo_empleado.apellido,
            nuevo_empleado.rut,
            nuevo_empleado.correo,
            nuevo_empleado.cargo,
            nuevo_empleado.sueldo_base,
        ),
    )

    conexion.commit()
    print("[✔] ¡Empleado registrado con éxito en la base de datos!")

  except ValueError as ve:
    print(f"[✘] Error de validación: {ve}")
  except sqlite3.IntegrityError:
    print("[✘] Error: El RUT ingresado ya se encuentra registrado.")
  except sqlite3.Error as e:
    print(f"[✘] Error en la base de datos: {e}")
  finally:
    if "conexion" in locals() and conexion:
      conexion.close()


def listar_empleados():
  """Operación CRUD: READ (Consultar/Listar) con manejo de excepciones."""
  print("\n--- LISTA DE EMPLEADOS ---")
  try:
    conexion = sqlite3.connect("ecotech.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM empleados")
    filas = cursor.fetchall()

    if not filas:
      print("No hay empleados registrados.")
      return

    for fila in filas:
      print(
          f"ID: {fila[0]} | Nombre: {fila[1]} {fila[2]} | RUT: {fila[3]} |"
          f" Cargo: {fila[5]} | Sueldo: ${fila[6]}"
      )

  except sqlite3.Error as e:
    print(f"[✘] Error al consultar los datos: {e}")
  finally:
    if "conexion" in locals() and conexion:
      conexion.close()


def actualizar_empleado():
  """Operación CRUD: UPDATE (Actualizar) con manejo de excepciones."""
  print("\n--- ACTUALIZAR SUELDO DE EMPLEADO ---")
  listar_empleados()
  try:
    emp_id = int(
        input(
            "Ingrese el ID del empleado que desea actualizar: "
        )
    )
    nuevo_sueldo = float(input("Ingrese el nuevo sueldo base: "))

    conexion = sqlite3.connect("ecotech.db")
    cursor = conexion.cursor()

    cursor.execute(
        "UPDATE empleados SET sueldo_base = ? WHERE id = ?",
        (nuevo_sueldo, emp_id),
    )
    conexion.commit()

    if cursor.rowcount > 0:
      print("[✔] Sueldo actualizado correctamente.")
    else:
      print("[✘] No se encontró un empleado con el ID indicado.")

  except ValueError:
    print("[✘] Error: Debe ingresar valores numéricos válidos.")
  except sqlite3.Error as e:
    print(f"[✘] Error en la base de datos: {e}")
  finally:
    if "conexion" in locals() and conexion:
      conexion.close()


def eliminar_empleado():
  """Operación CRUD: DELETE (Eliminar) con manejo de excepciones."""
  print("\n--- ELIMINAR EMPLEADO ---")
  listar_empleados()
  try:
    emp_id = int(input("Ingrese el ID del empleado a eliminar: "))

    conexion = sqlite3.connect("ecotech.db")
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM empleados WHERE id = ?", (emp_id,))
    conexion.commit()

    if cursor.rowcount > 0:
      print("[✔] Empleado eliminado correctamente.")
    else:
      print("[✘] No se encontró un empleado con el ID indicado.")

  except ValueError:
    print("[✘] Error: El ID debe ser un número entero.")
  except sqlite3.Error as e:
    print(f"[✘] Error en la base de datos: {e}")
  finally:
    if "conexion" in locals() and conexion:
      conexion.close()


def menu():
  """Menú principal interactivo de la aplicación."""
  inicializar_base_datos()
  while True:
    print("\n==============================")
    print("   SISTEMA ECOTECH SOLUTIONS  ")
    print("==============================")
    print("1. Registrar Empleado (Create)")
    print("2. Listar Empleados (Read)")
    print("3. Actualizar Empleado (Update)")
    print("4. Eliminar Empleado (Delete)")
    print("5. Salir")

    try:
      opcion = int(input("Seleccione una opción: "))
      if opcion == 1:
        registrar_empleado()
      elif opcion == 2:
        listar_empleados()
      elif opcion == 3:
        actualizar_empleado()
      elif opcion == 4:
        eliminar_empleado()
      elif opcion == 5:
        print("Saliendo del sistema. ¡Hasta luego!")
        break
      else:
        print("[!] Opción inválida. Ingrese un número entre 1 y 5.")
    except ValueError:
      print("[✘] Error: Debe ingresar obligatoriamente un número entero.")


if __name__ == "__main__":
  menu()
