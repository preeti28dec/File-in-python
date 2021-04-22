# c=open('file_lengthy.txt','x')
def file_lengthy(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
        return i + 1
print("Number of lines in the file: ",file_lengthy('file_lengthy.txt'))