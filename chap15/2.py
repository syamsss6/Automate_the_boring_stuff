import requests,os,bs4,threading

url='https://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
def downloadXkcd(start,end):
	for url in range(start,end):

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
	#prev=soup.select('a[rel="prev"]')[0]
	#url='http://xkcd.com'+prev.get('href')
thr=[]
for i in range(0,1400,100):
	t=threading.Thread(target=downloadXkcd,args=(i,i+99))
	thr.append(t)
	t.start()
for t in thr:
	t.join()
print('Done')
