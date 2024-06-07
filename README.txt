Parte 1:

Para levantar el contenedor de mongo, es necesario ejecutar el siguiente comando en la terminal:
    docker start 407f41cbe4f3

Para entrar a la shell de nuestra instancia de mongo, es necesario ejecutar el siguiente comando en la terminal:
    docker exec -it 407f41cbe4f3 mongosh

Finalmente para acceder a la base donde se encuentra la coleccion de albums, ejecutar el siguiente comando dentro de mongo:
    use musicdb

Una vez dentro, las queries y comandos delineados en la consigna se encuentran en el archivo mongo/mongo_cmds para ser ejecutados en la shell de mongo.

===============================

Parte 2:

Se encuentra en la PPT de defensa.

===============================

Parte 3:

Para levantar el contendedor de redis, es necesario ejecutar el siguiente comando en la terminal (hacer exit en caso de seguir en mongo):
    docker start e17ea57d760c

Luego, en la carpeta redis se encuentran 4 archivos de python que realizan cada uno de los puntos. Para correrlos, se debera correr el siguiente comando en la terminal:
    python redis/archivo.py

===============================