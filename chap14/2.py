import os,csv
 
for filen in os.listdir():
	if  filen.endswith('csv'):
		print('Removing header from '+filen+'...')
		fobj=open(filen,'r')
		fobj2=open('new_'+filen,'w',newline='')
		fread1=csv.reader(fobj)
		fwrite2=csv.writer(fobj2)
		flist=[]
		for i in fread1 :
			if fread1.line_num==1:
				pass
			else:
				flist.append(i)
		for row in flist:
			fwrite2.writerow(row)
				
fobj.close()
fobj2.close()
