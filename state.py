
from typing import TypedDict


class JobAnalysisState(TypedDict, total=False):
    job_description: str

    # Node 1: Information Extraction
    job_title: str
    company_name: str
    required_experience: str
    required_skills: list[str]

    # Node 2: Job Classification
    job_category: str
    employment_type: str

    # Node 3: Skill Analysis
    technical_skills: list[str]
    soft_skills: list[str]
    top_3_skills: list[str]

    # Node 4: Final Report
    hiring_report: dict
    error: str
