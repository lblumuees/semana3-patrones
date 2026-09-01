from .notificacion import Notificacion

class NotificacionEmail(Notificacion):
    def enviar(self, mensaje: str):
        print(f"📧 Email enviado: {mensaje}")

class EmailFactory:
    def crear_notificacion(self) -> Notificacion:
        return NotificacionEmail()