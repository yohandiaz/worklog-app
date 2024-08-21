from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean

from . import schemas

from .database import Base


class WorkLog(Base):
    """
    WorkLog model for storing work log entries.

    Attributes:
        id (int): Primary key for the work log entry.
        task (str): Task name associated with the work log entry.
        description (str): Description of the work log entry.
        date (datetime): Date and time when the work log entry was created.
        is_highlighted (bool): Flag indicating if the work log entry is highlighted.
    """

    __tablename__ = "worklogs"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.now)
    is_highlighted = Column(Boolean, default=False)

    def __repr__(self):
        return (
            f"<WorkLog(id={self.id}, task={self.task}, description={self.description}, "
            f"date={self.date}, is_highlighted={self.is_highlighted})>"
        )

    @staticmethod
    def from_schema(scheme: schemas.WorkLogCreate) -> "WorkLog":

        return WorkLog(
            task=scheme.task,
            description=scheme.description,
            date=scheme.date,
            is_highlighted=scheme.is_highlighted,
        )
