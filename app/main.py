from fastapi import FastAPI, HTTPException
import dal
import uvicorn


app = FastAPI()


@app.get("/employees/engineering/high-salary")
def high_salary():
    result = dal.get_engineering_high_salary_employees()
    return result  

@app.get("/employees/by-age-and-role")
def by_age_and_role():
    result = dal.get_employees_by_age_and_role()
    return result

@app.get("/employees/top-seniority")
def top_seniority():
    result = dal.get_top_seniority_employees_excluding_hr()
    return result


@app.get("/employees/age-or-seniority")
def age_or_seniority():
    result = dal.get_employees_by_age_or_seniority()
    return result



@app.get("/employees/managers/excluding-departments")
def excluding_departments():
    result = dal.get_managers_excluding_departments()
    return result


@app.get("/employees/by-lastname-and-age")
def by_lastname_and_age():
    result = dal.get_employees_by_lastname_and_age()
    return result