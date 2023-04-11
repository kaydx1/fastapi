import os.path

file_path = "./data/counter.txt"

def check_file_exist(path):
    
    return os.path.exists(path)

def get_counter() -> int:
    if check_file_exist(file_path):
        f = open(file_path, 'r')
        counter = int(f.readline())
        f.close()
        return counter
    else:
        return 0
          
def increase_counter() -> int:
    counter = get_counter()
    f = open(file_path, 'w')
    counter += 1
    f.write(str(counter))
    f.close()
    return counter