#A dictionary with the atoms' atomic symbols and atomic weights
weights = {"H": 1.008, "He": 4.002602, "Li": 6.94, "Be": 9.0121831, "B": 10.81,
"C": 12.011, "N": 14.007, "O": 15.999, "F": 18.998403163, "Ne": 20.1797, "Na":
22.98976928, "Mg": 24.305, "Al": 26.9815384, "Si": 28.085, "P": 30.973761998,
"S": 32.06, "Cl": 35.45, "Ar": 39.948, "K": 39.0983, "Ca": 40.078, "Sc":
44.955908, "Ti": 47.867, "V": 50.9415, "Cr": 51.9961, "Mn": 54.938043, "Fe":
55.845, "Co": 58.933194, "Ni": 58.6934, "Cu": 63.546, "Zn": 65.38, "Ga":
69.723, "Ge": 72.630, "As": 74.921595, "Se": 78.971, "Br": 79.904, "Kr": 83.798
, "Rb": 85.4678, "Sr": 87.62, "Y": 88.90584, "Zr": 91.224, "Nb": 92.90637, "Mo"
: 95.95, "Tc": 98, "Ru": 101.07, "Rh": 102.90549, "Pd": 106.42, "Ag": 107.8682,
"Cd": 112.414, "In": 114.818, "Sn": 118.710, "Sb": 121.760, "Te": 127.60, "I":
126.90447, "Xe": 131.293, "Cs": 132.90545196, "Ba": 137.327, "La": 138.90547,
"Ce": 140.116, "Pr": 140.90766, "Nd": 144.242, "Pm": 145, "Sm": 150.36, "Eu":
151.964, "Gd": 157.25, "Tb": 158.925354, "Dy": 162.500, "Ho": 164.930328, "Er":
167.259, "Tm": 168.934218, "Yb": 173.045, "Lu": 174.9668, "Hf": 178.49, "Ta":
180.94788, "W": 183.84, "Re": 186.207, "Os": 190.23, "Ir": 192.217, "Pt":
195.084, "Au": 196.966570, "Hg": 200.592, "Tl": 204.38, "Pb": 207.2, "Bi":
208.98040, "Po": 209, "At": 210, "Rn": 222, "Fr": 223, "Ra": 226, "Ac": 227,
"Th": 232.0377, "Pa": 231.03588, "U": 238.02891, "Np": 237, "Pu": 244, "Am":
243, "Cm": 247, "Bk": 247, "Cf": 251, "Es": 252, "Fm": 257, "Md": 258, "No":
259, "Lr": 266, "Rf": 267, "Db": 268, "Sg": 269, "Bh": 270, "Hs": 270, "Mt":
278, "Ds": 281, "Rg": 282, "Cn": 285, "Nh": 286, "Fl": 289, "Mc": 290, "Lv":
293, "Ts": 294, "Og": 294 }

#A function that throws an error (in case the molecule is invalid)
def error(string):
	#Print the error string
	print(string)
	#Exit the program because it can't continue with an error
	raise SystemExit

#The number of every atom type in a molecule
class AtomList:
	#A dictionary with all the atoms and the number of each one of them
	atoms = {}

	#The constructor for a new molecule
	def __init__(self):
		#Initialize the atom dictionary
		self.atoms = {}

	#Copies the molecule (instead of creating a new variable with a reference
	#to the old one)
	def copy(self):
		ret = AtomList()
		#Copy the dictionary to a new molecule and return it
		ret.atoms = dict(self.atoms)
		return ret

	#Adds atoms to the molecule
	def add_atom(self, atom, number):
		#If the atom already exists, add to the number of that atom
		if atom in self.atoms:
			self.atoms[atom] += number
		else:
			#The atom doesn't exist, create it
			self.atoms[atom] = number

	#Multiplies the number of every atom time by a scalar
	def multiply(self, scalar):
		#Loop through every atom and multiply it
		for key in self.atoms:
			self.atoms[key] *= scalar

	#Merges two lists of atoms. Useful for hydrates
	def add_list(self, lst):
		#Add every atom in the list
		for key in lst.atoms:
			#If the atom is already present in the molecule, add the number of
			#new atoms
			if key in self.atoms:
				self.atoms[key] += lst.atoms[key]
			else:
				#Else, just add the new atoms to the atom dictionary
				self.atoms[key] = lst.atoms[key]

	#A function that calculates the molecular weight of the molecule (the
	#same value as the molar mass)
	def calculate_mass(self):
		ret = 0
		#Add the weight of every atom times the number of times it's in the
		#molecule
		for key in self.atoms:
			if key in weights:
				#The atom exists, add it to the weight the number of times it's
				#in the molecule
				ret += weights[key] * self.atoms[key]
			else:
				#The atom doesn't exist, throw an error.
				error("Atom " + key + " doesn't exist")	
		#Return the weight
		return ret


#Gets the number of atoms of each element in a molecule from its chemical
#formula
def count_atoms(molecule):
	#Create the list of atoms that will be returned
	count = AtomList()

	lasti = 0
	#Loop through every atom in the chemical formula
	while lasti < len(molecule):
		i = lasti
		#Check if it's the start of an atom (upper case letter)
		if molecule[i].isupper():
			#Add the first character to the atom name
			atom = str(molecule[i])
			#If the next character is lower-case, it's still part of this atom
			if i + 1 != len(molecule) and molecule[i + 1].islower():
				#Add this character to the atom string
				atom += molecule[i + 1]
				#Advance the atom characters
				i += 2
			else:
				#Advance the atom character
				i += 1
			#Check if there is a number after the atom
			number = ""
			for j in range(i, len(molecule)):
				if molecule[j].isdigit():
					#The current character is a digit, it is still part of the
					#number after the atom. Add this character to the number
					number += molecule[j]
					if j == len(molecule) - 1:
						#This is the last digit of the chemical formula. Skip
						#to the end of the molecule because a non-digit
						#character won't be found and the number won't be
						#skipped.
						i = len(molecule)
				else:
					#A non-digit character was found. Skip to the end of the
					#number and exit the number-searching loop
					i = j
					break
			if number == "":
				#There is no number after the atom, so there's only one atom
				number = 1
			else:
				#Convert the number after the atom
				number = int(number)
			#Add the atom(s) to the list			
			count.add_atom(atom, number)
		#Check for a period after the molecule (hydrates)
		elif molecule[i] == '.':
			#Check if the period isn't the first character of the molecule
			if i == 0:
				#The period must be after the molecule. Throw an error.
				error("Hydrate period must be preceded by a molecule.")
			else:
				#The period isn't the first character. Process the contents
				#after it. First, get the number before the H2O molecules.
				number = ""
				#Advance the period character
				i += 1
				for j in range(i, len(molecule)):
					#The current character is a digit or a period, it is still
					#part of the number. Add this character to the number.
					if molecule[j].isdigit() or molecule[j] == '.':
						number += molecule[j]
						if j == len(molecule) - 1:
							#This is the last digit of the chemical formula.
							#That is invalid because a molecule is expected
							#after this.
							error("Molecule expected after hydrate number.")
					else:
						#A non-digit character was found. Skip to the end of
						#the number and exit the number-searching loop
						i = j
						break
				#Convert the number
				if number == "":
					#No number before the molecule, consider 1
					number = 1
				else:	
					number = float(number)
				#Get the molecule after the number
				hydrate = molecule[i:]
				hydrate = count_atoms(hydrate)
				#And multiply it by number times
				hydrate.multiply(number)
				#Add the atoms to the main molecule
				count.add_list(hydrate)
				#Exit the loop (the molecule was processed until the end)
				break
		#Check for parenthesis (common in ions)
		elif molecule[i] == '(':
			#Get the text until the closing parenthesis
			#Keep track of the parentheses stacks
			stack = 0
			par = ""
			for j in range(i, len(molecule)):
				#Open parentheses characters add 1 to the stack
				if molecule[j] == '(':
					stack += 1
				#Closing parenthesis remove a layer from the stack
				elif molecule[j] == ')':
					stack -= 1
				#If all the parentheses were closed, exit the loop and get the
				#string between the parentheses
				if stack == 0:
					par = molecule[i + 1 : j]
					i = j + 1
					break
			if stack != 0:
				#No closing parenthesis found. Throw an error.
				error("No closing parenthesis found.")
			#Process the molecule inside the parentheses
			par = count_atoms(par)
			#Get the number after the closing parenthesis
			number = ""
			for j in range(i, len(molecule)):
				if molecule[j].isdigit():
					#The current character is a digit, it is still part of the
					#number after the parenthesis. Add this character to the
					#number
					number += molecule[j]
					if j == len(molecule) - 1:
						#This is the last digit of the chemical formula. Skip
						#to the end of the molecule because a non-digit
						#character won't be found and the number won't be
						#skipped.
						i = len(molecule)
				else:
					#A non-digit character was found. Skip to the end of the
					#number and exit the number-searching loop
					i = j
					break
			#Convert the number
			if number == "":
				#No number, consider 1
				number = 1
			else:	
				number = int(number)
			#Make the atoms inside the parenthesis number of times
			par.multiply(number)
			#Add the content inside the parenteses to the molecule
			count.add_list(par)
		else:
			#No pattern found. Throw an error.
			error("Unexpected character '" + molecule[i] + "'");	
		lasti = i
	return count

while True:
	#Get the user input for the molecule
	molecule = input("Insert molecule: ")
	if molecule.lower() == "exit":
		#Exit the program if the user asked for it
		raise SystemExit
	#Get the number of atoms in the molecule
	atoms = count_atoms(molecule)
	#Write the molar mass to the console
	print(str(atoms.calculate_mass()) + u" g mol-1")