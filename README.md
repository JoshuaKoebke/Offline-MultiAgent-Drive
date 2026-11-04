# Offline-MultiAgent-Drive
A fully portable, 100% offline multi-agent AI system running from a USB drive. Powered by local Qwen3 and CrewAI to write, audit, and log software utilities locally without API costs. However the model can be substituted with any model the computer is able to run.
# 🧳 Portable Multi-Agent AI Workspace (Offline USB Setup)

A fully portable, 100% offline multi-agent AI orchestration system designed to run entirely from a high-speed USB drive. This workspace turns a single, local language model into a hierarchical team of specialized AI agents (Manager, Coder, and Auditor) that can write, test, and save software utilities directly to your local file system without internet dependencies or cloud API costs.

## 🌟 Core Features
- **Zero Cloud Costs & Absolute Privacy:** Powered entirely by a local offline model wrapper. No data ever leaves your machine, and you pay zero API fees.
- **Hierarchical Agent Flow:** Uses a centralized Manager agent to autonomously analyze user goals, delegate scripts to a Coder agent, and route the output to a Quality Auditor agent for testing and verification.
- **Dynamic Browser Interface:** Features a clean, visual Streamlit dashboard to prompt your agent team on the fly instead of hardcoding workflows.
- **Automated Dependency Sandbox:** The portable runner script automatically scans, verifies, and force-installs missing Python dependencies (`crewai`, `streamlit`, `langchain_openai`) into whichever host machine it plugs into.

## 📂 Project Architecture & USB Layout
To maintain complete hardware portability, all model weights, execution engines, launcher batches, and source scripts are kept next to each other in the root workspace folder:

📁 USB_Drive:/AI_Workspace/
 
  ├── 📄 1_launch_ai_server.bat      # Double-click FIRST (Initializes the LLM Server)
  
  ├── 📄 2_run_agents.bat            # Double-click SECOND (Verifies dependencies & boots UI)
  
  ├── ⚙️ llamafile-0.10.6.exe        # Mozilla llamafile local server engine
  
  ├── 🧠 qwen3-4b-thinking-2507...   # Local reasoning GGUF model weights
  
  └── 🐍 usb_agent_manager.py        # Streamlit UI & CrewAI framework orchestration

