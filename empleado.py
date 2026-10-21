from persona import Persona


class Empleado(Persona):
    """Hereda de Persona. Agrega cargo y sueldoBase."""

    DESCUENTO_AFP: float = 0.10     # supuesto: ajustar si el modelo usa otros valores
    DESCUENTO_SALUD: float = 0.07

    def __init__(self, nombre: str, apellido: str, rut: str, correo: str,
                 cargo: str, sueldo_base: float):
        super().__init__(nombre, apellido, rut, correo)  # reutiliza Persona
        self.cargo = cargo
        self.sueldo_base = sueldo_base

    @property
    def cargo(self) -> str:
        return self._cargo

    @cargo.setter
    def cargo(self, cargo: str) -> None:
        if not isinstance(cargo, str) or not cargo.strip():
            raise ValueError("El cargo no puede estar vacío.")
        self._cargo = cargo.strip()

    @property
    def sueldo_base(self) -> float:
        return self._sueldo_base

    @sueldo_base.setter
    def sueldo_base(self, sueldo_base: float) -> None:
        if not isinstance(sueldo_base, (int, float)):
            raise TypeError("El sueldo base debe ser un número.")
        if sueldo_base < 0:
            raise ValueError("El sueldo base no puede ser negativo.")
        self._sueldo_base = sueldo_base

    def obtener_cargo(self) -> str:
        return self.cargo

    def calcular_sueldo_neto(self) -> float:
        descuentos = self.sueldo_base * (self.DESCUENTO_AFP + self.DESCUENTO_SALUD)
        return self.sueldo_base - descuentos

    def mostrar_datos(self) -> str:
        return (f"{super().mostrar_datos()}\nCargo: {self.cargo}\n"
                f"Sueldo base: ${self.sueldo_base:,.0f}")

    def __repr__(self) -> str:
        return (f"Empleado(nombre='{self.nombre}', apellido='{self.apellido}', "
                f"rut='{self.rut}', correo='{self.correo}', "
                f"cargo='{self.cargo}', sueldo_base={self.sueldo_base})")
