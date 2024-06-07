import csv
import redis

# Conectar a Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Leer el archivo CSV y agregar los datos a Redis
with open('bataxi.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        r.geoadd("bataxi", (row[5], row[6], row[0]))

print("Datos importados a Redis")