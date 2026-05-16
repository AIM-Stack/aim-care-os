from fastapi import FastAPI

app = FastAPI(
    title=\"AIM Care OS\",
    version=\"0.1.0\"
)

@app.get(\"/\")
async def root():
    return {
        \"message\": \"AIM Care OS API Running\"
    }
