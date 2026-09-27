# Project Statement – Hostel Complaint Management System

## Problem Statement

Hostel students may face common problems such as electrical faults, water supply issues, food quality problems, Wi-Fi failures, cleaning issues, and damaged furniture. A simple complaint management system can keep these complaints organized and make their status easy to track.

## Scope

The project provides a small command-line system for:

- Storing hostel complaints in a local text file.
- Adding new complaints.
- Viewing all complaints.
- Searching complaints by ID, student name, or room number.
- Updating complaint status.
- Deleting complaints.
- Displaying basic complaint statistics.

The project intentionally uses a local `.txt` file instead of an external database or online service.

## Target Users

- Hostel students who need to report problems.
- Hostel staff or administrators who need to review and update complaints.

## High-Level Features

- Menu-driven terminal interface.
- Six complaint categories: Electrical, Water, Food, Wi-Fi, Cleaning, and Furniture.
- Automatic complaint ID generation.
- Complaint status tracking.
- Local persistent storage using `data/complaints.txt`.
- Search and basic reporting functionality.
