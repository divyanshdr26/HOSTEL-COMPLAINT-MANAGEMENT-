# Hostel Complaint Management System

A simple terminal-based Python project for recording, searching, updating, and reporting hostel complaints.

## Features

- Submit a hostel complaint
- View all complaints
- Search by complaint ID, student name, or room number
- Update complaint status
- Delete a complaint
- View simple complaint statistics
- Stores data locally in `data/complaints.txt`

## Complaint Categories

1. Electrical
2. Water
3. Food
4. Wi-Fi
5. Cleaning
6. Furniture

## Requirements

- Python 3.x
- No external Python packages are required.

## How to Run

Open the project folder in VS Code.

Open the VS Code terminal and run:

```bash
python main.py
```

If `python` is not recognized on Windows, try:

```bash
py main.py
```

## Testing the Project

Run the program and test each menu option:

1. Submit a complaint.
2. View complaints.
3. Search for the complaint.
4. Change its status.
5. View the report.
6. Delete the complaint.

All data is stored locally in:

```text
data/complaints.txt
```

The file is automatically updated whenever a complaint is added, changed, or deleted.

## Automated Tests

Run:

```bash
python -m unittest discover tests -v
```
