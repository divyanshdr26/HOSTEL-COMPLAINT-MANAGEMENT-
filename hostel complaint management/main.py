from complaints import (
    add_complaint,
    view_complaints,
    search_complaint,
    update_complaint_status,
    delete_complaint,
)
from reports import show_report


def print_menu():
    print("\n===== Hostel Complaint Management System =====")
    print("1. Submit Complaint")
    print("2. View Complaints")
    print("3. Search Complaint")
    print("4. Update Complaint Status")
    print("5. Delete Complaint")
    print("6. Complaint Report")
    print("7. Exit")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_complaint()
        elif choice == "2":
            view_complaints()
        elif choice == "3":
            search_complaint()
        elif choice == "4":
            update_complaint_status()
        elif choice == "5":
            delete_complaint()
        elif choice == "6":
            show_report()
        elif choice == "7":
            print("Thank you for using the Hostel Complaint Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
