
from langgraph.graph import StateGraph, START, END

from state import JobAnalysisState
from nodes import (
    extract_information,
    classify_job,
    analyze_skills,
    generate_report,
)


def build_graph():
    workflow = StateGraph(JobAnalysisState)

    workflow.add_node("extract_information", extract_information)
    workflow.add_node("classify_job", classify_job)
    workflow.add_node("analyze_skills", analyze_skills)
    workflow.add_node("generate_report", generate_report)

    workflow.add_edge(START, "extract_information")
    workflow.add_edge("extract_information", "classify_job")
    workflow.add_edge("classify_job", "analyze_skills")
    workflow.add_edge("analyze_skills", "generate_report")
    workflow.add_edge("generate_report", END)

    return workflow.compile()


job_analysis_graph = build_graph()
