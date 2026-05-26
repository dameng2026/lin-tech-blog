from fastapi import APIRouter
from .auth import wrap_response

router = APIRouter(prefix="/roles", tags=["roles"])

@router.get("/")
def list_roles():
    return wrap_response(data={
        "roles": [],
        "total": 0,
        "page": 1,
        "size": 20
    })

@router.post("/")
def create_role():
    return wrap_response(data={"message": "Role created successfully"})

@router.put("/{role_id}")
def update_role(role_id: int):
    return wrap_response(data={"message": "Role updated successfully"})

@router.delete("/{role_id}")
def delete_role(role_id: int):
    return wrap_response(data={"message": "Role deleted successfully"})