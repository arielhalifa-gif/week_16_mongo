from pymongo import MongoClient


def get_client():
    client = MongoClient('mongodb://localhost:27017')
    return client


def get_engineering_high_salary_employees():
    client = get_client()
    db = client['week-16-db']
    collection = db['employee_data_advanced']
    engineering = collection.find({'job_role.department': 'Engineering', 'salary': {'$gt': 65000}}, {'employee_id': 1, 'name': 1, 'salary': 1, '_id': 0})
    client.close()
    return engineering


def get_employees_by_age_and_role():
    client = get_client()
    db = client['week-16-db']
    collection = db['employee_data_advanced']
    by_age = collection.find({'age': {'$gte': 30, '$lte': 45}, 'job_role.department': {'$in': ['Specialist', 'Engineer']}}, {'_id': 0})
    client.close()
    return by_age


def get_top_seniority_employees_excluding_hr():
    client = get_client()
    db = client['week-16-db']
    collection = db['employee_data_advanced']
    employees_7 = collection.find({'job_role.department': {'$ne': 'HR'}}, {'_id': 0}).sort('years_at_company', -1 ).limit(7)
    client.close()
    return employees_7

def get_employees_by_age_or_seniority():
    client = get_client()
    db = client['week-16-db']
    collection = db['employee_data_advanced']
    employees = collection.find({'$or': [{'age': {'$gt':50}}, {'years_at_company': {'$lt': 3}}]},{'employee_id': 1, 'name': 1, 'age': 1, 'years_at_company': 1, '_id': 0})
    client.close()
    return employees


def get_managers_excluding_departments():
    client = get_client()
    db = client['week-16-db']
    collection = db['employee_data_advanced']
    managers = collection.find({'job_role.title': 'Manager', 'job_role.department': {'$nin':['Sales', 'Marketing']}})
    client.close()
    return managers


def get_employees_by_lastname_and_age():
    client = get_client()
    db = client['week-16-db']
    collection = db['employee_data_advanced']
    employees = collection.find({'age': {'$lt': 35}, 'name': {'$regex': {'$in': ['/.*Wright', '/.*Nelson']}}}, {'name': 1, 'age': 1, 'job_role.department': 1, '_id': 0})
    client.close()
    return employees