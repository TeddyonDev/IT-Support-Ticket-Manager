
import ast
import os

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
TICKET_FILE = os.path.join(BASE_FOLDER, "tickets.txt")
print("Reading ticket file:", TICKET_FILE)

tickets = []
ticket_id = 1

# LOAD SAVED TICKETS

print("\n=== LOADING SAVED TICKETS ===")
print("Reading file:", TICKET_FILE)

if os.path.exists(TICKET_FILE):

    with open(TICKET_FILE, "r") as file:

        for line_number, line in enumerate(file, start=1):

            try:
                ticket = ast.literal_eval(line.strip())

                if isinstance(ticket, dict):
                    tickets.append(ticket)
                    print(f"Ticket loaded from line {line_number}.")

                else:
                    print(f"Warning: Invalid ticket data on line {line_number}.")

            except (ValueError, SyntaxError):
                print(f"Warning: Corrupted ticket data on line {line_number}.")

else:
    print("No saved ticket file found.")

if tickets:
    ticket_id = max(ticket["id"] for ticket in tickets) + 1

print("Total tickets loaded:", len(tickets))
# SAVE TICKETS

def save_tickets():
    with open(TICKET_FILE, "w") as file:
        for ticket in tickets:
            file.write(str(ticket) + "\n")

def display_ticket(ticket):
    print("--------------------")
    print("ID:", ticket["id"])
    print("User:", ticket["user"])
    print("Problem:", ticket["problem"])
    print("Priority:", ticket["priority"])
    print("Status:", ticket["status"])
    print("--------------------")


# MAIN MENU

while True:

    print("\n=== IT SUPPORT TICKET MANAGER ===")
    print("1. Create ticket")
    print("2. View all tickets")
    print("3. Search ticket")
    print("4. Update ticket status")
    print("5. Show high-priority tickets")
    print("6. Delete ticket")
    print("7. Search tickets by username")
    print("8. Exit")

    choice = input("\nChoose an option: ")

    # CREATE TICKET

    if choice == "1":

        user = input("Enter your name: ").strip()

        while not user:
            print("Name cannot be empty!")
            user = input("Enter your name: ").strip()

        problem = input("Describe your computer problem: ").strip()

        while not problem:
            print("Problem description cannot be empty!")
            problem = input("Describe your computer problem: ").strip()

        priority = input("Enter priority (Low/Medium/High): ").strip().title()

        while priority not in ["Low", "Medium", "High"]:
            print("Invalid priority! Please try again.")
            priority = input("Enter priority (Low/Medium/High): ").strip().title()

        ticket = {
            "id": ticket_id,
            "user": user,
            "problem": problem,
            "priority": priority,
            "status": "Open"
        }

        tickets.append(ticket)
        ticket_id += 1

        save_tickets()

        print("\nTicket created successfully!")
        print(ticket)

    # VIEW ALL TICKETS

    elif choice == "2":

        print("\n=== ALL TICKETS ===")

        if not tickets:
            print("No tickets found.")
        else:
            for ticket in tickets:
                display_ticket(ticket)

    # SEARCH TICKET BY ID

    elif choice == "3":

        print("\n=== SEARCH TICKETS ===")

        try:
            search_id = int(input("Enter ticket ID to search: "))

            for ticket in tickets:
                if ticket["id"] == search_id:
                    print("\nTicket found!")
                    display_ticket(ticket)
                    break
            else:
                print("Ticket not found.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    # UPDATE TICKET STATUS

    elif choice == "4":

        print("\n=== UPDATE TICKET STATUS ===")

        try:
            update_id = int(input("Enter ticket ID to update: "))

            for ticket in tickets:
                if ticket["id"] == update_id:

                    new_status = input(
                        "Enter new status (Open/In Progress/Resolved): "
                    ).strip().title()

                    while new_status not in ["Open", "In Progress", "Resolved"]:
                        print("Invalid status!")
                        new_status = input(
                            "Enter new status (Open/In Progress/Resolved): "
                        ).strip().title()

                    ticket["status"] = new_status
                    save_tickets()

                    print("\nTicket status updated successfully!")
                    display_ticket(ticket)
                    break
            else:
                print("Ticket not found.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    # HIGH-PRIORITY TICKETS

    elif choice == "5":

        print("\n=== HIGH PRIORITY TICKETS ===")

        found = False

        for ticket in tickets:
            if ticket["priority"] == "High":
                found = True
                display_ticket(ticket)

        if not found:
            print("No high-priority tickets found.")

    
    # DELETE TICKET

    elif choice == "6":

        print("\n=== DELETE TICKET ===")

        try:
            delete_id = int(input("Enter ticket ID to delete: "))

            for ticket in tickets:
                if ticket["id"] == delete_id:

                    display_ticket(ticket)

                    confirmation = input(
                        "Are you sure you want to delete this ticket? (yes/no): "
                    ).strip().lower()

                    if confirmation == "yes":

                        tickets.remove(ticket)
                        save_tickets()

                        print("Ticket deleted successfully!")

                    else:
                        print("Deletion cancelled.")

                    break

            else:
                print("Ticket not found.")

        except ValueError:
            print("Invalid input! Please enter a number.")


    # SEARCH BY USERNAME

    elif choice == "7":

        print("\n=== SEARCH BY USERNAME ===")

        search_name = input("Enter username: ").strip()

        found = False

        for ticket in tickets:

            if ticket["user"].lower() == search_name.lower():

                found = True
                display_ticket(ticket)

        if not found:
            print("No tickets found for this user.")

    # EXIT

    elif choice == "8":

        print("Exiting Ticket Manager. Goodbye!")
        break

    else:
        print("Invalid option! Please choose 1-8.")
