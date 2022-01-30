from fastapi import FastAPI

app = FastAPI()


@app.post("/")
def read_root():
    dict = {"Hello" : "World"}
    return dict["Hello"]

@app.post("/")
def read_root():
    dict = {"Hello" : "World"}
    return dict["Hello"]

