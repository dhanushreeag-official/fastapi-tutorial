from fastapi import HTTPException
from app.services import employee_service

def getall_employees():
    return employee_service.getall_employees()