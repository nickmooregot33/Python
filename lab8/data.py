from types import *
import string
def s2f(string_list):
    test_string = string.ascii_lowercase + "!@#$%^&*()_+=<>?,/[]\_|"
    for row_index, row in enumerate(string_list):
        for col_index, col in enumerate(row):
            fail = 0
            #check for validity
            #is it a string
            if not type(string_list[row_index][col_index])== StringType:
                string_list[row_index][col_index] = 0.0
                continue
            string_list[row_index][col_index].strip(test_string)
            #is it a number
            if string_list[row_index][col_index] == "":
                string_list[row_index][col_index] = 0.0
            else:
                string_list[row_index][col_index] = float(string_list[row_index][col_index])

    return string_list
