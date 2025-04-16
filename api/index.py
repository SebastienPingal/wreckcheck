from fastapi import FastAPI
from api.test.index import app as test_app

app = FastAPI()

# Mount the users app
app.mount("/api/test", test_app)

@app.get("/api")
def hello_world():
    return {"message": "Hello World", "api": "Python"}
