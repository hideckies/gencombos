import fire
from os.path import exists


def gen(w1: str, w2: str, o: str):
	"""
	Custom Combos Wordlist Generator
	:param w1: Wordlist 1 - A wordlist file for the left side.
	:param w2: Wordlist 2 - A wordlist file for the right side.
	:param o:  Output File - Specify the name of the output file.
	"""

	# Check if file exists
	if not exists(w1):
		error_file_not_found(w1)
		return
	if not exists(w2):
		error_file_not_found(w2)
		return
	if exists(o):
		print("Error the Output File Already Exists: \"" + o + "\".\nPlease use the other name.")
		return

	# Read the given wordlists
	with open(w1, 'r', errors='replace') as words1:
		wordlist_1 = words1.read().splitlines()

	with open(w2, 'r', errors='replace') as words2:
		wordlist_2 = words2.read().splitlines()

	# Generate the custom combos and save it
	with open(o, 'a') as output:
		for a in wordlist_1:
			for b in wordlist_2:
				combo = a + ':' + b
				output.write(combo + "\n") 

	print("Completed! Custom combos generated successfully!\n" + "Output-> \"" + o + "\"")
	

def error_file_not_found(file_name):
	print("Error! File not found: " + "\""+ file_name + "\"")


if __name__ == '__main__':
	fire.Fire(gen)