from crewai.tools import BaseTool
from pydantic import Field


class AuditLogTool(BaseTool):
    name: str = "AuditLogTool"
    description: str = "Logs security and audit events for email processing."

    def _run(self, event: str) -> str:
        return f"Event logged: {event}"
