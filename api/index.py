from fastapi import FastAPI
from api.wreckcheck.index import app as wreckcheck_app

app = FastAPI()

# Mount the users app
app.mount("/api/wreckcheck", wreckcheck_app)

@app.get("/api")
def hello_world():
    return {"message": "Hello World", "api": "Python"}
