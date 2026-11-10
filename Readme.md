# IT Support Ticket Manager

A command-line Python application for creating, managing, searching, and tracking IT support tickets.

## Project Overview

The IT Support Ticket Manager simulates a basic IT help desk ticketing system. It allows users to record computer problems, assign priorities, track ticket statuses, and manage saved tickets.

This project was developed as a practical Python learning and portfolio project.

## Features

- Create new support tickets.
- Automatically assign unique ticket IDs.
- View all saved tickets.
- Search tickets by ID.
- Search tickets by username.
- Update ticket statuses.
- Filter high-priority tickets.
- Delete tickets with confirmation.
- Validate user input.
- Save tickets to a local text file.
- Load saved tickets when the application starts.
- Handle corrupted ticket data without stopping the application.

## Technologies Used

- Python 3
- `ast` module
- `os` module
- File handling
- Command-line interface (CLI)

## Python Concepts Demonstrated

- Variables and data types
- Dictionaries and lists
- Conditional statements
- Loops
- Functions
- User input and validation
- Exception handling
- File handling
- Reading and writing data
- Data persistence
- Code reusability

## How to Run

1. Install Python 3.
2. Download or clone this project.
3. Open a terminal in the project folder.
4. Run:

```bash
python ticket_manager.py
```

5. Follow the menu instructions.

## Data Storage

Tickets are stored locally in `tickets.txt`.

The application loads saved tickets when it starts and saves changes when tickets are created, updated, or deleted.

## Testing

The application was manually tested for:

- Creating and viewing tickets.
- Searching for existing and nonexistent tickets.
- Updating ticket statuses.
- Filtering high-priority tickets.
- Deleting tickets with confirmation.
- Searching by username.
- Invalid menu choices and ticket IDs.
- Empty input validation.
- Loading saved tickets.
- Handling corrupted ticket data.

All tested features worked without errors.

## Project Purpose

This project demonstrates practical beginner-level Python programming, problem-solving, debugging, and application development skills.

**Status:** Completed
