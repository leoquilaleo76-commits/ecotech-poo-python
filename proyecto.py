from datetime import date
from empleado import Empleado


class Proyecto:
    """Se relaciona con Empleado: guarda los empleados asignados."""

    ESTADOS_VALIDOS: set[str] = {"Planificado", "En curso", "Finalizado"}

    def __init__(self, id_proyecto: str, nombre: str, descripcion: str,
                 fecha_inicio: date, estado: str = "Planificado"):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.estado = estado
        self._empleados: list[Empleado] = []   # relación con Empleado

    @property
    def id_proyecto(self) -> str:
        return self._id_proyecto

    @id_proyecto.setter
    def id_proyecto(self, id_proyecto: str) -> None:
        if not isinstance(id_proyecto, str) or not id_proyecto.strip():
            raise ValueError("El id del proyecto no puede estar vacío.")
        self._id_proyecto = id_proyecto.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        if not isinstance(nombre, str) or len(nombre.strip()) < 2:
            raise ValueError("El nombre del proyecto debe tener al menos 2 caracteres.")
        self._nombre = nombre.strip()

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion: str) -> None:
        if not isinstance(descripcion, str):
            raise TypeError("La descripción debe ser texto.")
        self._descripcion = descripcion.strip()

    @property
    def fecha_inicio(self) -> date:
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio: date) -> None:
        if not isinstance(fecha_inicio, date):
            raise TypeError("La fecha de inicio debe ser de tipo date.")
        self._fecha_inicio = fecha_inicio

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, estado: str) -> None:
        if not isinstance(estado, str):
            raise TypeError("El estado debe ser texto.")
        limpio = estado.strip().capitalize()
        if limpio not in self.ESTADOS_VALIDOS:
            opciones = ", ".join(sorted(self.ESTADOS_VALIDOS))
            raise ValueError(f"Estado '{estado}' no válido. Opciones: {opciones}.")
        self._estado = limpio

    def asignar_empleado(self, empleado: Empleado) -> bool:
        """True si se asignó; False si no es Empleado o ya estaba asignado."""
        if not isinstance(empleado, Empleado) or empleado in self._empleados:
            return False
        self._empleados.append(empleado)
        return True

    def listar_empleados(self) -> list[Empleado]:
        return list(self._empleados)   # copia: no se expone la lista interna

    def mostrar_datos(self) -> str:
        return (f"Proyecto [{self.id_proyecto}] {self.nombre}\n"
                f"Descripción: {self.descripcion}\n"
                f"Inicio: {self.fecha_inicio:%d-%m-%Y}\nEstado: {self.estado}\n"
                f"Empleados asignados: {len(self._empleados)}")

    def __str__(self) -> str:
        return self.mostrar_datos()

    def __repr__(self) -> str:
        return (f"Proyecto(id_proyecto='{self.id_proyecto}', nombre='{self.nombre}', "
                f"estado='{self.estado}')")
