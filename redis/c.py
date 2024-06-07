import redis

# Conectar a Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

keys_count = len(r.keys('*'))
print(f"Cantidad de KEYS en la base de datos Redis: {keys_count}")