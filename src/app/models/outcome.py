"""Models for learning outcomes."""

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel


class Outcome(BaseModel):
    """A node in the outcomes tree (course/lab/outcome/suboutcome).

    Attributes:
        id: Unique identifier.
        type: Kind of outcome (e.g. course_outcomes, lab_outcomes, outcome, suboutcome).
        titles: Localized titles.
        descriptions: Localized descriptions.
        coverage_notes: Optional localized coverage notes.
        related_item_ids: Optional list of related course item ids.
        suboutcomes: Nested outcomes.
    """

    id: str
    type: str
    titles: Optional[Dict[str, str]] = None
    descriptions: Optional[Dict[str, str]] = None
    coverage_notes: Optional[Dict[str, str]] = None
    related_item_ids: Optional[List[str]] = None
    suboutcomes: List[Outcome] = []
