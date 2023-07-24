#!/usr/bin/python3
####################
################
### n3wadm1n #####
### Euribot  #####
#####################

import os, readline
from urllib.parse import urlparse

readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")

root_directory = input("\nEnter the root directory where you want to create the directory POCs_Clickjacking: ")

if not os.path.exists(root_directory):
    print("\nRoot directory not found..")
    exit()

output_directory = os.path.join(root_directory, "POCs_Clickjacking")
if not os.path.exists(output_directory):
    os.mkdir(output_directory)

input_file = input("\nPlease enter the name of the file with the URLs: ")

if not os.path.isfile(input_file):
    print("\nInput file not found.")
    exit()

with open(input_file, "r") as file:
    urls = file.readlines()

for url in urls:
    url = url.strip()
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    domain = domain.replace(".", "_") 
    output_file = os.path.join(output_directory, f"poc_{domain}.html")
    with open("clickjacking_poc_template.html", "r") as template_file:
        poc_content = template_file.read().replace("URL_HERE", url)
    with open(output_file, "w") as output:
        output.write(poc_content)

print(f"\nPoCs successfully created in the directory '{output_directory}'!")
