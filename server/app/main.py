from typing import Union

from fastapi import FastAPI
from .api  import product, category , login, user, role , role_permissions, permissions
# from .database import engine
# from .models import Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.include_router(product.router, tags=["Product"])
app.include_router(category.router, tags=["Categories"])
app.include_router(login.router, tags="Login")
app.include_router(user.router, tags="User")
app.include_router(role.router, tags="Role")
app.include_router(permissions.router , tags="Permissions")
app.include_router(role_permissions.router , tags="Role Permissions")
origins = [
    "http://localhost:3000",  # Địa chỉ ứng dụng Next.js
    "http://127.0.0.1:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
