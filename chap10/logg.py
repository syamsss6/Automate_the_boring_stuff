import random,logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
guess=''
dic={0:'tails',1:'heads'}
logging.debug('Start of program')
#while guess not in ('heads','tails'):
print('Guess the coin toss!Enter heads or tails')
logging.debug('Value of guess is '+guess)
guess=input()
toss=random.randint(0,1) #0 is tails
logging.debug('Value of  toss is %s and guess is %s'% (toss,guess))
if dic[toss] == guess:
	print('You got it')
else:
	print('Nope!Guess again')
	guess=input()
	logging.debug('Value of next guess is '+guess)
if dic[toss]==guess:
	print('You got it!')
else:
	print('Nope.You are really bad at this game')
logging.debug('End of program')

