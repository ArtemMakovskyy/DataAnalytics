from pydantic import BaseModel


class RetentionRow(BaseModel):
    cohort_month: str
    retention: list[float | None]


class RetentionResponse(BaseModel):
    count: int
    rows: list[RetentionRow]
