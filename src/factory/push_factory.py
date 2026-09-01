from .notificacion import Notificacion

class NotificacionPush(Notificacion):
    def enviar(self, mensaje: str):
        print(f"📲 Notificación Push enviada: {mensaje}")


class PushFactory:
    def crear_notificacion(self) -> Notificacion:
        return NotificacionPush()
