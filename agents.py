import os
from dotenv import load_dotenv
load_dotenv()

from crewai.agents import Agent
from tools import BloodTestReportTool
from langchain.chat_models import ChatOpenAI


llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)


doctor = Agent(
    role="General Physician",
    goal="Summarize and explain blood test report with clinical reasoning",
    verbose=True,
    memory=True,
    backstory="A qualified medical doctor providing evidence-based insights from lab results.",
    tool=[BloodTestReportTool().read_data_tool],
    llm=llm,
    allow_delegation=False
)
