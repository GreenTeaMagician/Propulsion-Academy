
class Quark:
	
	def __init__(self, qtype):
		self.quarks = ['up', 'down']
		self.qtype = qtype
		if self.qtype.lower() not in self.quarks:
			raise TypeError("Error: Object not in possible quarks! Possible quarks: " + str(self.quarks))
		if self.qtype == 'Up':
			self.charge = 2/3
		else:
			self.charge = -1/3
	
	def __str__(self):
		return f"Type: {self.qtype}, Charge: {self.charge}"
		
	def symbolq(self):
		return self.qtype[0]
		
	def charge(self):
		return self.charge
		

class Nucleon:
	
	def __init__(self, ntype, chargeList, lquarkList):
		self.ntype = ntype
		self.charge = sum(chargeList)
		self.lquarkList = lquarkList
		
		self.upQ = Quark('Up')
		self.downQ = Quark('Down')
		
		self.nucleonArray = []
		if self.charge == 1:
			self.nucleonArray.append(self.upQ)
			self.nucleonArray.append(self.upQ)
			self.nucleonArray.append(self.downQ)
		else:
			self.nucleonArray.append(self.upQ)
			self.nucleonArray.append(self.downQ)
			self.nucleonArray.append(self.downQ)
	def __iter__(self):
		for qtype in self.lquarkList:
			yield qtype.symbolq()
	
	def __str__(self):
		return self.ntype
	
	def whatisit(self):
		if self.ntype == ['Up', 'Down', 'Down']:
			return 'neutron'
		else:
			return 'proton'
		#return self.ntype
		#return [i.symbolq() for i in self.lquarkList]
	
	def symboln(self):
		return "".join(i[0] for i in self.ntype)
		
		
class Atom:
	
	def __init__(self, name, atomicNumber, atomicMass, Coordinates3D, charge):
		self.name = name
		self.atomicNumber = atomicNumber
		self.atomicMass = atomicMass
		self.Coordinates3D = Coordinates3D
		self.charge = charge
		
		self.upQ = Quark('Up')
		self.downQ = Quark('Down')
		#neutron
		self.nqtypeList = ['Up', 'Down', 'Down']
		self.nchargeList = [0.666, -0.333, -0.333]
		self.nlquarkList = [self.upQ, self.downQ, self.downQ]
		#print(str(i) for i in lquarkList)
		self.neutron = Nucleon(self.nqtypeList, self.nchargeList, self.nlquarkList)

		#proton
		self.pqtypeList = ['Up', 'Up', 'Down']
		self.pchargeList = [0.666, 0.666, -0.333]
		self.plquarkList = [self.upQ, self.downQ, self.downQ]
		self.proton = Nucleon(self.pqtypeList, self.pchargeList, self.plquarkList)
		
		self.nucleonArray = []
		self.numNeutrons = self.atomicMass - self.atomicNumber
		for i in range(0, self.numNeutrons):
			self.nucleonArray.append(self.neutron)
		for i in range(0, self.atomicMass):
			self.nucleonArray.append(self.proton)
		print([i.whatisit() for i in self.nucleonArray])
		print('self.nucleonarray above')
		
	def __str__(self):
		return self.name
		
	def symbola(self):
		return f"[{self.atomicNumber},{self.atomicMass}]"

	def __iter__(self):
		for book in self.books:
			yield str(book)
			
'''

def __iter__(self):
	for book in self.books:
		yield str(book)
'''
