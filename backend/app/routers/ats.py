from fastapi import APIRouter

router = APIRouter(prefix="/ats", tags=["ats"])

@router.post("/score")
def ats_score():
    # TODO: Implement ATS scoring
    return {"score": 85, "missing_keywords": ["Python", "Leadership"], "suggestions": ["Add more quantifiable results."]}
