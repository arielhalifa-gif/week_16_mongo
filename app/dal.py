import connection as conn

def get_engineering_high_salary_employees():
    client = conn.get_client()
    db = client['week-16-db']
    collection = db['employee_data_advanced']
    lst = []
    engineering = collection.find({'job_role.department': 'Engineering', 'salary': {'$gt': 65000}}, {'employee_id': 1, 'name': 1, 'salary': 1, '_id': 0})
    for e in engineering:
        lst.append(e)
    client.close()
    return lst


def get_employees_by_age_and_role():
    client = conn.get_client()
    db = client['week-16-db']
    collection = db['employee_data_advanced']
    lst = []
    by_age = collection.find({'age': {'$gte': 30, '$lte': 45}, 'job_role.department': {'$in': ['Specialist', 'Engineer']}}, {'_id': 0})
    for b in by_age:
        lst.append(b)
    client.close()
    return lst


def get_top_seniority_employees_excluding_hr():
    client = conn.get_client()
    db = client['week-16-db']
    collection = db['employee_data_advanced']
    lst = []
    employees_7 = collection.find({'job_role.department': {'$ne': 'HR'}}, {'_id': 0}).sort('years_at_company', -1 ).limit(7)
    for e in employees_7:
        lst.append(e)
    client.close()
    return e

def get_employees_by_age_or_seniority():
    client = conn.get_client()
    db = client['week-16-db']
    collection = db['employee_data_advanced']
    lst = []
    employees = collection.find({'$or': [{'age': {'$gt':50}}, {'years_at_company': {'$lt': 3}}]},{'employee_id': 1, 'name': 1, 'age': 1, 'years_at_company': 1, '_id': 0})
    for e in employees:
        lst.append(e)
    client.close()
    return lst


def get_managers_excluding_departments():
    client = conn.get_client()
    db = client['week-16-db']
    collection = db['employee_data_advanced']
    lst = []
    managers = collection.find({'job_role.title': 'Manager', 'job_role.department': {'$nin':['Sales', 'Marketing']}})
    for m in managers:
        lst.append(m)
    client.close()
    return m


def get_employees_by_lastname_and_age():
    client = conn.get_client()
    db = client['week-16-db']
    collection = db['employee_data_advanced']
    lst = []
    employees = collection.find({'age': {'$lt': 35}, 'name': {'$regex': {'$in': ['/.*Wright', '/.*Nelson']}}}, {'name': 1, 'age': 1, 'job_role.department': 1, '_id': 0})
    for e in employees:
        lst.append(e)
    client.close()
    return e