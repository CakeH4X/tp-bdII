import redis

places = [
    {"place": "Parque Chas", "lon": -58.479258, "lat": -34.582497},
    {"place": "UTN", "lon": -58.468606, "lat": -34.658304},
    {"place": "ITBA Madero", "lon": -58.367862, "lat": -34.602938}
]

# Conectar a Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

for place in places:
    count = len(r.georadius("bataxi", place["lon"], place["lat"], 1, unit='km'))
    print(f"Viajes a 1 km de {place['place']}: {count}")