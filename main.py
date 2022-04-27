from fastapi import FastAPI
from routers.home import home_router
from routers.user import user_list_router


app = FastAPI(
    title="CryptoMarket",
    description="API for a cryptomarket",
    version="0.1.0"
)


app.include_router(home_router)
app.include_router(user_list_router)