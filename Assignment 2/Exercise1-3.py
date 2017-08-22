name = input('Enter your name: ')
lname = input('Enter your last name: ')
allname = name +" " + lname
#1
print ('\n{}\n'.format(allname))
#2
ID = input('Enter your ID: ')
_ID = int(ID)
print ('your Student ID',_ID)
#3
print ('{:,}'.format(_ID))
#4
print ('\n',allname[2:4])
#VAR
cname = len(name)
clname = len(lname)
callname = len(allname)
half = int(len(allname)/2)
#
fname = allname[0:cname]
lname = allname[cname+1:callname]
halfname = allname[0:(half)]
#5
print ('\n Show first name : ',fname)
#6
print ('\n Show last name : ',lname)
#7
print ('\n Show half full name : ',halfname)
#8
print ('\n Split name w/ white space : {}'.format(allname.split(' ')))
