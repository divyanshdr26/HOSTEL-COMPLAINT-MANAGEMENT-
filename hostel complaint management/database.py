from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "complaints.txt"


def load_complaints():
    if not DATA_FILE.exists():
        DATA_FILE.parent.mkdir(exist_ok=True)
        DATA_FILE.touch()
        return []

    complaints = []

    with DATA_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split("|", 5)
            if len(parts) != 6:
                continue

            complaint_id, student, room, category, status, description = parts

            complaints.append({
                "id": complaint_id,
                "student": student,
                "room": room,
                "category": category,
                "status": status,
                "description": description,
            })

    return complaints


def save_complaints(complaints):
    DATA_FILE.parent.mkdir(exist_ok=True)

    with DATA_FILE.open("w", encoding="utf-8") as file:
        for item in complaints:
            description = item["description"].replace("|", "/").replace("\n", " ")
            file.write(
                f"{item['id']}|{item['student']}|{item['room']}|"
                f"{item['category']}|{item['status']}|{description}\n"
            )
