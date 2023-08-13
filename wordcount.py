'''
Author: Nagendran Sandraprakasam 
Description: Script to produce word counts given a source of input
'''

import time
import configparser
import os

# Record "Start Time"
code_start_time = time.time()

# Read the configuration from the [wordcount.cfg] file
config = configparser.ConfigParser()
config.read('wordcount.cfg')

#Get the configuration values from the config file
data_directory   = config.get('DEFAULT', 'data_directory')
file_name        = config.get('DEFAULT', 'filename_02')
input_file       = os.path.join(os.getcwd(), data_directory, file_name)

# Function to retrieve file contents to string
def get_file_contents(file_name):
    with open(file_name, 'r') as file:
        file_contents = file.read()

    result = file_contents
    return result  

# Function to sanitize the string to remove noise chars 
def sanitize_input_value(input_value):
    delimeters = [".", ",", "?", "!"]
    for delimeters in delimeters:
        input_value = input_value.replace(delimeters, " ")
        result = input_value.casefold() #convert the string value to lowercase

    return result

# Get the file contents and send to variable
input_value = get_file_contents(input_file)

# Output Dictionary Contents
sanitized_input = sanitize_input_value(input_value)

# Spit the sentence into a list of words
words = sanitized_input.split()

# Create Dictionary with a each unique words and value defaulted to "0"
word_dictionary = {}
word_dictionary = {}.fromkeys(words,0)

#Update Dictionary with the Word Count
for word in words:
    if word in word_dictionary:
        word_dictionary[word] += 1

# Output the Dictonary contents
for key in word_dictionary:
    print(key + ":", word_dictionary[key])

# Record "End Time"
code_end_time = time.time()

# Calculate duration of code execution
elapsed_time = code_end_time - code_start_time

print("Complete processing")
print("Data File: ", input_file)
print(f"Code Execution Time: {elapsed_time:.6f} seconds")
