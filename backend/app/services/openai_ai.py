import os, httpx
from ..config import settings

OPENAI_URL = "https://api.openai.com/v1/chat/completions"

async def suggest_bullets(resume_json: dict, jd_text: str):
    if not settings.OPENAI_API_KEY:
        return {"suggestions": [], "note": "OPENAI_API_KEY not set"}
    prompt = (
        "You are an expert resume coach for software engineers. "
        "Given the user's current resume data (JSON) and the target job description, "
        "propose 3-5 concise STAR-style bullet points each <= 25 words, prioritized for ATS keywords. "
        "Return JSON with fields: bullets[].\n\n"
        f"RESUME_JSON:\n{resume_json}\n\nJOB_DESCRIPTION:\n{jd_text}"
    )
    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(
            OPENAI_URL,
            headers={"Authorization": f"Bearer {settings.OPENAI_API_KEY}"},
            json={"model": "gpt-4o-mini", "messages":[{"role":"user","content":prompt}], "temperature":0.3}
        )
    data = r.json()
    text = data["choices"][0]["message"]["content"]
    return {"raw": text}
