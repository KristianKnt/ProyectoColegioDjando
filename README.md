# Problema Del ejercicio:
    - una intitucion educativa nesecita una plataforma para asignar las notas de varios estudiantes en diferentes materias.
    - una estudiante puede estar inscrito en varias materias
    - la calificaion de una materia se compone por tres cortes, y se califican en un rango de 0,5
    - el estudiante aprueba si el pormedio de los cortes es de 3,0
    
    ---------------------------------------------------------
    
    
    Caracteristicas 
    
    lo primero es clonar el repositorio  con su respectivo link  https://github.com/KristianKnt/ProyectoColegioDjando.git
    
    Tener instalado:  
        python 3.10.7
        Django 4.1.1
    
    
    El Ejercicio se hizo con las siguentes herramientas
        - Xampp (phpmyadim)
        - Xampp (servdor apache)
        - Visual Studio Code
    
    una vez clonado el repositorio abrirlo a travez de visual studio 
    
    antes de ejecutarlo debe instalar desde la consola 
    "pip3 install PyMySql" para hacer la conexion a la base da datos 
    
    para ejecutar la solucion antes debe crear la base de datos llamada colegio y configurar el puerto 3307 si no debe entrar a sistema2/sistema2/settings.py y buscar DATABASES 
            DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME':'colegio',
                'USER':'root',
                'PASSWORD':'',
                'HOST':'localhost',
                'PORT':'3307'
            }
        }
        
    Y hacer el cambio al puerto del servidor el nombre de la base de datos el user y el password en caso de no tener clave dejarlo vacio 
    
    
    ya una vez hecho lo anterio procedemos a abrirl la terminar y buscar el ejecicio entramos a la carpeta sistema2 y listarlo de tal manera que estemos adentro y podamos ver el archivo manage.py 
    
    ![Image text](https://github.com/KristianKnt/ProyectoColegioDjando/blob/main/ImagenDeGit1.png)
    
    si no se muetra la imagen esta en la entrada del repositorio llamada como ImagenDeGit1.png como ejemplo
    
    dirigirse a xampp y iniciar el servidor apache y tambien Mysql
    ![Image text](https://github.com/KristianKnt/ProyectoColegioDjando/blob/main/ImagenDeGit1.png
    ImagenDeGit2.png
    
    Antes de iniciar el proyecto debemos hacer las siguentes lineas para que se creen las tablas en la base de datos 
        - pyhton manaje.py makemigrations
        - pyhton manaje.py migrate
        (con estas dos lineas estamos creando las tablas en la cual ya tiene las claves primarias y foraneas del ejercicio)
    
    una vez adentro podremos iniciar el proyecyto con el seguiente comando :
    pyhton manage.py runserver 
    
    ![Image text](https://github.com/KristianKnt/ProyectoColegioDjando/blob/main/ImagenDeGit3.png
    ImagenDeGit3.png
    
    
    una vez cargue podemos dirigirnos al nevegador con la direccion http://127.0.0.1//8000/admin
    
    en ese momento ya esta en el servidor y solo queda loguearse con la siguiente credencial 
        User: cristianr
        Password: Holamund0
        
    ya una vez adentro puede crear materias estudiantes y asignarles una o varias notas desde la vista promedio.
    
    
    
    nota: hay varios detalles con el proyecto que aun no termino de acabar 
    
    
    !Muchas Gracias¡ por su tiempo de leer espero sea de su interes 
    
    
    "Si puede imaginarlo puedes programarlo"
    


