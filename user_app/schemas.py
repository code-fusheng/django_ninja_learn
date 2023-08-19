from datetime import date
from ninja import Schema

class EmployeeCreate(Schema):
    first_name: str
    last_name: str
    department: int = None
    birthdate: date = None