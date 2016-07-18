import requests,os,bs4

url='https://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('#'):
	print('Downloading the page %s.....' % url)
	res=requests.get(url)
	res.raise_for_status()
	soup=bs4.BeautifulSoup(res.text,"lxml")
	
	elem=soup.select('#comic img')
	if elem==[]:
		print('Could not find comic image')
	else:
		try:
			comicUrl='http:'+elem[0].get('src')
			print('Dowloading image %s...' %(comicUrl))
			res=requests.get(comicUrl)
			res.raise_for_status()
		except requests.exceptions:
			#skip this comic
			prev=soup.select('a[rel="prev"]')[0]
			url='http://xkcd.com'+prev.get('href')
			continue
		imgFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
		for chunk in res.iter_content(100000):
			imgFile.write(chunk)
		imgFile.close()
	#Get the previous button's url
	prev=soup.select('a[rel="prev"]')[0]
	url='http://xkcd.com'+prev.get('href')

print('Done')
