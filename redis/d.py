import redis

# Conectar a Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

members_count = r.zcard('bataxi')
print(f"Número de miembros en la key 'bataxi': {members_count}")