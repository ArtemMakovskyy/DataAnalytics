from fastapi import APIRouter

router = APIRouter(prefix="/api/test", tags=["test"])


@router.get("/health")
def health():
    return {"status": "ok"}