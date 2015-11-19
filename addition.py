import pdb

def read_nums():
	'''Read in numbers'''
	S_ENT1 = raw_input("Please enter number one: ")
	S_ENT2 = raw_input("Please enter number two: ")
	return S_ENT1, S_ENT2

def pad_smaller_num(S_ENT1, S_ENT2):
	'''This function adds padding to the smaller number with leading 0's to do the addition'''
	max_num = max(len(S_ENT1), len(S_ENT2))
	if max_num == len(S_ENT1):
		S_ENT2 = str(S_ENT2).zfill(len(S_ENT1))
	else:
		S_ENT1 = str(S_ENT1).zfill(len(S_ENT2))

	return S_ENT1, S_ENT2

def check_numbers(S_ENT1, S_ENT2):
	check = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if (S_ENT1 or S_ENT2) in check:
		return False
	else:
		return True

def add_nums(S_ENT1, S_ENT2):
	'''Reverse the strings and then add keeping track if 1 needs to be add to next integer'''
	i= 0
	carry = 0
	rev_S_ENT1 = S_ENT1[::-1]
	rev_S_ENT2 = S_ENT2[::-1]
	end = len(S_ENT1)
	num = []
	while (i < end):
		if (int(rev_S_ENT1[i]) + int(rev_S_ENT2[i])) > 9:
			carry = 1
			temp = (int(rev_S_ENT1[i]) + int(rev_S_ENT2[i])) - 10
			temp = str(temp)
			num.append(temp)
		else:
			if carry == 1:
				temp = (int(rev_S_ENT1[i]) + int(rev_S_ENT2[i])) + 1
			else:
				temp = (int(rev_S_ENT1[i]) + int(rev_S_ENT2[i]))
			temp = str(temp) 
			num.append(temp)
			carry = 0
		i+=1

	S_ENT3 = ""
	for v in num:
		S_ENT3+=v
	return S_ENT3[::-1]

def main():
	looping = True
	while(looping):
		S_ENT1, S_ENT2 = read_nums()
		good = check_numbers(S_ENT1, S_ENT2)
		if good:
			S_ENT1, S_ENT2 = pad_smaller_num(S_ENT1, S_ENT2)
			S_ENT3 = add_nums(S_ENT1, S_ENT2)
			print "Answer is: " + S_ENT3
			inputs = raw_input("Would you like to enter new numbers (yes/no): ")
			if inputs.lower() == "yes":
				continue 
			else:
				looping = False
		else:
			print "Unknown character in number, exiting..."
			inputs = raw_input("Would you like to try again (yes/no: ")
			if inputs.lower() == "yes":
				continue
			else:
				looping = False
	print "Exiting..."
	exit()

main()
