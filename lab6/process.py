################################################################################
#
# Function definitions
# In this section, you will write the functions used in the main script below.
# You will solve questions 1 and 9 here.
#
################################################################################
def process(filename):  # Q1
	# Create a blank list called `entries`
	pass
	# and an empty string called `current_style`.
	pass
	
	# Open the file `filename` for reading.
	with open(filename, 'r') as dataFile:
		# Loop through each line of the file:
		for line in dataFile:
			# Strip the whitespace off of the ends of the line.
			pass
			
			# If the line is blank, `continue` execution.
			if thisLine == '':
				pass # what should you do with a blank line?
				
			# If a line starts with `#`, it represents the musical style of the next set of records.
			elif thisLine[0] == '#':
				pass # what should you do if starting a new style?
				
			# Otherwise, a line contains a blues performer.
			else:
			    pass # what should you do if you have a record?
			    # add it to entries in the format
			    #   (surname, first_name, current_style)
			    pass
	
	return entries


def uniqify(input_list):
    keys = {}
    for e in input_list:
        keys[e] = 1
    return keys.keys()


def generate_url(artistTuple):  # Q9
	# Extract the first name and surname from `artistTuple`.
	
	# Replace any spaces in the first name with underscores `_`.
	
	# Use string formatting to generate a Wikipedia URL.
	
	# Return the URL.
    pass


#################################################################################
# Script entry point
# In this section, you will write code to solve questions 2 through 9.
#
################################################################################

# Load the file `blues.txt` using the function `process` into a list `blues`.
pass


################################################################################
#
# Sort the musicians by their first names, to answer Q2 and Q3
#
################################################################################

# Import the `itemgetter` function.
pass
# Sort by first name (second field).
pass

# Print the results for Q2, Q3.
pass


################################################################################
#
# Identify which surname is most common, to answer Q4
#
################################################################################

# Add all surnames to another list.
pass

# Make a list of the unique surnames.
pass

# Count the times each surname occurs.
pass

# Sort the list of unique surnames by occurrence.
pass

# Print the results for Q4.
pass


################################################################################
#
# Identify how common blues styles are by number of performers, to answer Q5
#
################################################################################

# Add all styles to another list.
pass

# Make a list of the unique styles.
pass

# Count the times each style occurs.
pass

# Sort the list of unique styles by occurrence.
pass

# Print the results for Q5.
pass


################################################################################
#
# Identify which first name elements are most common, to answer Q6
#
################################################################################

# Add all first name elements to a list.
pass

# Tokenize the names and add the components to a master list.
pass

# Uniqify that list and create a list of the count of each name component.
pass

# Print the most common name component (of the first name).
pass


#############################################
#
# Answer Q7 and Q8 (no coding required).
#
#############################################

#############################################
#
# Example call to generate_url
#
#############################################

#print generate_url(blues[100])
