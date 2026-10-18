from fastapi import APIRouter

from app.models.cohort_models import RetentionResponse
from app.services import cohort_service

router = APIRouter(prefix="/api/cohort-analysis", tags=["cohort-analysis"])


@router.get("/retention", response_model=RetentionResponse)
def get_retention() -> RetentionResponse:
    return cohort_service.build_cohort_analysis()
