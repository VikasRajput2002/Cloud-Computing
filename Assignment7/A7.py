#!/usr/bin/python
"""mapper.py"""
import sys
# input comes from STDIN (standard input)
for line in sys.stdin:
# remove leading and trailing whitespace
    line=line.strip()
    # split the line into words
    words=line.split()
    # increase counters
    for word in words:
        print(f'{word},1')

# Table 2: Reducer Example
# write the results to STDOUT (standard output);
# what we output here will be the input for the                              


# Reduce step, i.e. the input for reducer.py
#
# comma delimited; the trivial word count is 1


# !/usr/bin/env python
"""reducer.py""" 
import sys
current_word=None 
current_count=0
word = None

#This loop will only work when the input #to the script is sorted 
for line in sys.stdin:
    #read line and split by comma
    #recall, we used comma as delimiter in mapper
    line=line.strip().split(',')
    #get the key and val, in this case #word is the key and count is the val
    word,count=line[0],int(line[1])

    if current_word==None: #initialie 
        current_word=word 
        current_count=count
    elif current_word==word: #increment the count 
        current_count+=count 
    else:
        #spit current word and
        print(f'{current_word},{current_count}') 
        current_word=word 
        current_count=count
        #spit last word
        print(f'{current_word},{count}')
