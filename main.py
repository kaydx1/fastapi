from fastapi import FastAPI
import os.path



app = FastAPI()

file_path = "./data/counter.txt"


def check_file_exist(path):
    
    return os.path.exists(path)

def read_file(path):
    if check_file_exist(file_path):
        f = open(path, 'r')
        counter = int(f.readline())
        f.close()
        return counter
    else:
        return 0
          
def write_to_file(path):
    counter = read_file(path)
    f = open(path, 'w')
    counter += 1
    f.write(str(counter))
    f.close()
    return counter


@app.get("/items1")
async def read():
    return read_file(file_path)

@app.post("/items2")
async def count():
    return write_to_file(file_path)




