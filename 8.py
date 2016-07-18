bdy = {'alice' : 'apr1','bob':'dec12','cal':'feb20'}
while True:
	print ('enter name:(blank to quit)')
	name = input()
	if name == '':
	 break
	if name in bdy:
	 print (bdy[name]+'is birthday of'+name)
	else:
 	 print ('I do not have birthday information for ' + name)
	 print ('What is their birthday')
	 bday = input()
	 bdy[name] = bday
	 print ('Birthday database updated.')
