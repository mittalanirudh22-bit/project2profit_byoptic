import json
import os

DB_FILE = "projects.json"

def load_projects():
    if not os.path.exists(DB_FILE):
        return []

    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_project(project):
    data = load_projects()
    data.append(project)

    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)