from persona import Persona


class Cliente(Persona):
    """Hereda de Persona. Agrega direccion y telefono."""

    def __init__(self, nombre: str, apellido: str, rut: str, correo: str,
                 direccion: str, telefono: str):
        super().__init__(nombre, apellido, rut, correo)  # reutiliza Persona
        self.direccion = direccion
        self.telefono = telefono

    @property
    def direccion(self) -> str:
        return self._direccion

    @direccion.setter
    def direccion(self, direccion: str) -> None:
        if not isinstance(direccion, str) or not direccion.strip():
            raise ValueError("La dirección no puede estar vacía.")
        self._direccion = direccion.strip()

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, telefono: str) -> None:
        if not isinstance(telefono, str) or not telefono.strip():
            raise ValueError("El teléfono no puede estar vacío.")
        self._telefono = telefono.strip()

    def obtener_datos_contacto(self) -> str:
        return f"{self.correo} | {self.telefono} | {self.direccion}"

    def mostrar_datos(self) -> str:
        return (f"{super().mostrar_datos()}\nDirección: {self.direccion}\n"
                f"Teléfono: {self.telefono}")

    def __repr__(self) -> str:
        return (f"Cliente(nombre='{self.nombre}', apellido='{self.apellido}', "
                f"rut='{self.rut}', correo='{self.correo}', "
                f"direccion='{self.direccion}', telefono='{self.telefono}')")
