from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from routers.home import home_router
from routers.user import user_list_router
from routers.auth import auth_router
from utils.auth import AuthError


app = FastAPI(
    title="CryptoMarket",
    description="API for a cryptomarket",
    version="0.1.0"
)


@app.exception_handler(RequestValidationError)
def handle_validation_error(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    errors = {d["loc"][1]: d["msg"] for d in errors}
    return JSONResponse(errors, status_code=status.HTTP_400_BAD_REQUEST)


# @app.exception_handler(AuthError)
# def handle_auth_error(request: Request, exc: AuthError):
#     return JSONResponse({'detail': str(exc)}, status_code=status.HTTP_401_UNAUTHORIZED)


app.include_router(home_router)
app.include_router(user_list_router)
app.include_router(auth_router)