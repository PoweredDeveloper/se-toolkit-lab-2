"""Service for loading and querying outcomes from JSON data."""

import json
from typing import List, Optional

from app.models.outcome import Outcome
from app.settings import settings


def read_outcomes() -> List[Outcome]:
    """Load outcomes from outcomes.json."""
    with open(settings.outcomes_path, "r", encoding="utf-8") as handle:
        raw = json.load(handle)
    return [Outcome.model_validate(o) for o in raw["outcomes"]]


def get_outcome_by_id(outcomes: List[Outcome], outcome_id: str) -> Optional[Outcome]:
    """Find an outcome by id in the tree (depth-first)."""
    for o in outcomes:
        if o.id == outcome_id:
            return o
        found = get_outcome_by_id(o.suboutcomes, outcome_id)
        if found is not None:
            return found
    return None
