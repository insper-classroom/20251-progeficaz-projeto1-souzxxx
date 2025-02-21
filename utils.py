import json

def load_data(filename):
    filepath = f"static/data/{filename}"
    with open(filepath, "r") as file:
        data = json.load(file)
    return data

def load_template(filename):
    with open(f"static/templates/{filename}", "r") as file:
        template = file.read()
    return template


def add_note_to_file(data, filename):
    filepath = f"static/data/{filename}"
    with open(filepath, "w") as file:
        json.dump(data, file)

