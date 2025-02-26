import sentry_sdk
import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter
from starlette_exporter import handle_metrics
from starlette_exporter import PrometheusMiddleware

import settings
from api.handlers import user_router
from api.login_handler import login_router
from api.service import service_router

# sentry configuration
if settings.SENTRY_URL:
    sentry_sdk.init(
        dsn=settings.SENTRY_URL,
        send_default_pii=True,
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production,
        traces_sample_rate=1.0,
        _experiments={
            "continuous_profiling_auto_start": True,
        },
    )

#########################
# BLOCK WITH API ROUTES #
#########################

# create instance of the app
app = FastAPI(title="Beybars-API")
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

# create the instance for the routes
main_api_router = APIRouter()

# set routes to the app instance
main_api_router.include_router(user_router, prefix="/user", tags=["user"])
main_api_router.include_router(login_router, prefix="/login", tags=["login"])
main_api_router.include_router(service_router, tags=["service"])
app.include_router(main_api_router)

if __name__ == "__main__":
    # run app on the host and port
    uvicorn.run(app, host="127.0.0.1", port=settings.APP_PORT)
