from fastapi import FastAPI

app = FastAPI(
    title="MossVoice AI",
    description="AI Voice Salesforce Assistant using Moss",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "MossVoice AI is running",
        "status": "success"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/leads")
def get_leads():
    return {
        "message": "Lead retrieval will use Moss + Salesforce",
        "leads": []
    }
