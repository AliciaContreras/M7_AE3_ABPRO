# Sistema de Gestión Académica - Django

Este proyecto implementa la capa de datos para una plataforma de gestión académica utilizando **Django ORM** y **MySQL**. El modelo de datos resuelve relaciones complejas entre profesores, estudiantes y cursos, asegurando la integridad referencial y la escalabilidad.

## 🗂️ Estructura de Datos y Relaciones

La aplicación `academico` modela las siguientes relaciones:

*   **Uno a Muchos (ForeignKey):** 
    *   **Profesor ↔ Cursos:** Un profesor imparte varios cursos. Se implementa **borrado en cascada** (si se elimina el profesor, se eliminan sus cursos).

*   **Muchos a Muchos (ManyToManyField):** 
    *   **Estudiantes ↔ Cursos:** Gestionado mediante una tabla intermedia (**Inscripcion**) que almacena datos adicionales:
        *   Fecha de inscripción.
        *   Estado (`Activo` o `Finalizado`).
        *   Nota final.

*   **Uno a Uno (OneToOneField):** 
    *   **Estudiante ↔ Perfil:** Información extendida del estudiante (biografía, foto, redes sociales).

## ⚙️ Requisitos Previos

*   Python 3.x
*   Django
*   Servidor MySQL
*   Librería `mysqlclient`

## 🚀 Instalación y Ejecución

1.  **Configurar Base de Datos:**
    Asegúrate de configurar las credenciales de MySQL en `settings.py`.

2.  **Aplicar Migraciones:**
    Crea las tablas en la base de datos ejecutando:
    ```bash
    python manage.py makemigrations academico
    python manage.py migrate
    ```

3.  **Verificación:**
    Para probar las relaciones y la integridad de datos, utiliza la consola interactiva:
    ```bash
    python manage.py shell
    ```