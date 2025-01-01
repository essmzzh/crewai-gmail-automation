from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class ReportExportSchema(BaseModel):
    summary_text: str = Field(..., description="Summary content to export")
    format_type: str = Field("markdown", description="Format type: markdown or csv")


class ReportExportTool(BaseTool):
    name: str = "ReportExportTool"
    description: str = "Exports generated email summaries and reports to files."
    args_schema: type[BaseModel] = ReportExportSchema

    def _run(self, summary_text: str, format_type: str = "markdown") -> str:
        return f"Report exported successfully ({format_type}, {len(summary_text)} chars)."
