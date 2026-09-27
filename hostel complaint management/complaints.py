from database import load_complaints, save_complaints
from validators import valid_category, valid_status


CATEGORIES = {
    "1": "Electrical",
    "2": "Water",
    "3": "Food",
    "4": "Wi-Fi",
    "5": "Cleaning",
    "6": "Furniture",
}

STATUSES = ["Pending", "In Progress", "Resolved"]


def next_id(complaints):
    if not complaints:
        return 1001
    return max(int(item["id"]) for item in complaints) + 1


def add_complaint():
    complaints = load_complaints()

    print("\n--- Submit Complaint ---")
    name = input("Enter student name: ").strip()
    room = input("Enter room number: ").strip()

    if not name or not room:
        print("Name and room number cannot be empty.")
        return

    print("\nComplaint Categories:")
    for key, value in CATEGORIES.items():
        print(f"{key}. {value}")

    category_choice = input("Enter category: ").strip()
    if not valid_category(category_choice, CATEGORIES):
        print("Invalid category.")
        return

    description = input("Enter complaint description: ").strip()
    if not description:
        print("Complaint description cannot be empty.")
        return

    complaint = {
        "id": str(next_id(complaints)),
        "student": name,
        "room": room,
        "category": CATEGORIES[category_choice],
        "description": description,
        "status": "Pending",
    }

    complaints.append(complaint)
    save_complaints(complaints)

    print(f"\nComplaint submitted successfully!")
    print(f"Complaint ID: {complaint['id']}")
    print(f"Status: {complaint['status']}")


def print_complaint(item):
    print(
        f"ID: {item['id']} | Student: {item['student']} | "
        f"Room: {item['room']} | Category: {item['category']} | "
        f"Status: {item['status']}"
    )
    print(f"Description: {item['description']}")
    print("-" * 80)


def view_complaints():
    complaints = load_complaints()
    print("\n--- All Complaints ---")

    if not complaints:
        print("No complaints found.")
        return

    for item in complaints:
        print_complaint(item)


def search_complaint():
    complaints = load_complaints()
    query = input("\nEnter complaint ID, student name, or room number: ").strip().lower()

    found = [
        item for item in complaints
        if query in item["id"].lower()
        or query in item["student"].lower()
        or query in item["room"].lower()
    ]

    if not found:
        print("No matching complaint found.")
        return

    for item in found:
        print_complaint(item)


def update_complaint_status():
    complaints = load_complaints()
    complaint_id = input("\nEnter complaint ID: ").strip()

    for item in complaints:
        if item["id"] == complaint_id:
            print("\n1. Pending")
            print("2. In Progress")
            print("3. Resolved")
            choice = input("Enter new status: ").strip()

            if choice not in {"1", "2", "3"}:
                print("Invalid status.")
                return

            item["status"] = STATUSES[int(choice) - 1]
            save_complaints(complaints)
            print("Complaint status updated successfully.")
            return

    print("Complaint ID not found.")


def delete_complaint():
    complaints = load_complaints()
    complaint_id = input("\nEnter complaint ID to delete: ").strip()

    updated = [item for item in complaints if item["id"] != complaint_id]

    if len(updated) == len(complaints):
        print("Complaint ID not found.")
        return

    save_complaints(updated)
    print("Complaint deleted successfully.")
