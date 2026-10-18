from fastapi import APIRouter

router = APIRouter(prefix="/api/cohort-analysis", tags=["cohort-analysis"])


@router.get("/run")
def run_analysis():
    return {"status": "stub"}
