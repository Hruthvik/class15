from fastapi import FastAPI

app1 = FastAPI()

numbers = [0]

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
    if len(numbers) > 1:
        for i in numbers:
            avg = avg + i
        avg = avg/(len(numbers)-1)
        return {"result ": avg}
    else:
        return {"No numbers in the array"}

@app1.get("/numbers/sum")
async def sum():
    s = 0
    if len(numbers) > 1:
        for i in numbers:
            s = s + i
        return {"result ": s}
    else:
        return {"No numbers in the array"}
