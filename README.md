# Tercer Pre entrega de Python
# DreamChopper - Página Web de Ventas de Indumentaria y Accesorios en Cuero para Motociclistas

Bienvenido al repositorio de DreamChopper, una página web de comercio electrónico especializada en la venta de indumentaria y accesorios de cuero para entusiastas de las motocicletas.

## Descripción del Proyecto

DreamChopper es una plataforma en línea diseñada para conectar a los amantes de las motos con productos de alta calidad hechos de cuero. Desde camperas y pantalones hasta guantes, chaparreras y chalecos, nuestra tienda ofrece una amplia variedad de productos para que los motociclistas encuentren lo que necesitan para su viaje.

## Características

- Búsqueda y navegación intuitiva de productos.
- Catálogo categorizado de indumentaria y accesorios en cuero.
- Páginas de detalle de productos 
- Página con imágenes de productos

## Tecnologías Utilizadas

- **Django:** Framework de desarrollo web de Python.
- **HTML, CSS y JavaScript:** Tecnologías estándar para el desarrollo web front-end.
- **Bootstrap:** Para crear una interfaz responsive y atractiva.
- **SQLite3:** Base de datos incorporada para el desarrollo inicial.
- **Visual Studio Code:** Entorno de desarrollo integrado.

## Instalación y Uso

1. Clona este repositorio: `git clone https://github.com/tuusuario/motoleather.git`
2. Navega al directorio del proyecto: `cd dreamchopper`
3. Instala las dependencias: `pip install -r requirements.txt`
4. Realiza las migraciones de la base de datos: `python manage.py migrate`
5. Carga datos de ejemplo (opcional): `python3 manage.py loaddata sample_data.json`
6. Inicia el servidor de desarrollo: `python3 manage.py runserver`
7. Abre tu navegador y visita: `http://localhost:8000`
8. Para la agregación de productos se hace mediante un formulario y se busca de la siguiente forma:
   Ej: campera_form, chaleco_form, guantes_form, chaparreras_form, pantalon_form.
9. Para buscar información en la base de datos se hace mediante un formulario de la siguiente manera:
   Ej: buscar_campera, buscar_chaleco, buscar_chaparreras, buscar_guantes, buscar_pantalon

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar la plataforma, sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una rama para tu función o corrección: `git checkout -b nueva-funcion`
3. Realiza tus cambios y realiza commits: `git commit -m "Agregada la función de XYZ"`
4. Sube tus cambios a tu repositorio fork: `git push origin nueva-funcion`
5. Abre un Pull Request en este repositorio.
