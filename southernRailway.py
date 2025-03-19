import datetime

print("🚆 WELCOME TO SOUTHERN RAILWAYS 🚆\n")
today_date = datetime.datetime.now().strftime("%d-%m-%Y")
print(f"📅 Today's Date: {today_date}")

DESTINATIONS = {"Chennai": 450, "Madurai": 380, "Coimbatore": 420, "Trichy": 260}
booked_tickets = {}  # Dictionary to store tickets temporarily (resets on restart)

# Ticket booking
def book_ticket():
    name = input("Enter passenger name: ").strip()
    destination = input(f"Choose destination {list(DESTINATIONS.keys())}: ").strip()

    if destination not in DESTINATIONS:
        print("❌ Invalid destination!")
        return

    try:
        num_tickets = int(input("Enter number of tickets (1-5): "))
        if num_tickets < 1 or num_tickets > 5:
            raise ValueError("You can book up to 5 tickets.")
    except ValueError as e:
        print(f"❌ {e}")
        return

    pnr = f"PNR{len(booked_tickets) + 1001}"
    total_price = DESTINATIONS[destination] * num_tickets
    print(f"💰 Total Price: {total_price} (Pay via E-Wallet)")

    # Simulated Payment
    wallet_balance = 2000  
    if total_price > wallet_balance:
        print("❌ Insufficient wallet balance!")
        return
    wallet_balance -= total_price
    print(f"✅ Payment Successful! Remaining Wallet Balance: {wallet_balance}")

    booked_tickets[pnr] = {"Name": name, "Destination": destination, "Tickets": num_tickets, "Total Price": total_price}
    print(f"🎟️ Ticket Booked! PNR: {pnr}")

# View booked tickets
def view_tickets():
    if not booked_tickets:
        print("📭 No tickets booked yet!")
        return
    for pnr, details in booked_tickets.items():
        print(f"\nPNR: {pnr} | Name: {details['Name']} | Destination: {details['Destination']} | Tickets: {details['Tickets']} | Price: {details['Total Price']}")

# Cancel a ticket
def cancel_ticket():
    pnr = input("Enter PNR to cancel: ").strip()
    if pnr in booked_tickets:
        del booked_tickets[pnr]
        print(f"🚫 Ticket with PNR {pnr} cancelled!")
    else:
        print("❌ Invalid PNR!")

# PNR Status Check
def check_pnr():
    pnr = input("Enter PNR to check: ").strip()
    if pnr in booked_tickets:
        print(f"✅ Ticket Found: {booked_tickets[pnr]}")
    else:
        print("❌ No ticket found for this PNR.")

# Main menu
def main():
    while True:
        print("\n📌 Choose Service: 1. Book Ticket 2. View Tickets 3. Cancel Ticket 4. PNR Status 5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            book_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            cancel_ticket()
        elif choice == "4":
            check_pnr()
        elif choice == "5":
            print("👋 Thank you for using Southern Railways!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()