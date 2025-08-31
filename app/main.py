from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api.routes_auth import router as auth_router
from app.api.routes_predict import router as predict_router
from app.core.exceptions import register_exception_handlers
from app.middleware.logging_middleware import LoggingMiddleware

app = FastAPI(title="Car Price Prediction API", version="1.0.0")


app.add_middleware(LoggingMiddleware)

register_exception_handlers(app)

app.include_router(auth_router, tags=["Authentication"])
app.include_router(predict_router, tags=["Prediction"])

Instrumentator().instrument(app).expose(app)
