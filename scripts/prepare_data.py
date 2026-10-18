import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

SOURCE_FILE = DATA_DIR / "the-office.json"
OUTPUT_FILE = DATA_DIR / "input.txt"

SEASON = (1,2,3,4,5)

def clean_text(text):
    """Remove stage directions and extra whitespace."""

    # Remove text inside square brackets, e.g. [laughs]
    text = re.sub(r"\[.*?\]", "", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()

def extract_conversations(episodes):
    """Extract Season 2 scenes featuring Michael Scott."""

    conversations = []

    for episode in episodes:
        if int(episode["season"]) not in SEASON:
            continue

        for scene in episode.get("scenes", []):

            has_michael = any(
                entry.get("character", "").strip().lower() == "michael"
                for entry in scene
            )

            if not has_michael:
                continue

            dialogue = []

            for entry in scene:

                character = entry.get("character", "").strip()
                line = clean_text(entry.get("line", ""))

                if character and line:
                    dialogue.append(f"{character}:\n{line}")

            if dialogue:
                conversations.append("\n\n".join(dialogue))

    return conversations

def prepare_dataset():

    # Load JSON dataset
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        episodes = json.load(f)

    # Extract conversations
    conversations = extract_conversations(episodes)

    if not conversations:
        raise ValueError(
            "No conversations found. Check the JSON structure "
            "and season number."
        )

    # Combine all conversations into a single corpus
    corpus = "\n\n\n".join(conversations) + "\n"

    # Write input.txt
    OUTPUT_FILE.write_text(corpus, encoding="utf-8")

    # Dataset statistics
    print("Dataset prepared successfully!")
    print(f"Season: {SEASON}")
    print(f"Total scenes: {len(conversations)}")
    print(f"Total characters: {len(corpus):,}")
    print(f"Vocabulary size: {len(set(corpus))}")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    prepare_dataset()