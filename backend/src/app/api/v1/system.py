from fastapi import APIRouter
from .auth import wrap_response

router = APIRouter(prefix="/system", tags=["system"])

@router.get("/menus")
def get_menus():
    return wrap_response(data=[])

@router.post("/menus")
def create_menu():
    return wrap_response(data={"message": "Menu created successfully"})

@router.put("/menus/{menu_id}")
def update_menu(menu_id: int):
    return wrap_response(data={"message": "Menu updated successfully"})

@router.delete("/menus/{menu_id}")
def delete_menu(menu_id: int):
    return wrap_response(data={"message": "Menu deleted successfully"})