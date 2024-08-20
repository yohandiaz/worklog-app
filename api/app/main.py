from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    """
    Returns a database session.

    Returns:
        SessionLocal: The database session.

    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    """
    Returns a message directing the user to go to /docs to see the API documentation.
    """
    return {"Go to /docs to see the API documentation"}


@app.post("/worklogs/", response_model=schemas.WorkLog)
def create_worklog(worklog: schemas.WorkLogCreate, db: Session = Depends(get_db)):
    """
    Create a new worklog entry.

    Parameters:
    - worklog (schemas.WorkLogCreate): The worklog data to be created.
    - db (Session): The database session.

    Returns:
    - schemas.WorkLog: The created worklog.
    """
    return crud.create_worklog(db=db, worklog=worklog)


@app.get("/worklogs/", response_model=list[schemas.WorkLog])
def read_worklogs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of worklog entries.

    Parameters:
    - skip (int): The number of records to skip (default is 0).
    - limit (int): The maximum number of records to return (default is 10).
    - db (Session): The database session.

    Returns:
    - list[schemas.WorkLog]: A list of worklog entries.
    """
    return crud.get_worklogs(db=db, skip=skip, limit=limit)


@app.get("/worklogs/{worklog_id}", response_model=schemas.WorkLog)
def read_worklog(worklog_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific worklog entry by ID.

    Parameters:
    - worklog_id (int): The ID of the worklog to retrieve.
    - db (Session): The database session.

    Returns:
    - schemas.WorkLog: The retrieved worklog.

    Raises:
    - HTTPException: If the worklog with the given ID is not found (status code 404).
    """
    db_worklog = crud.get_worklog(db=db, worklog_id=worklog_id)
    if db_worklog is None:
        raise HTTPException(status_code=404, detail="WorkLog not found")
    return db_worklog


@app.put("/worklogs/{worklog_id}", response_model=schemas.WorkLog)
def update_worklog(
    worklog_id: int, worklog: schemas.WorkLogCreate, db: Session = Depends(get_db)
):
    """
    Update a worklog with the given ID.

    Parameters:
    - worklog_id (int): The ID of the worklog to be updated.
    - worklog (schemas.WorkLogCreate): The updated worklog data.
    - db (Session): The database session.

    Returns:
    - schemas.WorkLog: The updated worklog.

    Raises:
    - HTTPException: If the worklog with the given ID is not found (status code 404).
    """
    db_worklog = crud.update_worklog(db=db, worklog_id=worklog_id, worklog=worklog)
    if db_worklog is None:
        raise HTTPException(status_code=404, detail="WorkLog not found")
    return db_worklog


@app.delete("/worklogs/{worklog_id}", response_model=schemas.WorkLog)
def delete_worklog(worklog_id: int, db: Session = Depends(get_db)):
    """
    Deletes a worklog from the database.
    Parameters:
    - worklog_id (int): The ID of the worklog to be deleted.
    - db (Session): The database session.
    Returns:
    - db_worklog: The deleted worklog.
    Raises:
    - HTTPException: If the worklog is not found in the database.
    """

    db_worklog = crud.delete_worklog(db=db, worklog_id=worklog_id)
    if db_worklog is None:
        raise HTTPException(status_code=404, detail="WorkLog not found")
    return db_worklog
