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
 
  ├── 📄 mutpleAI.bat      # Double-click FIRST (Initializes the LLM Server)
  
  ├── 📄 2_run_agents.bat            # Double-click SECOND (Verifies dependencies & boots UI)
  
  ├── ⚙️ llamafile-0.10.6.exe        # Mozilla llamafile local server engine
  
  ├── 🧠 qwen3-4b-thinking-2507...   # Local reasoning GGUF model weights (model)
  
  └── 🐍 usb_agent_manager.py        # Streamlit UI & CrewAI framework orchestration

## Food for thought to simplfly this project.
This process uses llamafile which is available at https://github.com/mozilla-ai/llamafile.
The model I used is qwen3-4b-thinking-2507.Q4_K_M.gguf however any model will work that can fit in the selected device.
This project was designed to be portable and offline so the requirements is what can hold your selected model and the scripts.
These scripts were written in notepad for ease of use. The scripts are then saved as .bat or .py. The llamafile is saved as .exe to make it able to run.
To change model just replace the model name in the mutpleAI.bat and 2_run_agents.bat to run a different model. To find models visit huggingface.com to find a model right for you.

---

## 🛠️ Setup Instructions (First Time Setup)

Follow these steps to prepare your workspace drive. Because the environment is configured to self-install its framework layers, setting it up on a new machine takes less than two minutes:

1. **Install Python:** Ensure the computer you plug your drive into has **Python 3.10, 3.11, or 3.12** installed (make sure to check the box that says *"Add Python to PATH"* during installation).
2. **Download Files:** Place your `llamafile-0.10.6.exe` engine and your `qwen3-4b-thinking-2507.Q4_K_M.gguf` weights inside your main USB folder alongside the batch files.
3. **Configure Code Paths:** Open `usb_agent_manager.py` in a text editor and ensure the `USB_DRIVE_PATH` variable matches your current USB drive letter (e.g., `D:/AI_Workspace`).

---

## 🚀 How to Operate Your AI Workforce

Running a multi-agent assignment is handled via a simple two-window loop:

### Step 1: Fire up the AI Brain
Double-click **`mutpleAI.bat`**. 
* This launches your local server engine with dedicated security mapping flags so your agents can communicate safely.
* Keep this black terminal window open in the background! It acts as the engine room.

### Step 2: Launch the Team Dashboard
Once your server completes initialization, double-click **`2_run_agents.bat`**.
* The script will run an environmental check. If it's a brand new computer, it will automatically download `crewai`, `streamlit`, and `langchain-openai` in the background.
* After 5 seconds, a new tab will automatically pop open in your default web browser at `http://localhost:8501`.

### Step 3: Run your First Mission
1. Type a comprehensive mission goal into the text field on your screen.
   * *Example:* `"Write a Python script called logger.py that monitors system uptime and stores reports directly to my USB drive workspace folder."`
2. Click the **🚀 Launch Agent Team** button.
3. Do not click the Streamlit "Deploy" button—your workspace runs 100% locally.
4. Monitor the logs inside your second terminal window to watch the manager delegate tasks to workers. Once finished, a confirmation summary will populate directly on your webpage layout!
