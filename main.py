import os
from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import google.generativeai as genai

app = FastAPI()

# IMPORTANT: Link your HTML
@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

@app.post("/repurpose")
async def repurpose_content(text: str = Form(...)):
    prompt = f"Repurpose the following text into a 5-tweet Twitter thread, a LinkedIn post, and an Instagram caption. Use emojis and make it engaging:\n\n {text}"
    response = model.generate_content(prompt)
    return {"result": response.text}
