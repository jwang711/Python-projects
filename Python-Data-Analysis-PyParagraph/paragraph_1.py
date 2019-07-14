import os
import csv
import re

input_file = 'paragraph_1.txt'
output_file = 'paragraph_1_analysis.txt'
pyparagraph_input_path = os.path.join( '.','raw_data', input_file)
pyparagraph_output_path = os.path.join( '.',output_file)

# print(os.getcwd())

num_sentence=0
num_word=0
num_chars=0
with open(pyparagraph_input_path, 'r') as paragraph_1:
    for line in paragraph_1:

#find out Approximate word count
        words = line.split()
        num_word=num_word+len(words)
#find out Approximate sentence count
        num_sentence = line.count(".")
#Approximate Approximate letter count (per word)
        num_chars=num_chars+len(line)
        letter_count = num_chars / num_word
#Average sentence length (in words)
        sentence_length = num_word / num_sentence


#Print results
    print("Paragraph Analysis")
    print("------------------------------")
    print("Approximate Word Count:" + str(num_word))
    print("Approximate Sentence Count:" + str(num_sentence))
    print("Average Letter Count:" + str(round(letter_count,1)))
    print("Average Sentence Length:" + str(round(sentence_length, 2)))


#output
with open(pyparagraph_output_path, 'w') as paragraph_1_analysis:

    paragraph_1_analysis.write("Paragraph Analysis" + "\n")
    paragraph_1_analysis.write("---------------------------\n")
    paragraph_1_analysis.write("Approximate Word Count:" + str(num_word) + "\n")
    paragraph_1_analysis.write("Approximate Sentence Count:" + str(num_sentence) + "\n")
    paragraph_1_analysis.write("Average Letter Count:" + str(round(letter_count,1)) + "\n")
    paragraph_1_analysis.write("Average Sentence Length:" + str(round(sentence_length,2)) + "\n") 
    




    

