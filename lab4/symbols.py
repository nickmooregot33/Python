#!/software/SciPy-Stack-2.7.10-x86_64/bin/python2

#function to answer question #10 of lab4 in CS 101

def symbol_to_name(symbol):
	if len(symbol) == 1:
		if 'H' in symbol:
			return 'Hydrogen'
		elif 'B' in symbol:
			return 'Boron'
		elif 'C' in symbol:
			return 'Carbon'
		elif 'N' in symbol:
			return 'Nitrogen'
		elif 'O' in symbol:
			return 'Oxygen'
		else:
			return None
	elif len(symbol) == 2:
		if 'He' in symbol:
			return 'Helium'
		elif 'Be' in symbol:
			return 'Beryllium'
		elif 'Li' in symbol:
			return 'Lithium'
		else:
			return None
	else:
		return None

#testing the testcases

#if symbol_to_name('He') == 'Helium':
#	print "True"
#if symbol_to_name('Be') <> 'Boron':
#	print "True"
#if symbol_to_name('He') <> 'Hydrogen':
#	print "True"
#if symbol_to_name('B') <> 'Beryllium':
#	print "True"
#if symbol_to_name('N') == 'Nitrogen':
#	print "True"
#if symbol_to_name('Ne') == None:
#	print "True"
