from fastapi import FastAPI

app1 = FastAPI()

numbers = []

@app1.get("/")
async def showMessage():
    return {"response": "this is the root. Nothing else."}

@app1.post("/numbers")
async def getnumber(new):
    if new.isdigit() == True:
        numbers.append(int(new))
        return {"result": "OK"}
    else:
        return {"result": "Error"}

@app1.get("/numbers/average")
async def average():
    avg = 0
    if len(numbers) > 0:
        for i in numbers:
            avg = avg + i
        avg = avg/(len(numbers))
        return {"result ": avg}
    else:
        return {"No numbers in the array"}

@app1.get("/numbers/sum")
async def sum():
    s = 0
    if len(numbers) > 0:
        for i in numbers:
            s = s + i
        return {"result ": s}
    else:
        return {"No numbers in the array"}
        
 @app.get("/numbers/stddev")
async def getStdev():
    if (numbers == []):
        return {"result": "No numbers in the array"}
    else:
        stddev = statistics.stdev(numbers)
        return {"result": stddev }      

