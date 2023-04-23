import sys

def write_lp(variables, products, ressources, limits, productNeeds, profits, output, int_contraint):
	"""
	Take all the elements needed by a linear problem which goal is to maximize the benefits of the products
	made with ressources. And write it in an output file using the lp solver syntax.
	"""
	output.write("max: ")		# In our case it will always be a maximum of the benefits
	delim = ""
	# We write the objective function
	for i in range(products):
		output.write(delim)
		output.write(str(profits[i]) + variables[i])
		delim = "+"
	output.write(";\n")
	# We write the contraints
	for i in range(ressources):
		delim = ""
		for j in range(products):
			output.write(delim + productNeeds[j][i] + variables[j])
			delim = "+"
		output.write(" <= " + limits[i] + ";\n")
	if int_contraint:  # If there's the option -int
		output.write("int " + ','.join(variables) + ";")



def main():
	"""
	Main function of the programm. It retrieves the data of the linear programm written in the first file name
	and translate it into a file texte with the lp solver syntax.  
	"""
	# Check of the line command arguments
	if len(sys.argv) != 3 and len(sys.argv) != 4:	
		print("Illegal number of arguments!\n")
		exit(1)
	#Check of the last argument
	int_contraint = len(sys.argv) == 4 and sys.argv[3] == "-int"    # Boolean describing if there's the option -int
	reader = open(sys.argv[1], 'r')		# Reader
	output = open(sys.argv[2], 'w')		# Writter
	lines = reader.readlines()			# We read all the file and put it in a list, each line is an element.
	ressources = int(lines[0].split()[0])  # Nb of ressources
	products = int(lines[0].split()[1])    # Nb of products
	limits = lines[1].split()              # Limits of ressources
	variables = []                         # Names of variables
	productNeeds = []                      # List of ressources needed for each products
	profits = []                           # Profits earned by each products
	for i in range(2, products + 2):
		productNeeds.append(lines[i].split()[1: ressources + 1])
		variables.append(lines[i].split()[0])
		profits.append(lines[i].split()[1 + ressources])
	# Now that we have all the datas that were written in the input, we translate it in the output
	write_lp(variables, products, ressources, limits, productNeeds, profits, output, int_contraint)
	reader.close()
	output.close()

main()