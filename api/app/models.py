from sqlalchemy import Column, Integer, String, DateTime, Boolean

from . import schemas

from .database import Base


class WorkLog(Base):
    """
    Represents a work log entry.

    Attributes:
        id (int): The unique identifier for the work log.
        task (str): The task associated with the work log.
        description (str): The description of the work log.
        date (datetime): The date of the work log.
        is_highlighted (bool): Indicates if the work log is highlighted.
        inserted_at (datetime): The timestamp when the work log was inserted.

    Methods:
        __repr__(): Returns a string representation of the work log.
        from_schema(scheme: schemas.WorkLogCreate) -> "WorkLog": Creates a WorkLog instance from a schema.

    """

    __tablename__ = "worklogs"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    date = Column(DateTime, nullable=True)
    is_highlighted = Column(Boolean, default=False)
    inserted_at = Column(DateTime, nullable=False)
    # updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    def __repr__(self):
        """
        Return a string representation of the WorkLog object.
        Returns:
            str: A formatted string representing the WorkLog object.
        """

        return (
            f"<WorkLog(id={self.id}, task={self.task}, description={self.description}, "
            f"date={self.date}, is_highlighted={self.is_highlighted}, inserted_at={self.inserted_at})>"
        )

    @staticmethod
    def from_schema(scheme: schemas.WorkLogCreate) -> "WorkLog":
        """
        Convert a WorkLogCreate schema object to a WorkLog object.
        Parameters:
        - scheme: A WorkLogCreate schema object representing the data to be converted.
        Returns:
        - WorkLog: A WorkLog object with the converted data.
        """

        return WorkLog(
            task=scheme.task,
            description=scheme.description,
            date=scheme.date,
            is_highlighted=scheme.is_highlighted,
            inserted_at=scheme.inserted_at,
            # updated_at=scheme.updated_at,
        )
