import math
import requests

# chennai lat and long
myloc = (13.10041374771677, 80.26630119140623)

def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))

def get_dist(meteor):
    return meteor.get('distance', math.inf)
if __name__ == '__main__':
    meteor_resp = requests.get('https://data.nasa.gov/resource/y77d-th95.json')

    meteor_data = meteor_resp.json()

    for meteor in meteor_data:
         if 'reclat' not in meteor or 'reclong' not in meteor: continue
         meteor['distance'] = calc_dist(float(meteor['reclat']), float(meteor['reclong']), myloc[0], myloc[1])

    meteor_data.sort(key=get_dist)

    print(meteor_data[0:10])
