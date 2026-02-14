"""Router for outcomes endpoints."""

from typing import List

from fastapi import APIRouter, HTTPException

from app.models.outcome import Outcome
from app.services.outcome_service import get_outcome_by_id, read_outcomes

router = APIRouter()


@router.get("", response_model=List[Outcome])
def get_all_outcomes():
    """Get all top-level outcomes."""
    return read_outcomes()


@router.get("/{outcome_id}", response_model=Outcome)
def get_outcome(outcome_id: str):
    """Get an outcome by id (searches the full tree)."""
    outcomes = read_outcomes()
    outcome = get_outcome_by_id(outcomes, outcome_id)
    if outcome is not None:
        return outcome
    raise HTTPException(status_code=404, detail="Outcome not found")
