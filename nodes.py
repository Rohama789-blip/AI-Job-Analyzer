
from langchain_core.messages import HumanMessage, SystemMessage

from llm import get_llm
from schemas import JobExtraction, JobClassification, SkillAnalysis


def extract_information(state: dict) -> dict:
    """Node 1: Extract basic job information."""
    llm = get_llm().with_structured_output(JobExtraction)

    result = llm.invoke([
        SystemMessage(
            content=(
                "Extract information only from the supplied job description. "
                "Do not invent missing details. Use 'Not specified' when "
                "the title, company, or experience is unavailable. "
                "Return an empty list when skills are not specified."
            )
        ),
        HumanMessage(content=state["job_description"]),
    ])

    return result.model_dump()


def classify_job(state: dict) -> dict:
    """Node 2: Classify job category and employment type."""
    llm = get_llm().with_structured_output(JobClassification)

    result = llm.invoke([
        SystemMessage(
            content=(
                "Classify the job into a category such as AI, Web Development, "
                "Data Science, Mobile Development, DevOps, or Other. "
                "Identify the employment type only from the description. "
                "If it is missing, return 'Not specified'. "
                "Do not assume that every job is remote or full-time."
            )
        ),
        HumanMessage(content=state["job_description"]),
    ])

    return result.model_dump()


def analyze_skills(state: dict) -> dict:
    """Node 3: Identify technical skills, soft skills, and top three."""
    llm = get_llm().with_structured_output(SkillAnalysis)

    result = llm.invoke([
        SystemMessage(
            content=(
                "Analyze the supplied job description. Separate technical "
                "skills from soft skills. Select up to three important skills "
                "that are explicitly required or strongly emphasized. "
                "Do not invent requirements. If information is insufficient, "
                "return fewer skills."
            )
        ),
        HumanMessage(content=state["job_description"]),
    ])

    return result.model_dump()


def generate_report(state: dict) -> dict:
    """Node 4: Combine all results into a hiring report."""
    report = {
        "job_title": state.get("job_title", "Not specified"),
        "company_name": state.get("company_name", "Not specified"),
        "required_experience": state.get(
            "required_experience", "Not specified"
        ),
        "required_skills": state.get("required_skills", []),
        "job_category": state.get("job_category", "Not specified"),
        "employment_type": state.get("employment_type", "Not specified"),
        "technical_skills": state.get("technical_skills", []),
        "soft_skills": state.get("soft_skills", []),
        "top_3_skills": state.get("top_3_skills", [])[:3],
    }

    return {"hiring_report": report}
