class Reserva:
    def __init__(self, estudiante, tutor, fecha,
                 modalidad="presencial", notas="", recordatorio=False,
                 lugar=None, duracion=None):
        self.estudiante = estudiante
        self.tutor = tutor
        self.fecha = fecha
        self.modalidad = modalidad
        self.notas = notas
        self.recordatorio = recordatorio
        self.lugar = lugar
        self.duracion = duracion

    def __str__(self):
        return (f"Reserva(estudiante={self.estudiante}, tutor={self.tutor}, "
                f"fecha={self.fecha}, modalidad={self.modalidad}, notas={self.notas}, "
                f"recordatorio={self.recordatorio}, lugar={self.lugar}, duracion={self.duracion})")
