import sys
import os

def remove_null(filename):
	"""
	Remove all the null values of the products to make.
	"""
	reader = open(filename, 'r')
	lines = reader.readlines()
	print("opt = " + lines[1].split()[-1])
	for line in lines[4:]:
		split = line.split()
		if split[-1] == '0':
			continue
		print(split[0] + " = " + split[-1]) 


def decoupages_aux(long_barre, liste, acc, result):
	enough = True
	for i in range(len(liste)):
		if long_barre >= liste[i]:
			enough = False
			new_acc = acc.copy()
			new_acc[-i - 1] += 1
			val = decoupages_aux(long_barre - liste[i], liste, new_acc, result)
			if val != None and val not in result:
				result.append(val)
	if enough:
		return acc

def decoupages_max(long_barres, liste):
	result = []
	other_lst = [0] * len(liste)
	decoupages_aux(long_barres, sorted(liste), other_lst, result)
	return result

def show_properly(tab):
	print("-- Decoupages Max --\n\n" + '\n'.join([str(decoupage) for decoupage in tab]) + "\n\n-- End --\n\n")

def write_lp(length, list_len, list_req, max_cuts, output):
	# --- Optimizer ---
	output.write("min: ")
	delim = ""
	for i in range(len(max_cuts)):
		output.write(delim + "x" + str(i))
		delim = " + "
	output.write(";\n")
	# --- Constraints ---
	for i in range(len(list_req)):
		delim = ""
		for j in range(len(max_cuts)):
			if (max_cuts[j][i] != 0):
				output.write(delim)
				if (max_cuts[j][i] > 1):
					output.write(str(max_cuts[j][i]) + " ")
				output.write("x" + str(j))
				delim = " + "
		output.write(" >= " + str(list_req[i]) + ";\n")
	# --- Integrality ---
	output.write("int ")
	delim = ""
	for i in range(len(max_cuts)):
		output.write(delim + "x" + str(i))
		delim = ", "
	output.write(";")



def main():
	if len(sys.argv) != 5:
		print("Illegal number of arguments!\n")
		exit(1)

	#Converting the arguments that are of type str to int and int[]
	length = int(sys.argv[1])

	#If the list is written between []
	if sys.argv[2][0] == "[" and sys.argv[2][-1] == "]":
		list_len = sys.argv[2][1: -1]
	#If it's written with number separated with comas
	else:
		list_len = sys.argv[2]

	if sys.argv[3][0] == "[" and sys.argv[3][-1] == "]":
		list_req = sys.argv[3][1: -1]
	else:
		list_req = sys.argv[3]

	output = open(sys.argv[4], 'w')

	list_len = [int(i) for i in list_len.split(",")]
	list_req = [int(i) for i in list_req.split(",")]
	
	max_cuts = decoupages_max(length, list_len)
	write_lp(length, list_len, list_req, max_cuts, output)

	output.close()

	os.system("lp_solve " + sys.argv[4] + " > " + "out.txt")

	remove_null("out.txt")
	


main()