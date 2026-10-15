from fastapi import APIRouter
from app.controllers import employee_controller

router = APIRouter(prefix = "/api/v1/employee")

@router.get("/")
def employees_list():
    return employee_controller.getall_employees()