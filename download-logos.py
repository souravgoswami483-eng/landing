import urllib.request, concurrent.futures
from pathlib import Path
assets={'medica':'medica-logo1-1','reliance':'reliance','greenbrier':'greenbrier','amri':'amri-logo','sbi':'sbi-1','vedic':'vedic','hsbc':'hsbc','axis':'axis','jaypee':'jaypee','manipal':'manipal','royal-caribbean':'royal-cri','suraksha':'surakha'}
def get(pair):
 name,path=pair
 urllib.request.urlretrieve('https://www.runaxinstitute.com/wp-content/uploads/2023/12/'+path+'.webp',Path('dist/assets')/(name+'.webp'))
 print(name)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:list(ex.map(get,assets.items()))
