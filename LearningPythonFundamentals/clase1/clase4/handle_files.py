try:
    path= 'C:\\DataFiles\\archivo.txt'
    new_file = open(path,'r')
    #data = new_file.readlines()
    #print(data)
    one_line = new_file.readline()
    one_line = new_file.readline()
    print(one_line)
    print(one_line)

    #for line in data:
        #print(line)
    #new_file = open('C:\\DataFiles\\archivo.txt', 'w')
    #new_file.write("Hello World\n")
    #new_file.write("Hola Mundo\n")
    #new_file.write("Hola UTVT\n")
    #new_file.close()
except Exception as e:
    print(e)