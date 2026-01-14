"""Defines database endpoints for directly querying from the shopping list table."""
from typing import Annotated
from fastapi import APIRouter, Depends

from app import services
from app.db import SessionDep, tables

def get_service(session: SessionDep):
    return services.Shopping(session=session)

ServiceDep = Annotated[services.Shopping, Depends(get_service)]

router = APIRouter()

@router.get("/")
def read_list(service: ServiceDep):
    return service.read_all()

@router.get("/{shopping_list_id}/")
def read(service: ServiceDep, shopping_list_id: int):
    return service.read_by_pk(primary_key=shopping_list_id)

@router.post("/{shopping_list_name}")
def create_list(service: ServiceDep, shopping_list_name: str):
    shopping_list= tables.Shopping(name=shopping_list_name)
    return service.create(shopping_list)