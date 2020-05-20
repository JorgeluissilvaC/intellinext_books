# Instrucciones de instalación:
1. Validamos que la máquina tenga instalado Python 2. Este proyecto se desarrolló en Python 2.7.18.
2. Instalar modulo virtualenv de Python:
	`pip install virtualenv`
3. Creamos un ambiente virtual para instalar las dependencias del proyecto. 
  `virtualenv <Nombre del entorno>`
4. Activamos el entorno virtual, ingresamos dentro de la carpeta   <Nombre del entorno> y ejecutamos:
  `Scripts\activate`    
5. Descargamos el repositorio de GitHub, con el siguiente comando (Validamos que la máquinatenga Git instalado):
  `git clone https://github.com/JorgeluissilvaC/intellinext_books`
6. Entramos a la carpeta del repositorio e instalamos las dependencias, con el siguiente comando:
  `pip install -r requirements.txt`
7. Realizamoslas migraciones necesarias a la base de datos. 
  `python manage.py makemigrations`               
  `python manage.py migrate`
8. En la carpeta base del proyecto, corremos el servidor de desarrollo:
	  `python manage.py runserver`
9. Procedemosa utilizar la aplicación. Estará disponible en la URL:
  http://localhost:8000/
