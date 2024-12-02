from datetime import datetime
from fastapi import FastAPI, Depends, Form, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add CORS middleware for API access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

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


@app.get("/", response_class=HTMLResponse)
async def read_worklogs_html(request: Request, db: Session = Depends(get_db)):
    """
    Render the homepage with a list of worklogs.

    Parameters:
    - request (Request): The incoming HTTP request.
    - db (Session): The database session.

    Returns:
    - HTMLResponse: The rendered HTML template.
    """
    worklogs = crud.get_worklogs(db=db, skip=0, limit=100)
    return templates.TemplateResponse("worklogs.html", {"request": request, "worklogs": worklogs})


# --- API Endpoints ---

@app.get("/api/", response_model=dict)
def read_root():
    """
    Returns a message directing the user to go to /docs to see the API documentation.
    """
    return {"message": "Go to /docs to see the API documentation"}


@app.post("/api/worklogs/", response_model=schemas.WorkLog)
def create_worklog(worklog: schemas.WorkLogCreate, db: Session = Depends(get_db)):
    """
    Create a new worklog entry from JSON data.
    """
    # Set default date to today if not provided
    if not worklog.date:
        worklog.date = datetime.now().strftime("%Y-%m-%d")
    
    return crud.create_worklog(db=db, worklog=worklog)




@app.get("/api/worklogs/", response_model=list[schemas.WorkLog])
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


@app.get("/api/worklogs/{worklog_id}", response_model=schemas.WorkLog)
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


@app.put("/api/worklogs/{worklog_id}", response_model=schemas.WorkLog)
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


@app.delete("/api/worklogs/{worklog_id}", response_model=schemas.WorkLog)
def delete_worklog(worklog_id: int, db: Session = Depends(get_db)):
    """
    Deletes a worklog from the database.

    Parameters:
    - worklog_id (int): The ID of the worklog to be deleted.
    - db (Session): The database session.

    Returns:
    - schemas.WorkLog: The deleted worklog.

    Raises:
    - HTTPException: If the worklog is not found in the database.
    """
    db_worklog = crud.delete_worklog(db=db, worklog_id=worklog_id)
    if db_worklog is None:
        raise HTTPException(status_code=404, detail="WorkLog not found")
    return db_worklog
