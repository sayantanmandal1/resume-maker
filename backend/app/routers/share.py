from fastapi import APIRouter

router = APIRouter(prefix="/share", tags=["share"])

@router.get("/{token}")
def get_shared_resume(token: str):
    # TODO: Implement real sharing logic
    return {"msg": f"Shared resume for token {token} (stub)"}

