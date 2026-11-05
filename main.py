import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PKG_FILE = "Infinitykkj-STORE-0.0.12-PS4-Beta-PKG.pkg"
ICON_FILE = "ICON0.png"

app = FastAPI(title="Infinity Store PS4 Installer")

# Habilita CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def index():
    html_path = os.path.join(BASE_DIR, "index.html")
    if not os.path.exists(html_path):
        raise HTTPException(status_code=404, detail="index.html não encontrado.")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/download/Infinitykkj-STORE.pkg")
@app.get("/download/loja.pkg")
def download_pkg():
    pkg_path = os.path.join(BASE_DIR, PKG_FILE)
    if not os.path.exists(pkg_path):
        raise HTTPException(status_code=404, detail=f"Arquivo {PKG_FILE} não encontrado no servidor.")
    return FileResponse(
        pkg_path,
        media_type="application/octet-stream",
        filename="Infinitykkj-STORE.pkg"
    )

@app.get("/download/ICON0.png")
@app.get("/ICON0.png")
def download_icon():
    icon_path = os.path.join(BASE_DIR, ICON_FILE)
    if not os.path.exists(icon_path):
        raise HTTPException(status_code=404, detail=f"Arquivo {ICON_FILE} não encontrado no servidor.")
    return FileResponse(
        icon_path,
        media_type="image/png",
        filename="ICON0.png"
    )

if __name__ == "__main__":
    import uvicorn
    porta = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=porta, reload=False)
