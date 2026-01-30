"""
Case Data Package.

Contains domain-specific patient cases for each nurse specialization.
Each module contains training cases for specialized triage agent optimization.
"""

from .chf_cases import CHF_CASES
from .preop_cases import PREOP_CASES
from .ed_cases import ED_CASES
from .pediatric_cases import PEDIATRIC_CASES
from .wound_care_cases import WOUND_CARE_CASES
from .ob_cases import OB_CASES
from .neuro_cases import NEURO_CASES
from .gi_cases import GI_CASES
from .mental_health_cases import MENTAL_HEALTH_CASES
from .respiratory_cases import RESPIRATORY_CASES

__all__ = [
    "CHF_CASES",
    "PREOP_CASES",
    "ED_CASES",
    "PEDIATRIC_CASES",
    "WOUND_CARE_CASES",
    "OB_CASES",
    "NEURO_CASES",
    "GI_CASES",
    "MENTAL_HEALTH_CASES",
    "RESPIRATORY_CASES",
]
