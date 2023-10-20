# common_directories

La idea del script es que en algunos momentos cuanto estamos en la etapa de enumeracion en un pentest no sabemos que rutas o directorios comunes maneja X tecnologia wordpress, apache, php, etc... por lo que este script esta bien para mostrarnos que directorios maneja la tecnologia que estamos buscando, en el momento el script cuenta con directorios limitados pero esto se ira alimentando, asi que por favor este atento a las actualizaciones.

Con la opcion -o el script le permite guardar por ejemplo la lista de directorios comunes de wordpress en un .txt (ej) -o wp.txt


## Ejemplo de usu

![image](https://github.com/Anonimo501/common_directories/assets/67207446/595e8c38-90e2-4717-b1cb-5e1067e7df9a)

![image](https://github.com/Anonimo501/common_directories/assets/67207446/b1835c38-e617-405a-9e33-12b6c607c27c)

![image](https://github.com/Anonimo501/common_directories/assets/67207446/92590945-9d64-4787-b475-5fde86e51d56)


## descarga y uso

git clone https://github.com/Anonimo501/common_directories.git

cd common_directories

python3 directorios.py

python3 directorios.py wordpress

python3 directorios.py wordpress -o wp.txt
