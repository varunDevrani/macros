from fastapi import FastAPI

from src.database.base import Base
from src.database.connect_db import engine
from src.exceptions import register_exception_handlers
from src.routes.auth import router as auth_router
from src.routes.skill import router as skill_router
from src.routes.user import router as user_router

app = FastAPI()


@app.on_event("startup")
def startup():
	Base.metadata.create_all(
		bind=engine
	)

@app.on_event("shutdown")
def shutdown():
	print("app shutting down...")


register_exception_handlers(app)

app.include_router(user_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1")
app.include_router(skill_router, prefix="/api/v1")
