from fastapi import FastAPI

app = FastAPI(
    title="Gold Fund NAV API",
    version="0.1.0",
)

@app.get("/")
def home():
    return {
        "service": "Gold Fund NAV API",
        "status": "running",
        "source": "FIPIRAN",
        "nav_integration": "not_configured",
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/nav/latest")
def latest_nav():
    return {
        "status": "unavailable",
        "message": "Live NAV integration is not configured",
        "data": [],
    }
