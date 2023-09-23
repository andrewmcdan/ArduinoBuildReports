import os
import pathlib
import sys

if len(sys.argv) != 3:
    print("Usage: python update_readme.py <project name> <workflow url>")
    sys.exit(1)
else:
    project_name = sys.argv[1]
    workflow_url = sys.argv[2]

# Get the current directory
current_dir = pathlib.Path(__file__).parent.absolute()
readme_file = os.path.join(current_dir, "README.md")

# Read the README.md file
with open(readme_file, "r+") as f:
    lines = f.readlines()
    found = false
    for i, line in enumerate(lines):
        if line.startswith("[//]: # (" + project_name + ")"):
            found = true
            break
    if not found:
        # Add the project name and workflow url to the README.md file
        lines.append("[//]: # (" + project_name + ")\n")
        lines.append("[![Build Status of Last Commit](" + workflow_url + "/badge.svg)](" + workflow_url + ")\n\n")
