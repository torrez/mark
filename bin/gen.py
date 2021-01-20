#!/usr/bin/env python3

all_lines = []
big_string = ""

template = """
<iframe width="560" height="315" src="https://www.youtube.com/embed/XXXXXXXXXX" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
"""
with open('source.txt','r') as fh:
     all_lines = fh.readlines()

for line in all_lines:
    trash, yt_code = line.rstrip().split('=')

    embed = template.replace('XXXXXXXXXX', yt_code) 
    big_string += embed + "<br>"

with open('index.html', 'r') as fh:
    index_file = fh.read()

generated = index_file.replace('XXXXXXXXXX', big_string)
print(generated)
