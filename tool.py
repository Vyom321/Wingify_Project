import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools.tools.serper_dev_tool import SerperDevTool
from langchain.document_loaders import PDFLoader

# Internet search tool (if needed)
search_tool = SerperDevTool()

# Blood test PDF reader tool
class BloodTestReportTool:
    async def read_data_tool(self, path='data/sample.pdf'):
        """Reads and returns full content from a blood test PDF report"""
        docs = PDFLoader(file_path=path).load()
        content = ""
        for page in docs:
            clean = page.page_content.replace("\n\n", "\n")
            content += clean + "\n"
        return content
