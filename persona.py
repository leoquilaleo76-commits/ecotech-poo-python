class Persona:
    """Superclase del modelo UML: nombre, apellido, rut, correo."""

    def __init__(self, nombre: str, apellido: str, rut: str, correo: str):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.correo = correo

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        if not isinstance(nombre, str) or len(nombre.strip()) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        self._nombre = nombre.strip().title()

    @property
    def apellido(self) -> str:
        return self._apellido

    @apellido.setter
    def apellido(self, apellido: str) -> None:
        if not isinstance(apellido, str) or len(apellido.strip()) < 2:
            raise ValueError("El apellido debe tener al menos 2 caracteres.")
        self._apellido = apellido.strip().title()

    @property
    def rut(self) -> str:
        return self._rut

    @rut.setter
    def rut(self, rut: str) -> None:
        if not isinstance(rut, str) or not rut.strip():
            raise ValueError("El RUT no puede estar vacío.")
        self._rut = rut.strip().upper()

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, correo: str) -> None:
        if not isinstance(correo, str) or "@" not in correo:
            raise ValueError("El correo no es válido.")
        self._correo = correo.strip().lower()

    def obtener_nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellido}"

    def obtener_rut(self) -> str:
        return self.rut

    def obtener_correo(self) -> str:
        return self.correo

    def mostrar_datos(self) -> str:
        return (f"Nombre: {self.obtener_nombre_completo()}\n"
                f"RUT: {self.rut}\nCorreo: {self.correo}")

    def __str__(self) -> str:
        return self.mostrar_datos()

    def __repr__(self) -> str:
        return (f"Persona(nombre='{self.nombre}', apellido='{self.apellido}', "
                f"rut='{self.rut}', correo='{self.correo}')")
