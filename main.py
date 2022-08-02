from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from routers.home import home_router
from routers.user import user_list_router, user_detail_router
from routers.auth import auth_router
from routers.exchange import exchange_rate_router
from routers.currency import currency_router
from routers.transaction import transaction_list_router
from routers.account import account_list_router
from exceptions.auth import AuthError


app = FastAPI(
    title="CryptoExchange", description="API for crypto exchange", version="0.1.0"
)


@app.exception_handler(RequestValidationError)
def handle_validation_error(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    errors = {d["loc"][1]: d["msg"] for d in errors}
    return JSONResponse({"detail": errors}, status_code=status.HTTP_400_BAD_REQUEST)


@app.exception_handler(AuthError)
def handle_auth_error(request: Request, exc: AuthError):
    return JSONResponse({"detail": str(exc)}, status_code=status.HTTP_401_UNAUTHORIZED)


app.include_router(home_router)
app.include_router(user_list_router)
app.include_router(user_detail_router)
app.include_router(auth_router)
app.include_router(exchange_rate_router)
app.include_router(currency_router)
app.include_router(transaction_list_router)
app.include_router(account_list_router)
