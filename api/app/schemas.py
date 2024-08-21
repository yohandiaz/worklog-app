from datetime import datetime, date as date_type
from pydantic import BaseModel, Field


class WorkLogBase(BaseModel):
    """
    Base model for work log entries.

    Attributes:
        task (str): Task name associated with the work log entry.
        description (str): Description of the work log entry.
        date (datetime): Date and time when the work log entry was created.
        is_highlighted (bool): Flag indicating if the work log entry is highlighted.
        inserted_at (datetime): Date and time when the work log entry was inserted.
    """

    task: str
    description: str = Field(default='')
    date: date_type = Field(default_factory=date_type.today)
    is_highlighted: bool = False
    inserted_at: datetime
    # updated_at: datetime


class WorkLogCreate(WorkLogBase):
    """
    Model for creating a new work log entry.
    Inherits all attributes from WorkLogBase.
    """

    pass


class WorkLog(WorkLogBase):
    """
    Model for representing a work log entry with an ID.

    Attributes:
        id (int): Primary key for the work log entry.
    Inherits all attributes from WorkLogBase.
    """

    id: int

    class Config:
        """
        Configuration class for the schema.
        Attributes:
            orm_mode (bool): Flag indicating whether to use ORM mode or not.
        """

        orm_mode = True
