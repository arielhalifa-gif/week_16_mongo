from fastapi import FastAPI, HTTPException
import uvicorn


app = FastAPI()


@app.get("/employees/engineering/high-salary")
def high_salary():
    pass