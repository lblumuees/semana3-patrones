from .reserva import Reserva

class ReservaBuilder:
    def __init__(self, estudiante, tutor, fecha):
        # Campos obligatorios
        self.estudiante = estudiante
        self.tutor = tutor
        self.fecha = fecha
        # Campos opcionales con valores por defecto
        self.modalidad = "presencial"
        self.notas = ""
        self.recordatorio = False
        self.lugar = None
        self.duracion = None

    # Métodos Fluent API
    def with_modalidad(self, modalidad):
        self.modalidad = modalidad
        return self

    def with_notas(self, notas):
        self.notas = notas
        return self

    def with_recordatorio(self, recordatorio=True):
        self.recordatorio = recordatorio
        return self

    def with_lugar(self, lugar):
        self.lugar = lugar
        return self

    def with_duracion(self, duracion):
        self.duracion = duracion
        return self

    # Validación y construcción final
    def build(self):
        if not self.estudiante:
            raise ValueError("El campo 'estudiante' es obligatorio.")
        if not self.tutor:
            raise ValueError("El campo 'tutor' es obligatorio.")
        if not self.fecha:
            raise ValueError("El campo 'fecha' es obligatorio.")

        return Reserva(self.estudiante, self.tutor, self.fecha,
                       self.modalidad, self.notas, self.recordatorio,
                       self.lugar, self.duracion)
