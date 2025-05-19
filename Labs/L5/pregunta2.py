import threading
from urllib.request import urlopen

def download(url,file_name):
	with urlopen(url) as page:
		image_data = page.read()
		with open(file_name,'wb') as f:
			f.write(image_data)

def descarga_secuencial():
	for i in range(1,30):
		url = f'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/{i:02}.png'
		file_name = f'{i:02}.png'
		download(url,file_name)

if __name__=='__main__':
	descarga_secuencial()
