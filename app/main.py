import logging

import uvicorn
from fastapi import FastAPI
from app.controllers import cohort_analysis_controller, test_controller

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="DataAnalytics API")
app.include_router(test_controller.router)
app.include_router(cohort_analysis_controller.router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)