from .notificacion import Notificacion

class NotificacionSMS(Notificacion):
    def enviar(self, mensaje: str):
        print(f"📱 SMS enviado: {mensaje}")

class SMSFactory:
    def crear_notificacion(self) -> Notificacion:
        return NotificacionSMS()
