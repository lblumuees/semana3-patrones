# Semana 3 - Patrones de Diseño en Python

Este proyecto implementa dos patrones de diseño creacionales: **Factory Method** y **Builder**, aplicados al contexto de un sistema de tutorías.  
El objetivo es demostrar cómo estos patrones ayudan a mejorar la extensibilidad, legibilidad y organización del código.

---

## 📂 Estructura del repositorio

semana3-patrones/
├── README.md
├── docs/                  # Diagramas UML y documentación
│   ├── factory-method.puml
│   ├── factory-method.png
│   ├── builder.puml
│   └── builder.png
├── src/                   # Código fuente en Python
│   ├── factory/           # Implementación del patrón Factory Method
│   │   ├── init.py
│   │   ├── notificacion.py
│   │   ├── email_factory.py
│   │   ├── sms_factory.py
│   │   ├── push_factory.py
│   │   └── whatsapp_factory.py
│   └── builder/           # Implementación del patrón Builder
│       ├── init.py
│       ├── reserva.py
│       └── reserva_builder.py
└── tests/                 # Pruebas unitarias
├── test_factory.py
└── test_builder.py



---

## 🚀 Patrones implementados

### 🔹 Factory Method
- **Problema que resuelve:** creación de distintas variantes de notificación sin acoplar el cliente a clases concretas.  
- **Participantes:**  
  - `Notificacion` (interfaz abstracta)  
  - `NotificacionEmail`, `NotificacionSMS`, `NotificacionPush`, `NotificacionWhatsApp` (productos concretos)  
  - `EmailFactory`, `SMSFactory`, `PushFactory`, `WhatsAppFactory` (fábricas concretas)  

**Ejemplo de uso:**
```python
from src.factory.email_factory import EmailFactory

factory = EmailFactory()
notif = factory.crear_notificacion()
notif.enviar("Reunión confirmada para mañana a las 10 AM")


### 🔹 Builder
- **Problema que resuelve: construcción de objetos complejos (Reserva) con parámetros obligatorios y opcionales, evitando constructores telescópicos.

- **Participantes:** 

	- Reserva (producto principal)
	- ReservaBuilder (builder con Fluent API)
	
**Ejemplo de uso:**
```python
from datetime import date
from src.builder import ReservaBuilder

reserva_virtual = ReservaBuilder("Luis", "Tutor Juan", date.today()) \
    .with_modalidad("virtual") \
    .with_notas("Traer laptop") \
    .with_recordatorio(True) \
    .build()

print(reserva_virtual)




## Tecnologías
- Python 3.14.3
- UML (PlantUML para diagramas)
- Pytest (para pruebas unitarias)
- Git + GitHub (control de versiones)