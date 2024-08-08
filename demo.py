# 3. Write a code to Read a file and append lines to a list?

file_name = 'Q3.txt'
lines_list =['a','b ','c']

with open(file_name,'r') as file:
    for line in file:
        lines_list.append(line.strip())

print(lines_list)
