import logging

logging.basicConfig(filename='log.txt',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

logging.debug('Start of program')
#logging.disable(logging.CRITICAL)
def fact(n):
	logging.debug('Start of factorial(%s)'%n)

	total=1
	for i in range(1,n+1):
		total*=i
		logging.debug('i is '+str(i)+',total is '+str(total))
	logging.debug('End of factorial of %s'%n)
	return total

print(fact(5))
logging.debug('End of program')
