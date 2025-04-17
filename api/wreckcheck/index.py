from fastapi import FastAPI, File, UploadFile, HTTPException, Query
import os
import base64
from openai import OpenAI
from dotenv import load_dotenv
import json
import sys

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def clean_vehicle_data(data):
    """Remove description fields from vehicle repair data to reduce payload size."""
    if "data" in data and "repair" in data["data"]:
        for item in data["data"]["repair"]:
            if "description" in item:
                del item["description"]
    return data

@app.post("/")
async def wreckcheck(vin: str = Query(..., description="Vehicle Identification Number"), image: UploadFile = File(..., description="Image of the car")):
    try:
        # Instead of API call, load the mock data
        with open("src/public/json/repairmock_clean.json", "r") as file:
            vehicle_data = json.load(file)
        
        # Set the VIN in the mock data to match the requested VIN
        vehicle_data["data"]["vin"] = vin
        
        print(f"🚗 Successfully loaded mock vehicle data for VIN: {vin}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"🚨 Error getting vehicle data: {e}")

    try:
        # Read the image file
        image_content = await image.read()
        
        # Encode image to base64
        base64_image = base64.b64encode(image_content).decode("utf-8")
        
        # Extract vehicle info for prompt
        vehicle_info = f"{vehicle_data['data']['year']} {vehicle_data['data']['make']} {vehicle_data['data']['model']}"
        
        # Send image to OpenAI for car damage analysis AND repair estimation in one call
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are an automotive damage assessment expert. Your analysis must be direct, factual, and to the point. Never use phrases like 'I'm unable to' or 'As an AI'. Always provide clean, factual information formatted in markdown. Always use actual dollar values for estimates based on the provided repair cost data - never use placeholders like 'XXX' or generic text."
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": f"""Analyze this image of a {vehicle_info} and provide:

1. DAMAGE ANALYSIS:
   - List each damaged area with location, severity (minor/moderate/severe), and type of damage
   - Recommend repair approach for each area (repair, replace, paint, etc.)

2. REPAIR ESTIMATE:
   Using the following repair cost data, create a detailed estimate with ACTUAL DOLLAR VALUES (not placeholders):
   
   {json.dumps(vehicle_data['data']['repair'])}
   
   IMPORTANT: Match repairs to the most relevant items in the data and use the actual cost values. DO NOT use placeholders like $XXX or any text in cost fields - use actual numbers.

OUTPUT FORMAT:
```markdown
## DAMAGE ANALYSIS
- Area 1: [description of damage with severity]
  - Repair recommendation: [approach]
- Area 2: [description of damage with severity]
  - Repair recommendation: [approach]
...

## REPAIR ESTIMATE
| Item | Parts | Labor | Total |
|------|-------|-------|-------|
| Item 1 | $125 | $250 | $375 |
| Item 2 | $300 | $150 | $450 |
...

TOTAL ESTIMATE: $XXX
```

IMPORTANT: 
- Start your response with the markdown formatting above. No introductory text.
- Use ACTUAL dollar values from the repair data - never use placeholders like XXX."""},
                        {"type": "image_url", "image_url": {"url": f"data:image/{image.content_type};base64,{base64_image}"}}
                    ]
                }
            ],
            max_tokens=1200
        )
        
        # Extract the combined analysis and estimate
        analysis_and_estimate = response.choices[0].message.content
        
        # Remove markdown backticks from the response
        analysis_and_estimate = analysis_and_estimate.replace("```markdown", "").replace("```", "").strip()
        
        print(f"🔍 Generated damage analysis and repair estimate")
        
        return {
            "analysis_and_estimate": analysis_and_estimate,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"🚨 Error: {e}")
