file = open('hello.txt', 'rt')

line_list = file.readline()
for no, line in enumerate(line_list):
    print('{} {}'.format(no+1, line), end='')

file.close()