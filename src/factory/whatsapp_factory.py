from .notificacion import Notificacion

class NotificacionWhatsApp(Notificacion):
    def enviar(self, mensaje: str):
        print(f"💬 WhatsApp enviado: {mensaje}")

class WhatsAppFactory:
    def crear_notificacion(self) -> Notificacion:
        return NotificacionWhatsApp()
