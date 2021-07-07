
def read_file(fpath):
    count = 0 
    BLOCK_SIZE = 500
    with open(fpath) as f: 
        while True: 
            block = f.read(BLOCK_SIZE)
#           print(len(block))
            count += len(block.split())
            if not(block): 
                return count
#            if block[len(block)-1].isalpha() or block[len(block)-1].isdigit():
#                count = count - 1

path = input('please input the path of the English document:')
Eng_document = read_file(path)
print('THis txt file have '+str(Eng_document)+'words.')
    
