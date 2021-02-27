import uvicorn
from fastapi import FastAPI, UploadFile, File
import json
import tools
import mongo

app = FastAPI()


@app.get("/")
async def rootGet():
    return {"message": "Hello World"}


@app.post("/")
async def sendFioResult(file: UploadFile = File(...)):
    contents = await file.read()
    contents = tools.removePointInJsonKeys(contents)
    mongo.insertInMongo(tools.jsonfileToDic(contents))
    return True


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8080, reload=True)
