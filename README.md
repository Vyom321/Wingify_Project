
# Wingify_Project

# Blood Test Report Analyzer (CrewAI + FastAPI)
A professional-grade API to analyze blood test reports in PDF format using CrewAI and LLM agents. This project enables automated extraction and summarization of key health indicators from lab reports.

# Table of Contents
Project Overview
Features
Setup Instructions
Environment Variables
Running the Application
API Documentation
Bugs Fixed
Sample Request
Example Output
License

# Project Overview
The Blood Test Report Analyzer automates the interpretation of lab test reports by using a general physician agent built on CrewAI. It takes a blood report in PDF format and returns a structured analysis or summary, which can be customized through a natural language query.

# Features
Upload PDF reports and receive summaries.
Intelligent LLM-based general physician agent.
Uses LangChain PDF loader for data parsing.
Easily extendable to include nutrition or fitness agents.
Clean and RESTful FastAPI backend.

# Setup Instructions
bash
Copy
Edit
git clone https://github.com/Vyom321/blood-test-analyzer.git
cd blood-test-analyzer
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
# Install dependencies
pip install -r requirements.txt

# Environment Variables
Create a .env file and add your OpenAI API key:
bash
Copy
Edit
OPENAI_API_KEY=your-openai-api-key-here
You can copy from .env.example

# Running the Application
To start the FastAPI server:
bash
Copy
Edit
uvicorn main:app --reload
Access the Swagger docs at:
http://127.0.0.1:8000/docs
or ReDoc at:
http://127.0.0.1:8000/redoc

# API Documentation
POST /analyze
Request:
file: PDF file (required)
query: Natural language question or instruction (optional)
Default Query: "Summarize my Blood Test Report"
Response Format:
json
Copy
Edit
{
  "status": "success",
  "query": "Summarize my Blood Test Report",
  "analysis": "The patient’s cholesterol levels are within range...",
  "file_processed": "report.pdf"
}
#  Bugs Fixed
File	Bug Description	Fix Applied
agents.py	Undefined LLM (llm = llm)	Integrated ChatOpenAI with .env key
tools.py	Missing PDFLoader import	Imported from langchain.document_loaders
task.py	Unrealistic and unprofessional task descriptions	Rewritten to reflect ethical, factual goals
main.py	File not passed into the tool correctly	Fixed file saving, reading, and cleanup

# Sample Request (cURL)
bash
Copy
Edit
curl -X POST http://127.0.0.1:8000/analyze \
  -F "file=@blood_test_report.pdf" \
  -F "query=Summarize my liver profile"
Example Output
json
Copy
Edit
{
  "status": "success",
  "query": "Summarize my liver profile",
  "analysis": "The liver enzymes AST and ALT are within the normal range...",
  "file_processed": "blood_test_report.pdf"
}
📄 License
This project is intended for educational and research purposes only. Not a substitute for professional medical advice.

