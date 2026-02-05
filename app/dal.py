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
    