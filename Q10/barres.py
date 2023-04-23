def decoupages_aux(bar_len, list, acc, result):
	"""
	Recursive function that take a total amount and make all the possible
	portions. The list of amount portions we can male are ordered by the greatest
	first and the lowest at the least.
	"""
	enough = True # we can't cut the length of remaining bar more.
	# For each amount we can cut
	for i in range(len(list)):
		if bar_len >= list[i]: # If it remains enough length
			enough = False
			new_acc = acc.copy() # We copy the values because we don't want to have this object been modified by the different recursions
			new_acc[-i - 1] += 1
			val = decoupages_aux(bar_len - list[i], list, new_acc, result)	# After added 1 unity for the portion we call this function again
			if val != None and val not in result:
				result.append(val)
	if enough:
		return acc

def decoupages_max(bar_len, list):
	"""
	Returns the all the portions solutions.
	"""
	result = [] # List of the solutions that cut the total length of bars
	other_lst = [0] * len(list) # it is the format of a single portion which is a list that take the same length of 'list' and put 0 on each case
	decoupages_aux(bar_len, sorted(list), other_lst, result)
	return result

def show_properly(tab):
	"""
	Returns a beautiful display of the solutions.
	"""
	print("-- Decoupages Max --\n\n" + '\n'.join([str(decoupage) for decoupage in tab]) + "\n\n-- End --\n\n")

def main():
	show_properly(decoupages_max(300, [120, 100, 50])) #Question 1)
	show_properly(decoupages_max(500, [200, 120, 100, 50])) # Question 2)

main()