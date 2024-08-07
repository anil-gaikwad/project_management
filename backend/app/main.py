import logging
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute


from backend.app.common.exceptions import CustomException, FastAPIExceptionHandlers
from backend.app.routers.company import company_router
from backend.app.routers.employee import employee_router
from backend.app.routers.project import project_router
from backend.app.common.utils import get_validation_error_message
from backend.app.routers.websocket import ws_router

logger = logging.getLogger(__name__)

project_app = FastAPI(
    title="Project Management Rest APIs",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
    swagger_ui_parameters={"displayRequestDuration": True},
)


project_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Add Custom Exception Handlers
FastAPIExceptionHandlers(app=project_app)

# Add routers
project_app.include_router(company_router)
project_app.include_router(employee_router)
project_app.include_router(project_router)
project_app.include_router(ws_router)

# Initialized API endpoints
endpoints = []
for route in project_app.routes:
    if isinstance(route, APIRoute):
        endpoints.append(f"{','.join(route.methods)} - {route.name}: {route.path}")
logger.info("List of api", extra={"props": {"endpoint": endpoints}})


@project_app.get("/")
def read_root():
    return {"message": "Welcome to the Project Management API"}


@project_app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    raw_errors = exc.errors()
    error_wrapper = raw_errors[0]
    if isinstance(error_wrapper, list):
        error_wrapper = error_wrapper[0]

    if isinstance(error_wrapper, dict):
        loc = error_wrapper["loc"]
        error_message = get_validation_error_message(error_dict=error_wrapper, loc=loc)
        if not error_message:
            error_message = f"{loc[-1]} is required property"
        raise CustomException(
            status_code=400, message=error_message, payload=error_wrapper
        )
    else:
        validation_error = error_wrapper
        raise CustomException(status_code=400, message=str(validation_error))


if __name__ == "__main__":
    import uvicorn

    logger.info("Running project locally...")
    uvicorn.run(
        app="backend.app.main:project_app",
        host="0.0.0.0",
        port=3000,
        reload=True,
    )