# file_1=open('people1-exercise.txt')
# print(file_1.read())
# file_1.close
# file_1=open('people1-exercise.txt','w')
# file_1.write("Pug\r\nJack Russell Terrier\r\nEnglish Springer Spaniel\r\nGerman Shepherd\r\nStaffordshire Bull Terrier\r\nCavalier King Charles Spaniel\r\nGolden Retriever\r\nWest Highland White Terrier\r\nBoxer\r\nBorder Terrier\r\n ")
# file_1.close()
# file_1=open('people1-exercise.txt')
# print(file_1.read())
# file_1.close
LIST=["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
file_1=open('peoplel-exerise.txt','w')
i=0
while i<len(LIST):
    file_1.write(LIST[i])
    file_1.write("\n")
    i+=1
file_1.close()
    
# file_4=open('delhi.txt','r')
# file_4.read()
# file_4.close
