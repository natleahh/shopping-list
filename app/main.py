"""Main app entry point."""
from fastapi import FastAPI

from app.api.v1 import shopping

app = FastAPI()

# register routes
app.include_router(shopping.router, prefix=f"/v1/list")