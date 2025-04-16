from fastapi import FastAPI, File, UploadFile
import os
import base64
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.post("/")
async def wreckcheck(image: UploadFile = File(...)):
    # Read the image file
    image_content = await image.read()
    
    # Encode image to base64
    base64_image = base64.b64encode(image_content).decode("utf-8")
    
    # Send image to OpenAI for car damage analysis
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Analyze this car image and describe any visible damage. If there is damage, please specify the location, severity, and provide a brief description."},
                    {"type": "image_url", "image_url": {"url": f"data:image/{image.content_type};base64,{base64_image}"}}
                ]
            }
        ],
        max_tokens=500
    )
    
    # Extract the analysis
    analysis = response.choices[0].message.content
    
    return {"damage_analysis": analysis}

@app.post("/estimate")
async def estimate(damage_analysis: str):
    return {"estimate": "1000"}