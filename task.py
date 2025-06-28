from crewai import Task
from agents import doctor
from tools import BloodTestReportTool

help_patients = Task(
    description="Analyze the uploaded blood report and generate a medically appropriate summary. "
                "Ensure the information is accurate and clearly explained to the user.",
    expected_output="A structured summary including key values (e.g., CBC, Lipid Profile, Liver function) "
                    "and health implications, formatted as bullet points or a readable paragraph.",
    agent=doctor,
    tools=[BloodTestReportTool().read_data_tool],
    async_execution=False
)
