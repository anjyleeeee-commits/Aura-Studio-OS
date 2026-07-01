from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent

DATABASE = {
    "characters": [],
    "locations": [],
    "cameras": [],
    "emotions": [],
    "actions": []
}

print("=" * 50)
print("Aura Studio Engine Builder v0.3")
print("=" * 50)

for folder, data in DATABASE.items():

    path = ROOT / "data" / folder
    path.mkdir(parents=True, exist_ok=True)

    file = path / f"{folder}.json"

    if not file.exists():

        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print("[CREATE]", file.relative_to(ROOT))

    else:

        print("[SKIP]  ", file.relative_to(ROOT))

print("\nBuild Complete")