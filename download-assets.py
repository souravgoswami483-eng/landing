import urllib.request, concurrent.futures
from pathlib import Path
assets={'campus':'2024/01/Campus-Bulding1.webp','front-office':'2024/01/front-office.webp','classroom':'2024/01/classroom-1.webp','housekeeping':'2024/01/housing-keeping.webp','kitchen':'2024/01/food_lab.webp','service':'2024/01/food-beverage.webp','students':'2026/03/home-about-image.webp','apollo':'2023/12/apollo.webp','swissotel':'2023/12/swissotel.webp','indigo':'2023/12/indigo-1.webp','peerless':'2023/12/peerless.webp','hospital':'2026/09/Hospital-management-course-in-Kolkata-300x200.webp'}
def get(pair):
 name,path=pair
 urllib.request.urlretrieve('https://www.runaxinstitute.com/wp-content/uploads/'+path,Path('dist/assets')/(name+'.webp'))
 print(name)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:list(ex.map(get,assets.items()))
