from fastapi import FastAPI, Query, Path, HTTPException

app = FastAPI()

employee = [
    {"id": 1, "name": "Dhanushree", "role": "Senior Software Engineer"},
    {"id": 2, "name": "Lakshmeesha", "role": "Lead Associate"}
]

"""Health Check API"""
@app.get("/health")
def health_check():
    return { "status": "ok" }

"""Query params"""
@app.get("/welcome")
def welcome_greet(name : str = Query(default= "dear", min_length= 3, max_length = 50)):
    return { "greet": f"Welcome {name}"}

"""Path Params"""
@app.get("/get-role/{employee_id}")
def get_role(employee_id: int = Path(...,ge=1)):
    for emp in employee:
        if emp["id"] == employee_id:
            role = emp["role"]
            return { "role": role}
    raise HTTPException(status_code = 404, detail = "Employee not found")