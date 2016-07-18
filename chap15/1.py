import time,subprocess
timeLeft=5
while timeLeft>0:
	print(timeLeft)
	time.sleep(1)
	timeLeft-=1

subprocess.Popen(['see','1.mp3'])
