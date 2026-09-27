from collections import Counter
from database import load_complaints


def show_report():
    complaints = load_complaints()

    print("\n--- Complaint Report ---")

    if not complaints:
        print("No complaints available.")
        return

    status_counts = Counter(item["status"] for item in complaints)
    category_counts = Counter(item["category"] for item in complaints)

    print(f"Total complaints: {len(complaints)}")

    print("\nStatus-wise:")
    for status in ["Pending", "In Progress", "Resolved"]:
        print(f"{status}: {status_counts.get(status, 0)}")

    print("\nCategory-wise:")
    for category, count in sorted(category_counts.items()):
        print(f"{category}: {count}")
