from sqlalchemy.orm import Session
from . import models, schemas


def create_worklog(db: Session, worklog: schemas.WorkLogCreate):
    """
    Create a new worklog entry in the database.

    Parameters:
    - db (Session): The database session.
    - worklog (schemas.WorkLogCreate): The worklog data to be created.

    Returns:
    - db_worklog (models.WorkLog): The created worklog entry.
    """
    db_worklog = models.WorkLog.from_schema(worklog)
    db.add(db_worklog)
    db.commit()
    db.refresh(db_worklog)
    return db_worklog


# Get all worklog entries with optional pagination
def get_worklogs(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of worklogs from the database.

    Args:
        db (Session): The database session.
        skip (int, optional): The number of worklogs to skip. Defaults to 0.
        limit (int, optional): The maximum number of worklogs to retrieve. Defaults to 10.

    Returns:
        List[WorkLog]: A list of worklogs.
    """
    return db.query(models.WorkLog).offset(skip).limit(limit).all()


# Get a single worklog entry by its ID
def get_worklog(db: Session, worklog_id: int):
    """
    Retrieve a worklog from the database by its ID.
    Args:
        db (Session): The database session.
        worklog_id (int): The ID of the worklog to retrieve.
    Returns:
        WorkLog: The retrieved worklog.
    """

    return db.query(models.WorkLog).filter(models.WorkLog.id == worklog_id).first()


# Update a worklog entry by its ID
def update_worklog(db: Session, worklog_id: int, worklog: schemas.WorkLogCreate):
    """
    Update a worklog in the database.

    Args:
        db (Session): The database session.
        worklog_id (int): The ID of the worklog to update.
        worklog (schemas.WorkLogCreate): The updated worklog data.

    Returns:
        models.WorkLog: The updated worklog object.
    """
    db_worklog = (
        db.query(models.WorkLog).filter(models.WorkLog.id == worklog_id).first()
    )
    if db_worklog:
        for key, value in worklog.dict().items():
            setattr(db_worklog, key, value)
        db.commit()
        db.refresh(db_worklog)
    return db_worklog


# Delete a worklog entry by its ID
def delete_worklog(db: Session, worklog_id: int):
    """
    Deletes a worklog from the database.

    Args:
        db (Session): The database session.
        worklog_id (int): The ID of the worklog to be deleted.

    Returns:
        WorkLog: The deleted worklog if it exists, otherwise None.
    """
    db_worklog = (
        db.query(models.WorkLog).filter(models.WorkLog.id == worklog_id).first()
    )
    if db_worklog:
        db.delete(db_worklog)
        db.commit()
    return db_worklog
