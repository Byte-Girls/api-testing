import json
import os

def load_schema_resource(filename):
    schema_dir = os.path.join(os.path.dirname(__file__), "..", "resources", "schemas")
    schema_path = os.path.join(schema_dir, filename)
    
    with open(schema_path, "r", encoding="utf-8") as f:
        return json.load(f)