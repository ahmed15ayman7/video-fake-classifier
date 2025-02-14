from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from classifier import classify_video
from fastapi.middleware.cors import CORSMiddleware

# إنشاء تطبيق FastAPI
app = FastAPI()

# 🔹 تمكين CORS لتجنب مشاكل الوصول من أي موقع
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # يمكنك تخصيص النطاقات المسموح بها
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# تعريف نوع الطلب باستخدام Pydantic
class VideoRequest(BaseModel):
    video_url: str

@app.post("/classify")
async def classify(request_data: VideoRequest):
    video_url = request_data.video_url
    if not video_url:
        raise HTTPException(status_code=400, detail="No video URL provided.")

    result = classify_video(video_url)
    return result

# تشغيل التطبيق عند استخدام Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
