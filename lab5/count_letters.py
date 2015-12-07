from string import ascii_lowercase
def count_letters(text):
	for letter in ascii_lowercase:
		lettercount = text.count(letter,0,len(text))
		print 'letter: %s,%s'% (letter,lettercount)

