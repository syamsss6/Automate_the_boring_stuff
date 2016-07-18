import time


print('Press ENTER to begin.Then press ENTER to "click" the stopwatchPress Ctrl-C to quit.')
input()
print('Started')
start=time.time()
lasttime=start
lapNum=1
try:
	while 1:
		input()
		lapTime=round(time.time()-lasttime,2)
		total=round(time.time()-start,2)
		print('Lap #%s:%s (%s)' %(lapNum,str(total).rjust(5),str(lapTime).rjust(5)))
		lapNum+=1
		lasttime=time.time()
except KeyboardInterrupt:
	#Handling Ctrl-C exception
	print('\nDone')
