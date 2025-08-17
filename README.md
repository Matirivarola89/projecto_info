
Blog de Autos: Motor sin Límites 
​Proyecto de blog web desarrollado con el framework Django para la promoción y publicación de artículos sobre vehículos. Esta aplicación permite a los usuarios interactuar con el contenido a través de posts, comentarios y un sistema de autenticación de perfiles.

Tecnologías Utilizadas
​Backend: Python, Django
​Frontend: HTML, CSS (Bootstrap 5), JavaScript
​Base de Datos: SQLite
​Despliegue: PythonAnywhere


Características Principales
​Perfiles de Usuario: Acceso de múltiples perfiles, incluyendo Administrador (admin) y Registrado (registrado).
​Gestión de Posts: Los usuarios administradores pueden crear, actualizar y eliminar posts.
​Sistema de Comentarios: Los usuarios registrados y autenticados pueden comentar en los posts.
​Autenticación y Autorización: Sistema de login y registro de usuarios, con restricciones de acceso a ciertas vistas (como el registro para usuarios ya logueados y la creación de posts para usuarios no administradores).
​Filtrado y Búsqueda: Funcionalidad para filtrar posts por fecha, categoría y número de comentarios.

Requisitos Previos
​Asegúrate de tener instalado lo siguiente en tu sistema:
​Python 3.x
​pip (gestor de paquetes de Python)

Instalación y Configuración
​Sigue estos pasos para configurar el proyecto en tu entorno local.

1.Clonar el repositorio:

git clone https://github.com/Matirivarola89/projecto_info

2.Crear y activar un entorno virtual:

python -m venv venv
source venv/bin/activate  # En Linux/macOS
# venv\Scripts\activate   # En Windows

3.Instalar las dependencias del proyecto:

pip install -r requirements.txt

4.Configurar la base de datos y migrar:

python manage.py makemigrations
python manage.py migrate

5.Crear un superusuario (administrador) para acceder al panel de administración:

python manage.py createsuperuser

6.Recopilar archivos estáticos y de medios:

python manage.py collectstatic

7.Ejecutar el servidor de desarrollo:

python manage.py runserver

Ahora puedes acceder al proyecto en http://127.0.0.1:8000/.


Estructura del Proyecto
​auto_blog_project/: Directorio principal del proyecto.
​accounts/: Aplicación para la gestión de usuarios (registro y autenticación).
​blog/: Aplicación principal que contiene la lógica del blog (modelos, vistas, plantillas).
​media/: Directorio para los archivos de medios (imágenes de posts, logos, etc.).
​templates/: Directorio que almacena las plantillas HTML base del proyecto.
​requirements.txt: Archivo con todas las dependencias del proyecto.
​manage.py: Utilidad de línea de comandos de Django.

Autor
​Grupo 2

​Licencia
​Este proyecto está bajo la Licencia MIT.