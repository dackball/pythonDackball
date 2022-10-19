file = open('hello.txt', 'rt')

line_list = file.readline()
for line in line_list:
    print(line, end='')

file.close()