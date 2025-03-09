import os

#Function to print ascii art given a file that contains it
def print_ascii_art(file):

    #Get absolute file path
    current_file_path = os.path.dirname(os.path.abspath(__file__))
    new_file_path = os.path.join(current_file_path, '..', 'props', file)

    #Print
    f= open(new_file_path,'r')
    print(''.join([line for line in f]))