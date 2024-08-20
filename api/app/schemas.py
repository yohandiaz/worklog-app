from datetime import datetime
from pydantic import BaseModel


class WorkLogBase(BaseModel):
    """
    Base model for work log entries.

    Attributes:
        task (str): Task name associated with the work log entry.
        description (str): Description of the work log entry.
        date (datetime): Date and time when the work log entry was created.
        is_highlighted (bool): Flag indicating if the work log entry is highlighted.
    """

    task: str
    description: str
    date: datetime
    is_highlighted: bool = False


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
