def symbol_to_name(symbol):
	if 'H' in symbol:
		if 'He' in symbol:
			return 'Helium'
		else:
			return 'Hydrogen'
	elif 'B' in symbol:
		if 'Be' in symbol:
			return 'Beryllium'
		else:
			return 'Boron'
	elif 'Li' in symbol:
		return 'Lithium'
	elif 'C' in symbol:
		return 'Carbon'
	elif 'N' in symbol:
		if 'Ne' in symbol:
			return None
		else:
			return 'Nitrogen'
	elif 'O' in symbol:
		return 'Oxygen'
	else:
		return None

go_flag = True
while go_flag:
	# ask for input symbol
	symbol_in = raw_input("Give me the symbol")
    # check input symbol for 'x'
	if (symbol_in == 'x'):
        # change go_flag to stop
		go_flag = False
	else:
        # change the symbol
		symbol_out = symbol_to_name(symbol_in)
		print "The symbol is %s." %symbol_out

