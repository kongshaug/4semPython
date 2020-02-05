import os
import csv
import platform
import argparse

if platform.system() == 'Windows':
    newline='\n'

parser = argparse.ArgumentParser(description="safe filenames, print lines and destroy entire cities") 

parser.add_argument('-i','--path-to-folder', type=str, required=False,help="folder with file names to copy")
parser.add_argument('-o','--output-file', type=str, required=False,help="output file target")
parser.add_argument('-f','--path-to-file', type=str, required=False,help="grabs forst line of file")
parser.add_argument('-e','--path-to-files', type=str, required=False,help="prints emails")
parser.add_argument('-m','--path-to-md', type=str, required=False,help="md file prints headers")





def all_file_names_in_folder(path_to_folder, file_name):
    with open(file_name, 'w', newline=newline) as file_object:
        output_writer = csv.writer(file_object)
        for _, _, files in os.walk(path_to_folder):
            output_writer.writerow(files)
    
                


def print_first_line(*path_to_file):
    for file in path_to_file:
        with open(file) as file_object:
            first_line = file_object.readline()
            print(first_line)
            
def print_email_line(*path_to_file):
    for file in path_to_file:
        with open(file) as file_object:
            lines = file_object.readlines()
            for line in lines:
                if("@" in line):
                    print(line.rstrip())

def print_md_line(*path_to_file):
    for file in path_to_file:
        with open(file) as file_object:
            lines = file_object.readlines()
            for line in lines:
                if("#" in line):
                    print(line.rstrip())







arguments = parser.parse_args()
if arguments.path_to_folder != None and arguments.output_file != None :
    all_file_names_in_folder(arguments.path_to_folder, arguments.output_file)
elif arguments.path_to_file != None:
    print_first_line(arguments.path_to_file)
elif arguments.path_to_files != None:
    print_email_line(arguments.path_to_files)
elif arguments.path_to_md != None:
    print_md_line(arguments.path_to_md)
    


