FROM python:3.11-slim

# latex + build tools for PDF rendering
RUN apt-get update && apt-get install -y --no-install-recommends \
    texlive-latex-base texlive-latex-extra texlive-fonts-recommended \
    texlive-xetex latexmk ghostscript poppler-utils git build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml /app/
RUN pip install --no-cache-dir -e .

COPY app /app/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
