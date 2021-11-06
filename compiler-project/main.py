# 1

my_file = open("preprocessed.txt", "w")
file = open("input.cpp", "r")

while True:

    # Get next line from file
    line = file.readline()
    my_file.write(line)

    # if line is empty
    # end of file is reached
    if not line:
        break

file.close()
my_file = open("preprocessed.txt", "r")

# ----- delete includes -----

while True:
    my_file_line = my_file.readline()
    line = my_file_line.split()
    for i in range(len(line)):
        if line[i] == '#' and line[i+1] == 'include':
            var = line[i: len(line) + 1] == ''
    listToStr = ''.join([str(elem) for elem in line])
    my_file.writelines(listToStr)

    if not line:
        break

# ----- delete multi line & single line comments -----

while True:
    my_file_line = my_file.readline()
    line = my_file_line.split()
    for i in range(len(line)):
        if line[i] == '/*' or line[i] == '//':
            var = line[i: len(line) + 1] == ''
        if line[i] == '*/':
            var = line[0: i + 1] == ''
    istToStr = ''.join([str(elem) for elem in line])
    my_file.writelines(listToStr)

    if not line:
        break
  
# ----- defines -----
while True:
    list_of_defines = []
    my_file_line = my_file.readline()
    line = my_file_line.split()
    for i in range(len(line)):
        if line[i] == '#' and line[i+1] == 'define':
            list_of_defines.append([line[i+2],line[i+3)
                                                   
     
# ----- undefs -----




# ----- typedefs -----
