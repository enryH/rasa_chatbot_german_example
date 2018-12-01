from rasa_nlu.training_data import load_data

data = load_data("data/data.json")

with open("data/data.md", "w", encoding="utf8") as f:
    f.write(data.as_markdown())