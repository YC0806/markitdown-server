from pathlib import Path
from tempfile import NamedTemporaryFile
import os

from fastapi import FastAPI, File, HTTPException, UploadFile
from markitdown import MarkItDown

app = FastAPI(title="MarkItDown Service")

md = MarkItDown(enable_plugins=False)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/convert")
def convert(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="missing filename")

    suffix = Path(file.filename).suffix or ".bin"
    tmp_path = None

    try:
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp_path = tmp.name
            content = file.file.read()
            tmp.write(content)

        result = md.convert(tmp_path)

        return {
            "filename": file.filename,
            "markdown": result.text_content,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"conversion failed: {e}")

    finally:
        try:
            file.file.close()
        except Exception:
            pass

        if tmp_path and os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except OSError:
                pass
