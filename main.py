from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
from crewai import Crew, Process
from agents import doctor
from task import help_patients

app = FastAPI(title="Blood Test Report Analyzer")

def run_crew(query: str, file_path: str):
    """Run CrewAI to process the report"""
    medical_crew = Crew(
        agents=[doctor],
        tasks=[help_patients],
        process=Process.sequential,
    )
    return medical_crew.kickoff({"query": query, "file_path": file_path})

@app.get("/")
async def root():
    return {"message": "Blood Test Report Analyzer API is running"}

@app.post("/analyze")
async def analyze_blood_report(
    file: UploadFile = File(...),
    query: str = Form(default="Summarize my Blood Test Report")
):
    file_id = str(uuid.uuid4())
    file_path = f"data/blood_test_report_{file_id}.pdf"
    try:
        os.makedirs("data", exist_ok=True)
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        response = run_crew(query.strip(), file_path)

        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass
