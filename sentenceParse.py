import pdb 
from collections import Counter
import re

def total_alpha_char(result):
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
	count = 0
	for c in result:
		if c in alpha:
			count += 1
	return count

def letter_freq(result):
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	letter = Counter()
	for word in result:
		if word in letters:
			letter[word] += 1
	for c in letter:
		letter[c] = float(letter[c])
		letter[c] /= len(result)
	letter = str(letter)
	letter = letter[9:-2]
	return letter

def number_freq(result):
	numbers = "0123456789"
	number = Counter()
	for word in result:
		if word in numbers:
			number[word] +=1
	for n in number:
		number[n] = float(number[n])
		number[n] /= len(result)
	number = str(number)
	number = number[9:-2]

	if number == "":
		number = "No Numbers in Phrase"
	return number

def number_words(result):
	words = re.findall(r"[\w']+", result)
	return words

def generate_sequence(words):
	sequences = []
	garb = []
	for word in words:
		if len(word) < 3:
			garb.append(word)
		else:
			count = 0
			n = 0
			if len(word) > 3:
				count += len(word) - 2 
				first = True
				i = 3
				j = 0
				sets = []
				while(count > n):
					if first:
						wordss = word[:i]
						first = False
					else:
						wordss = word[j:i]
					n+=1
					i+=1
					j+=1
					sets.append(wordss)
				sequences.append(sets)
			else:
				sequences.append(word)
	return sequences

def start_ted_counts(words, sequences):
	count = 0 
	for seq in sequences:
		if type(seq) == list:
			if seq[0].lower() == "ted":
				count +=1
		elif seq.lower() == "ted":
			count+=1
	return int(count), float(count)/(float(len(words)))


def middle_ted_counts(words, sequences):
	count = 0 
	for seq in sequences:
		if type(seq) == list:
			temp = seq[1:-1]
			for seqs in temp:
				if seqs.lower() == "ted":
					count+=1 
	return int(count), float(count)/(float(len(words)))

def end_ted_counts(words, sequences):
	count = 0 
	for seq in sequences:
		if type(seq) == list:
			if seq[-1].lower() == "ted":
				count +=1

	return int(count), float(count)/(float(len(words)))

def total_seq_counts(words, sequences):
	count = 0
	num_seqs = 0
	for seq in sequences:
		if type(seq) == list:
			for seqs in seq:
				if seqs.lower() == "ted":
					count+=1
				if len(seq) >= 3:
					num_seqs+=1
				else:
					if len(seq) >= 3:
						num_seqs+=1
		elif seq.lower() == "ted":
			count+=1
			if len(seq) >= 3:
				num_seqs+=1
		else:
			if len(seq) >= 3: 
				num_seqs+=1
	try:
		return int(count), (float(count)/float(num_seqs)), int(num_seqs)
	except:
		print "Cannot divide by count 0, exiting..."
		exit()

def main():
	print "It is a statistical text analyzer, please enter a phrase followed by a '#'"
	result = raw_input("Please enter an input: ")
	if result == "#":
		print "No word or numbers found, exiting..."
		exit()
	index = result.find("#")
	if index != -1:
		result = result[:index]
	else:
		print "Input does not have a '#' character"
		exit()

	if result.strip() == "":
		print "Input does not have anything entered, exiting..."
		exit()

	print "Total alphanumeric characters: " + str(total_alpha_char(result))
	print "Letter Frequency: " + str(letter_freq(result))
	print "Number Frequency: " + str(number_freq(result))
	words = number_words(result)
	print "Number of Words: " + str(len(words))
	seqs = generate_sequence(words)
	start = start_ted_counts(words, seqs)
	middle = middle_ted_counts(words, seqs)
	end = end_ted_counts(words, seqs)

	change = False
	if middle[1] > 1.0:
		change_freq = 1.0
		change = True

	print "Number of words starting with 'ted': "  + str(start[0]) 
	print "Frequency of words starting with 'ted': " + str(start[1]) 
	print "Number of words with 'ted' in the middle: " + str(middle[0])
	if change:
		print "Frequency of words with 'ted' in the middle: " + str(change_freq) 
	else:
		print "Frequency of words with 'ted' in the middle: " + str(middle[1]) 

	print "Number of words with 'ted' at the end: " + str(end[0])
	print "Frequency of words ending with 'ted': " + str(end[1]) 
	
	total = total_seq_counts(words, seqs)
	print "Frequency of sequences with 'ted': " + str(total[1]) 
	print "Total number of 3 alphanumeric character sequences: " + str(total[2])
	print "Total number of 'ted' sequences: " + str(total[0])

main()