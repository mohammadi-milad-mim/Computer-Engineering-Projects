import re

def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)

number_of_files = 1
for i in range(number_of_files):
    in_file_name = "files_0/f_0_{num}.txt".format(num=i+1)
    out_file_name = "files_1/f_1_{num}.txt".format(num=i+1)
    temp_file_name = "files_0/t_0_{num}.txt".format(num=i+1)
    fin = open(in_file_name, "r")
    fout = open(out_file_name, "w")
    ftemp = open(temp_file_name,"w")
    temp = ""
    define_list = {}
    #Find include, paste them on ouput file
    for line in fin.readlines():
        sline = line.split()
        if re.search("#\s*include", line):
            path = "files_0/"+sline[-1][1:-1]
            tt = open(path, "r")
            temp+=tt.read()
            temp+='\n'
            #print(temp)
        else:
            temp+=line
    ftemp.write(temp)
    ftemp.close()
    
    ftemp = open(temp_file_name,"r")
    temp = ""
    for line in ftemp.readlines():
        #print(line)
        sline = line.split()
        if re.search("#\s*define", line):
            idx=0
            for i in range(len(sline)):
                if i=="#define" or i=="define":
                    idx=i+1
            tkey = sline[idx+1]
            tvalue = ' '.join(sline[idx+2:])
            #print(tkey)
            #print(tvalue)
            define_list[tkey]=tvalue
        else:
            temp+=line
    temp = comment_remover(temp)
    print(temp)
    print(define_list)
    for key, value in define_list.items():
        print(key,value)
        temp = temp.replace(key,value)
    
    temp = comment_remover(temp)
    fout.write(temp)
    fout.close()




#The OLD Version. Fixed Bugs!




'''
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
'''
