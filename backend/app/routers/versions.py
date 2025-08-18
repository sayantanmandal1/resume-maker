from fastapi import APIRouter

router = APIRouter(prefix="/versions", tags=["versions"])

@router.get("/test")
def test_versions():
    return {"msg": "Versions router working"}
