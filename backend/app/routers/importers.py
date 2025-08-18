from fastapi import APIRouter, UploadFile, File

router = APIRouter(prefix="/imports", tags=["imports"])

@router.post("/linkedin")
def import_linkedin(file: UploadFile = File(...)):
    # TODO: Parse LinkedIn PDF/JSON
    return {"msg": "LinkedIn import (stub)", "data": {}}

@router.post("/github")
def import_github(username: str):
    # TODO: Fetch GitHub repos
    return {"msg": "GitHub import (stub)", "projects": []}

@router.post("/resume")
def import_resume(file: UploadFile = File(...)):
    # TODO: Parse resume PDF
    return {"msg": "Resume import (stub)", "data": {}}
