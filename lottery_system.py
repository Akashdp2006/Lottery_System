import random

# Store players and tickets
players = []
tickets = []
winning_numbers = []
results = []

# 1. REGISTER PLAYER

def register_player():
    print("\n--- Register Player ---")

    name = input("Enter your name: ")

    if name.strip() == "":
        print("Name cannot be empty!")
        return

    player_id = len(players) + 1

    player = {
        "id": player_id,
        "name": name}
    
    players.append(player)
    print("Player registered successfully!")
    print("Your Player ID is:", player_id)



# 2. BUY LOTTERY TICKET

def buy_ticket():
    print("\n--- Buy Lottery Ticket ---")

    if len(players) == 0:
        print("Please register a player first.")
        return
    print("\nRegistered Players:")
    for player in players:
        print(player["id"], "-", player["name"])
    try:
        player_id = int(input("Enter your Player ID: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    selected_player = None

    for player in players:
        if player["id"] == player_id:
            selected_player = player
            break
    if selected_player is None:
        print("Player not found!")
        return

    # Generate 6 unique numbers from 1 to 50
    numbers = sorted(random.sample(range(1, 51), 6))

    ticket_id = len(tickets) + 1
    ticket = {
        "ticket_id": ticket_id,
        "player_id": player_id,
        "player_name": selected_player["name"],
        "numbers": numbers}
    

    tickets.append(ticket)
    print("\nTicket generated successfully!")
    print("Ticket ID:", ticket_id)
    print("Your Numbers:", numbers)


# 3. CONDUCT LOTTERY DRAW

def conduct_draw():
    global winning_numbers
    global results
    print("\n--- Lottery Draw ---")
    if len(tickets) == 0:
        print("No tickets available.")
        return

    # Generate winning numbers
    winning_numbers = sorted(random.sample(range(1, 51), 6))

    results = []

    print("\nWinning Numbers:", winning_numbers)

    # Check every ticket
    for ticket in tickets:
        matched_numbers = set(ticket["numbers"]) & set(winning_numbers)
        matches = len(matched_numbers)
        # Calculate prize
        if matches == 6:
            prize = 10000
        elif matches == 5:
            prize = 5000
        elif matches == 4:
            prize = 1000
        elif matches == 3:
            prize = 100
        else:
            prize = 0

        result = {
            "ticket_id": ticket["ticket_id"],
            "player_name": ticket["player_name"],
            "matches": matches,
            "prize": prize}
        
        results.append(result)

    print("\nLottery draw completed!")



# 4. VIEW RESULTS

def show_results():
    print("\n--- Lottery Results ---")
    if len(results) == 0:
        print("No results available.")
        print("Please conduct the lottery draw first.")
        return

    print("\nWinning Numbers:", winning_numbers)
    print("\n================================")
    print("          RESULTS")
    print("================================")
    for result in results:
        print("\nPlayer:", result["player_name"])
        print("Ticket ID:", result["ticket_id"])
        print("Numbers Matched:", result["matches"])
        print("Prize: ₹", result["prize"])
        if result["prize"] > 0:
            print("Congratulations! You won!")
        else:
            print("Better luck next time!")



# 5. VIEW ALL TICKETS

def view_tickets():
    print("\n--- All Tickets ---")

    if len(tickets) == 0:
        print("No tickets available.")
        return

    for ticket in tickets:
        print("\nTicket ID:", ticket["ticket_id"])
        print("Player:", ticket["player_name"])
        print("Numbers:", ticket["numbers"])



# MAIN PROGRAM

def main():
    while True:
        print("\n")
        print("================================")
        print("       LUCKYDRAW LOTTERY")
        print("================================")
        print("1. Register Player")
        print("2. Buy Lottery Ticket")
        print("3. Conduct Lottery Draw")
        print("4. View Results")
        print("5. View All Tickets")
        print("6. Exit")
        print("================================")
        choice = input("Enter your choice: ")
        if choice == "1":
            register_player()
        elif choice == "2":
            buy_ticket()
        elif choice == "3":
            conduct_draw()
        elif choice == "4":
            show_results()
        elif choice == "5":
            view_tickets()
        elif choice == "6":
            print("\nThank you for using LuckyDraw!")
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice!")
            print("Please select 1 to 6.")


# Start the program
if __name__ == "__main__":
    main()
