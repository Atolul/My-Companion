from pathlib import Path
import json

PROJECT_DIR = Path(__file__).parent.parent
DATA_FILE = PROJECT_DIR / "data" / "data.json"

def load_data():
    if not DATA_FILE.exists():
        return{
            "projects": [],
            "todos": [],
            "settings": {}
        }
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    DATA_FILE.parent.mkdir(exist_ok=True)

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


        