from pydantic import BaseModel, Field
from crewai.tools import BaseTool


class ArchiveEmailSchema(BaseModel):
    """Schema for ArchiveEmailTool input."""
    email_id: str = Field(..., description="ID of the email to archive")
    folder: str = Field("Archive", description="Destination folder for the archived email")


class ArchiveEmailTool(BaseTool):
    """Tool to archive an email into a folder. Not used by any agent."""
    name: str = "archive_email"
    description: str = "Archive an email into a folder instead of deleting it"
    args_schema: type[BaseModel] = ArchiveEmailSchema

    def _run(self, email_id: str, folder: str = "Archive") -> str:
        """Archive an email.

        Args:
            email_id: The ID of the email to archive
            folder: The destination folder

        Returns:
            A string confirming the archive action
        """
        return f"Email {email_id} archived to {folder}."
