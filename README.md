# Workflow System

**Workflow System** es una plataforma experimental de automatización personal diseñada para capturar tareas, ideas, notas de estudio y recordatorios desde entradas simples, organizarlas y convertirlas progresivamente en flujos de trabajo útiles.

El proyecto se encuentra en una etapa temprana de desarrollo. La base actual no representa la arquitectura final, sino el primer cimiento funcional de un sistema más amplio que seguirá cambiando, creciendo y refinándose con el tiempo.

---

## Visión

La visión de Workflow System es construir un backend modular orientado a la automatización personal, capaz de recibir información desde distintas fuentes, clasificarla, almacenarla y prepararla para futuros procesos como recordatorios, planificación de estudio, paneles de control, integración con herramientas externas y procesamiento asistido por inteligencia artificial.

---

## Estado actual

Actualmente, el repositorio contiene la base inicial del sistema:

* Backend con FastAPI.
* Base de datos PostgreSQL.
* Modelo de datos con SQLAlchemy.
* Canal de entrada mediante bot de Telegram.
* Entorno local con Docker y Docker Compose.
* Clasificación básica de texto en tareas, estudio o notas.

La implementación actual es un MVP inicial. Muchos componentes son intencionalmente simples y podrán ser reemplazados, ampliados o rediseñados a medida que el sistema evolucione.

---

## ¿Qué puede hacer por ahora?

En su estado actual, el sistema puede:

* Ejecutarse localmente con Docker Compose.
* Recibir mensajes de texto desde un bot de Telegram.
* Enviar esos mensajes al backend de FastAPI.
* Clasificar el contenido como `task`, `study` o `note`.
* Guardar los registros en PostgreSQL.
* Listar los elementos almacenados desde la API.

---

## Stack tecnológico

* Python 3.11
* FastAPI
* Uvicorn
* PostgreSQL 15
* SQLAlchemy
* Pydantic
* Docker
* Docker Compose
* Telegram Bot API

---

## Estructura del proyecto

```
workflow-system/
├── app/
│   ├── core/
│   │   └── classifier.py
│   ├── db.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── telegram_bot.py
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Arquitectura general

```
Usuario en Telegram
        ↓
Bot de Telegram
        ↓
Backend FastAPI
        ↓
Clasificador
        ↓
Base de datos PostgreSQL
```

El bot de Telegram funciona como canal de entrada. La API recibe y estructura la información. El clasificador aplica una primera capa de organización. Finalmente, los datos se almacenan en PostgreSQL para ser utilizados por futuros módulos del sistema.

---

## Endpoints principales

### Verificar que la API está activa

```
GET /
```

Devuelve una respuesta básica indicando que el backend está funcionando.

---

### Crear un elemento

```
POST /items
```

Ejemplo de solicitud:

```
{
  "content": "estudiar bases de datos",
  "source": "manual",
  "status": "pending"
}
```

Ejemplo de respuesta:

```
{
  "id": 1,
  "content": "estudiar bases de datos",
  "type": "study",
  "source": "manual",
  "status": "pending",
  "created_at": "2026-05-02T22:00:00"
}
```

---

### Listar elementos

```
GET /items
```

Devuelve todos los elementos almacenados.

---

## Ejecución local

### 1\. Clonar el repositorio

```
git clone https://github.com/jdcamargo2/workflow-system.git
cd workflow-system
```

### 2\. Crear el archivo de entorno

```
cp .env.example .env
```

Luego edita el archivo `.env` y configura tus propios valores, especialmente:

```
TELEGRAM_BOT_TOKEN=tu_token_de_telegram
```

### 3\. Levantar el sistema

```
docker compose up --build
```

La API estará disponible en:

```
http://127.0.0.1:8000
```

La documentación automática de FastAPI estará disponible en:

```
http://127.0.0.1:8000/docs
```

---

## Variables de entorno


| Variable             | Descripción                                             |
| ---------------------- | ---------------------------------------------------------- |
| `POSTGRES_USER`      | Usuario de PostgreSQL                                    |
| `POSTGRES_PASSWORD`  | Contraseña de PostgreSQL                                |
| `POSTGRES_DB`        | Nombre de la base de datos                               |
| `DATABASE_URL`       | URL de conexión usada por SQLAlchemy                    |
| `TELEGRAM_BOT_TOKEN` | Token del bot de Telegram                                |
| `API_BASE_URL`       | URL interna usada por el bot para comunicarse con la API |

---

## Notas de desarrollo

Este proyecto es intencionalmente simple en su estado actual. Algunas decisiones son temporales y probablemente cambiarán:

* Las tablas se crean con `Base.metadata.create_all()` en lugar de migraciones.
* El clasificador está basado en palabras clave.
* Todavía no existe autenticación.
* Todavía no hay pruebas automatizadas.
* El bot usa polling en lugar de webhooks.
* El modelo de datos todavía es pequeño.
* La arquitectura aún está en exploración.

---

## Roadmap

Algunas mejoras previstas:

* Añadir un flujo de instalación más detallado.
* Agregar health checks en Docker Compose.
* Incorporar migraciones con Alembic.
* Añadir pruebas automatizadas.
* Mejorar el modelo de datos.
* Ampliar los tipos de elementos.
* Mejorar la lógica de clasificación.
* Añadir recordatorios y programación de tareas.
* Integrar herramientas externas de productividad.
* Crear una interfaz visual o panel administrativo.
* Mejorar el manejo de errores.
* Preparar una estructura más robusta para despliegue.

---

## Estado de producción

Workflow System **no está listo para producción**.

Antes de un despliegue real, el sistema necesitará:

* Gestión segura de secretos.
* Autenticación y autorización.
* Migraciones de base de datos.
* Mejor manejo de errores.
* Logging y observabilidad.
* Estrategia de respaldos.
* Pruebas automatizadas.
* Configuración de despliegue.
* Revisión de seguridad.

---

## Dirección del proyecto

Workflow System está siendo desarrollado como una base de automatización personal a largo plazo. Su propósito no es únicamente guardar tareas, sino construir una capa flexible capaz de conectar rutinas de estudio, planificación personal, recordatorios, bots, paneles de control y futuros procesos asistidos por IA.

La versión actual representa el punto de partida.
