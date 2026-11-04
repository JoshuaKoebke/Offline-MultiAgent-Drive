import os
import streamlit as st
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import tool
from crewai_tools import FileReadTool

# Setup Page Layout & USB Workspace
st.set_page_config(page_title="Local AI Agent Workspace", layout="wide")
st.title("🧳 Portable Multi-Agent Manager")
USB_DRIVE_PATH = "D:/AI_Workspace"
os.makedirs(USB_DRIVE_PATH, exist_ok=True)

# Define tools and direct LLM instantiation
file_reader_tool = FileReadTool()

@tool("Write File to USB Drive")
def write_to_usb_tool(filename: str, content: str) -> str:
    """Useful to create or overwrite a file on the USB drive."""
    safe_path = os.path.join(USB_DRIVE_PATH, os.path.basename(filename))
    try:
        with open(safe_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Success! File saved to: {safe_path}"
    except Exception as e:
        return f"Error writing file: {str(e)}"

# Direct LLM Object Instantiation (Bypasses cloud provider validation)
local_brain = LLM(
    model="openai/qwen3-4b-thinking-2507.Q4_K_M.gguf",
    base_url="http://localhost:8080/v1",
    api_key="na"
)

# Streamlit Interface and Crew Execution
user_goal = st.text_area("What mission do you want to assign your Agent Team?")
if st.button("🚀 Launch Agent Team", type="primary"):
    if not user_goal.strip():
        st.warning("Please type a goal first!")
    else:
        with st.spinner("Deploying workers..."):
            
            # FIXED: Added required backstory configurations to avoid Pydantic errors
            coder_agent = Agent(
                role="Coder", 
                goal="Write functional Python code modules.", 
                backstory="You are an expert developer focused on clean, efficient code.",
                tools=[write_to_usb_tool], 
                llm=local_brain
            )
            
            reviewer_agent = Agent(
                role="Auditor", 
                goal="Review written code for security bugs and syntax typos.", 
                backstory="You are a strict code quality controller who reads raw source files.",
                tools=[file_reader_tool], 
                llm=local_brain
            )
            
            # FIXED: Added required backstory to the Task layout mapping
            complex_task = Task(
                description=user_goal, 
                expected_output="Final summary report detailing all actions taken."
            )
            
            # FIXED: Properly pass the local brain to the hierarchical orchestration crew
            manager_crew = Crew(
                agents=[coder_agent, reviewer_agent],
                tasks=[complex_task],
                process=Process.hierarchical,
                manager_llm=local_brain,
                verbose=True
            )
            
            final_report = manager_crew.kickoff()
            st.success("🎯 Mission Completed!")
            st.write(str(final_report))
