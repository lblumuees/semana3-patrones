from abc import ABC, abstractmethod

class Notificacion(ABC):
    """
    Clase abstracta que define el contrato para todas las notificaciones.
    """

    @abstractmethod
    def enviar(self, mensaje: str):
        """
        Método abstracto que debe implementar cada tipo de notificación.
        """
        pass