employees = [
    {"id": 1, "name": "Dhanushree", "role": "Senior Software Engineer"},
    {"id": 2, "name": "Lakshmeesha", "role": "Lead Associate"}
]

def getall():
    return employees

def getbyid(id: int):
    for emp in employees:
        if emp["id"] == id:
            return emp

def getrole(id: int):
    for emp in employees:
        if emp["id"] == id:
            return emp["role"]