#IMPORTS
import os
import sys
import random as r
import numpy as np

#ERROR MESSAGES
error1 = "Unexpected error occured while opening \"data\"."
error2 = "Try to check your permissions and review your path."
error3 = "There is no data generated"

#INPUT
def get_input(s):
	try:
		i = float(input(s))
		return i
	except:
		print("Not a number")
		return 0


#---


#WRITE
def write_data():
	print("Are you sure you want to proceed?")
	write = input("This will erase all data if existent (Y/n) ")
	if(write != "n" and write != "N"):
		f = open("./data", "w")
		f.write("*** Data file ***\n")

		print("---")

		n = 0
		while(n <= 0):
			n = int(get_input("Number of lines: ")) #Obtener numero lineas

		print("---\nData generation: \n---")
		for i in range(n):
			m = r.randint(1, 10+n) #Numero elementos linea i
			for j in range(m):
				x = r.randint(1,m)
				print("{} ".format(x), end="")
				f.write(str(x) + " ")
			print("\n")
			f.write("\n")
		f.close()


#READ
def read_data():
	if os.path.exists("./data"):
		try:
			f = open("./data", "r")
			if f.readline()[:17] == "*** Data file ***":
				data = f.readlines()
				a = []

				for i in range(len(data)):
					line = np.int_(np.array(data[i].rsplit()))
					a.append(line)
			f.close()

			ordered = input("Do you want ordered contents? (Y/n) ")
			ordbool = ordered != "n" and ordered != "N"

			if ordbool:
				otext = "Ordered "
			else:
				otext = "Unordered "

			print("---\n" + otext + "contents from data file:\n")
			for i in range(len(a)):
				if ordbool:
					a[i].sort()
				for j in range(len(a[i])):
					print("{} ".format(a[i][j]), end="")
				print("\n")
			return True, a
		except:
			print(error1)
			print(error2)
			return False, 0
	else:
		print(error3)
		write = input("Do you want generate new data? (Y/n) ")
		if(write != "n" and write != "N"):
			write_data()
			return False, 0
	print("---")


#SUM
def sum_data(a):
	print("---\nSums of data\n")
	sums = []
	for i in range(len(a)):
		s = 0
		t = ""
		for j in range(len(a[i])):
			s += a[i][j]
			t += (str(a[i][j]) + "+")
		print(t[:-1], "=", s)
		sums.append(s)
# ---


#DECIDE READ OR WRITE
print("---\nWelcome to Datapy")
while(True):
	rw = input("1.Read data(r)\n2.Generate new data(w)\n3.Read and Write(rw)\n4.Read and Sum(s)\n5.Exit(e)\n-> ")
	print("---")

	if(rw == "e" or rw == "E" or rw == "5"):
		sys.exit()
	elif(rw == "r" or rw == "R" or rw == "1"):
		read_data()
	elif(rw == "w" or rw == "W" or rw == "2"):
		write_data()
	elif(rw == "s" or rw == "S" or rw == "4"):
		t = read_data()
		if t[0]:
			sum_data(t[1])
	else:
		t = read_data()
		if t[0]:
			print("---\nYou are about to generate new data")
			write_data()
