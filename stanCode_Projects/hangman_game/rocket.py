"""
File: rocket.py
Name: Johnson
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = int(input('Please ENTER the ROCKET size: '))



def main():
	'''
	The first version of this project was done in the hospital, since I took an operation on Wed,
	so the whole syntax is a bit more lousy. I have discharged from the hospital at weekend and
	I did this project again, called it 'rocket_Lite.py'.
	'''
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	for i in range(SIZE):
		for j in range(SIZE + 1):
			if i + j > SIZE - 1:
				print('/', end='')
			else:
				print(' ', end='')
		for j in range(i + 1):
			print('\\', end='')
		print('')


def belt():
	for i in range((2 * SIZE) + 2):
		if i == 0:
			print('+', end='')
		elif i == ((2 * SIZE) + 1):
			print('+', end='')
		else:
			print('=', end='')
	print('')


def upper():						# The original thought of the upper() is that / and \ scatter like
	for i in range(SIZE):			# checkerboard, so I use %2 to print it.
		print('|', end='')
		for j in range(SIZE - 1 - i):
			print('.', end='')
		for k in range(i + 1):
			if k % 2 == 1:
				print('\\', end='')
			else:
				print('/', end='')
		if i % 2 == 0:
			for m in range(i + 1):
				if m % 2 == 1:
					print('/', end='')
				else:
					print('\\', end='')
		else:
			for m in range(i + 1):
				if m % 2 == 1:
					print('\\', end='')
				else:
					print('/', end='')
		for n in range(SIZE - 1 - i):
			print('.', end='')
		print('|', end='')
		print('')


def lower():						# The original thought of the lower() is that / and \ scatter like
	for i in range(SIZE):			# checkerboard, so I use %2 to print it.
		print('|', end='')
		for j in range(i):
			print('.', end='')		# The trickiest thing is that if the rocket size is odd or even will
		for k in range(SIZE - i):	# affect the distribution of / and \, so I use another if/else to fix it.
			if k % 2 == 0:
				print('\\', end='')
			else:
				print('/', end='')
		if SIZE % 2 == 0:
			if i % 2 == 1:
				for m in range(SIZE - i):
					if m % 2 == 0:
						print('/', end='')
					else:
						print('\\', end='')
			else:
				for m in range(SIZE - i):
					if m % 2 == 0:
						print('\\', end='')
					else:
						print('/', end='')
		else:
			if i % 2 == 1:
				for m in range(SIZE - i):
					if m % 2 == 1:
						print('/', end='')
					else:
						print('\\', end='')
			else:
				for m in range(SIZE - i):
					if m % 2 == 1:
						print('\\', end='')
					else:
						print('/', end='')
		for n in range(i):
			print('.', end='')
		print('|', end='')
		print('')

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
