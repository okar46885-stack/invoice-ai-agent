from pydantic import BaseModel, Field
from typing import List, Optional, Any


class Provenance(BaseModel):
    page: Optional[int]
    coords: Optional[List[float]] = None  # [x,y,w,h]
    text_span: Optional[str] = None


class FieldExtraction(BaseModel):
    name: str
    value: Optional[str] = None
    confidence: float = Field(..., ge=0.0, le=100.0)
    provenance: Optional[Provenance] = None


class SuggestRequest(BaseModel):
    document_id: str
    fields: List[FieldExtraction]


class SuggestionOut(BaseModel):
    suggestion_id: int
    document_id: str
    field: str
    suggestion_value: str
    confidence: float
    provenance: Optional[Any] = None
    reason: Optional[str] = None


class SuggestResponse(BaseModel):
    suggestions: List[SuggestionOut]
    document_review_required: bool


class FeedbackIn(BaseModel):
    suggestion_id: Optional[int] = None
    document_id: Optional[str] = None
    field: Optional[str] = None
    action: str  # apply/edit/reject
    corrected_value: Optional[str] = None
    reviewer_id: str
    notes: Optional[str] = None
