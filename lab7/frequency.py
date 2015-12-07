################################################################################
#
# Function definitions
# In this section, you will write the functions used in the main script below.
# You will solve questions 2 through 5 here.
#
################################################################################


# convert a percentage string ('54.32%') into a floating-point value (0.5432)
def p2f(value):
    tmp = value[0:-1]
    decimal=float(tmp)
    return decimal/100.0
    


# load the frequency file for a given language
def loadFreq(language):
    letters = {}
    with open('lang/%s'%language, 'r') as langfile:
        # Split each line at the comma and add the second part (value)
        # to the dictionary with the first part (letter) as key.
        
        data=langfile.read().splitlines()
        for i in data:
            tmp=i.split(",")
            key=tmp[0].strip()
            value=p2f(tmp[1].strip())
            letters[key] = value

        # Make sure to strip off whitespace as well as to convert the
        # value to a float first.
    return letters


def loadLanguages():
    # load the list of files in the directory 'lang'
    from os import listdir
    languageNames=listdir('lang')

    
    L = {}
    for language in languageNames:
        frequency_distribution=loadFreq(language)
        L[language]=frequency_distribution
    # Loop over languageNames and 1) create a dictionary using `loadFreq`
    # and 2) add this dictionary to `L` with the language as the key.
    return L


def calcFreq(text):

    # get the letters of the alphabet as an uppercase string
    from string import ascii_uppercase as alphabet
    text=text.upper()
    
    from string import whitespace,punctuation
    for character in whitespace+punctuation:
        text=text.replace(character,'')

    letterFreq = {}

    # count the number of times each letter occurs in text
    for i in alphabet:
        count = 0
        for j in text:
            if j == i:
                count+=1
        letterFreq[i]= float(count)/float(len(text))
    
    # normalize the frequencies
    return letterFreq


def calcMatch(L_text, L_ref):
    L_diff = {}
    L_text2= {}
    L_ref2={}
    ##make sure we have all the letters in both lists
    for i in L_ref:
        if i not in L_text:
            L_text2[i] = 0.0
        else:
            L_text2[i] = L_text[i]

    for j in L_text:
        if j not in L_ref:
            L_ref2[j] = 0.0
        else:
            L_ref2[j] = L_ref[j]

    # loop over L_text and L_ref by key and store the absolute difference
    # in L_diff
    for i in L_ref:
        L_diff[i] = L_text2[i] - L_ref2[i]
        if L_diff[i] < 0:
            L_diff[i] = -(L_diff[i])

    
    # then add up the total of all of the differences and return that as f
    L_sum = 0
    for i in L_diff:
        L_sum+=L_diff[i]

    return L_sum

#################################################################################
# Script entry point
# In this section, you may write code to solve questions 6 through 15.
#
################################################################################

