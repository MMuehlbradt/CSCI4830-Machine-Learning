"""

Michael Muehlbradt

mimu0324

mimu0324@colorado.edu

Week 1

"""
#grouping probabilities by previous letter
# P(_ | I) = 1

# P(a | _) = 0.5
# P(l | _) = 0.5

# P(l | a) = 0.6
# P(m | a) = 0.4

# P(_ | m) = 0.8
# P(! | m) = 0.2

# P(i | l) = 1

# P(v | i) = 0.95
# P(n | i) = 0.05

# P(e | v) = 1

# P(e | n) = 1

# P(! | e) = 1

# P(_ | !) = 0.7
# P(I | !) = 0.2
# P(! | !) = 0.1

import random

for i in range(0,10): # 10 lines
	letter = "I"
	for k in range(0,98): #have first letter 0-98 = 99 items
		probability = random.random()

		# P(_ | I) = 1
		if letter[k] == "I":
			letter = letter + "_"
			
			
		# P(a | _) = 0.5	
		elif letter[k] == "_":
			if probability < 0.5:
				letter = letter + "a"		
		# P(l | _) = 0.5		
			else:
				letter = letter + "l"


		# P(l | a) = 0.6
		elif letter[k] == "a":
			if probability < 0.6:
				letter = letter + "l"
		# P(m | a) = 0.4
			else:
				letter = letter + "m"
				
				
		# P(_ | m) = 0.8		
		elif letter[k] == "m":
			if probability < 0.8:
				letter = letter + "_"
		# P(! | m) = 0.2	
			else:
				letter = letter + "!"
				
		# P(i | l) = 1		
		elif letter[k] == "l":
			letter = letter + "i"
			
			
		# P(v | i) = 0.95
		elif letter[k] == "i":
			if probability < 0.95:
				letter = letter + "v"
		# P(n | i) = 0.05	
			else:
				letter = letter + "n"


		# P(e | v) = 1
		elif letter[k] == "v":
			letter = letter + "e"


		# P(e | n) = 1
		elif letter[k] == "n":
			letter = letter + "e"
			
			
		# P(! | e) = 1	
		elif letter[k] == "e":
			letter = letter + "!"
		# P(! | !) = 0.1	
		else:
			if probability < 0.1:
				letter = letter + "!"
		# P(I | !) = 0.2		
			elif probability < 0.2:
				letter = letter + "I"
		# P(_ | !) = 0.7		
			else:
				letter = letter + "_"
			
	print(letter)
