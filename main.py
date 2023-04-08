from fastapi import FastAPI
import os.path



app = FastAPI()



@app.get("/items")
async def read_item():
    file_path = "./data/counter.txt"
    if os.path.exists(file_path):
        f = open(file_path, 'r')
        counter = f.readline()
        f.close()
        if counter == '':
            f = open(file_path, 'w')
            f.write('1')
            f.close()
            counter = 1
            return {"counter": counter}
        else:
            f = open(file_path, 'w')
            counter = int(counter)+1
            f.write(str(counter))
            f.close()
            return {"counter": counter}
    else:
        f = open(file_path, 'w+')
        f.close()
        return {"counter": 1}



