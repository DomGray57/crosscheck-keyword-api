from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# ✅ Home route (already working)
@app.get("/")
def home():
    return {"message": "Crosscheck Keyword API is live!"}

# 🧠 Define input model
class CrosscheckRequest(BaseModel):
    keyword: str

# 🔍 Simulated crosscheck route
@app.post("/crosscheck_keyword")
def crosscheck_keyword(request: CrosscheckRequest):
    keyword = request.keyword
    return {
        "keyword": keyword,
        "results": {
            "google_trends": {
                "average_score": random.randint(40, 80),
                "peak_score": random.randint(80, 100),
                "last_24h": random.randint(30, 90),
                "status": "rising" if random.random() > 0.5 else "steady"
            },
            "tiktok": {
                "hashtag": f"#{keyword.replace(' ', '')}",
                "views": f"{random.randint(1, 10)}.{random.randint(0, 9)}M",
                "trend": "gaining" if random.random() > 0.5 else "stable"
            },
            "pinterest": {
                "suggestions": [f"{keyword} outfit", f"{keyword} aesthetic", f"{keyword} moodboard"]
            },
            "etsy": {
                "listings": random.randint(50, 1000),
                "competition": "low" if random.random() > 0.6 else "medium"
            },
            "reddit": {
                "mentions": random.randint(5, 50),
                "vibe": random.choice(["positive", "neutral", "mixed", "trending"])
            }
        },
        "insight": "Simulated response. Hooked up for real-time integration later."
    }
