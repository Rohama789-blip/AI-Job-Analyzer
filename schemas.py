
from pydantic import BaseModel, Field


class JobExtraction(BaseModel):
    job_title: str = Field(description="Job title")
    company_name: str = Field(description="Company name, or Not specified")
    required_experience: str = Field(description="Required experience")
    required_skills: list[str] = Field(description="Required skills")


class JobClassification(BaseModel):
    job_category: str = Field(description="Job category")
    employment_type: str = Field(
        description="Full-time, Part-time, Internship, Contract, or other stated type"
    )


class SkillAnalysis(BaseModel):
    technical_skills: list[str] = Field(description="Technical skills")
    soft_skills: list[str] = Field(description="Soft skills")
    top_3_skills: list[str] = Field(
        description="Three most important skills, or fewer if insufficient information"
    )
