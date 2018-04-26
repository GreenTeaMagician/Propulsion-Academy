
from quark import *

upQ = Quark('Up')
downQ = Quark('Down')

quarkArray = []
quarkArray.append(upQ)
quarkArray.append(upQ)
quarkArray.append(downQ)
print(str(upQ))
print(str(i) for i in quarkArray)
#proton
pqtypeList = ['Up', 'Up', 'Down']
pchargeList = [0.666, 0.666, -0.333]
plquarkList = [upQ, upQ, downQ]

proton = Nucleon(pqtypeList, pchargeList, plquarkList)

#neutron
qtypeList = ['Up', 'Up', 'Down']
chargeList = [0.666, -0.333, -0.333]
lquarkList = [upQ, downQ, downQ]
#print(str(i) for i in lquarkList)
neutron = Nucleon(qtypeList, chargeList, lquarkList)


#for i in proton:
#	print(i)
#print(str(i) for i in proton.whatisit())

print([i for i in lquarkList])
print(proton.whatisit())
print('----------')
hydrogenNucleonsList = [proton]
HeliumNucleonsList = [proton, proton, neutron, neutron]
Coordinates3DHe = [1.42, 2.87, 4.19]
chargeHe = 2

Helium = Atom("Helium", 2, 4, Coordinates3DHe, 2)
#Testing symbol-function in classes:
print('symbol methods')
print()
print(upQ.symbolq())
print(proton.symboln())
print(Helium.symbola())

#testing __str__ in classes
print('__str__ methods')
print()
print(upQ.__str__())
print(proton.__str__())
print(Helium.__str__())

#testing __iter__ in classes:
print()
#print(upQ.__iter__) #does not exist
#print(i.__str__() for i in proton)
'''
for i in proton:
	print(i)
for i in Helium:
	print(i)


#Things that need output:
print("__str__ of Atom:")
print(HeliumNucleus.__str__)
print("__iter__ of Atom")
print(i for i in HeliumNucleus)
'''
print('__iter functions, nucleon, atom')
#print(upQ.__str__()) No Applicable
print(proton.__iter__())
print(Helium.__iter__())


print("HERE WE GOOOOOOOOOOOOOOOOOOOOOOOO")

osmium = Atom('Osium', 76, 190, [1,1,1], 76)
