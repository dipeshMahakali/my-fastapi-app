Using uv as your package manager is the modern way to build FastAPI applications in 2026. It replaces pip, venv, and pip-tools with a single, blazingly fast tool written in Rust.

Here is the updated guide to setting up FastAPI using uv.

1. Project Initialization
Instead of manually creating folders and virtual environments, uv handles the scaffolding for you.

Bash

# Initialize a new FastAPI project
uv init --app my-fastapi-app
cd my-fastapi-app
This command creates a pyproject.toml (your recipe) and a .python-version file to ensure consistency across different machines.

2. Add Dependencies
With uv, you don't need to manually activate a virtual environment to install things. uv will manage the .venv folder automatically.

Bash

# Add FastAPI with standard production dependencies
uv add "fastapi[standard]"
Note: The [standard] extra includes uvicorn (the server) and fastapi-cli.
Server Start Command: uv run fastapi dev main.py

Task,Command
Add a dev tool (like pytest),uv add --dev pytest
Sync environment,uv sync
Update all packages,uv lock --upgrade
Run a one-off script,uv run script.py


Pro Tip: fastapi-new
If you want an even faster start with a professional structure (including folders for routers and schemas), you can use the official scaffolding tool:

Bash

uvx fastapi-new awesome-project
This uses uvx to run the generator without even needing to install it first.