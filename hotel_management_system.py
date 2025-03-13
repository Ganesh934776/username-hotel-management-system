from datetime import date

class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = True

    def book_room(self):
        if self.is_available:
            self.is_available = False
            print(f"Room {self.room_number} has been booked.")
        else:
            print(f"Room {self.room_number} is not available.")
    
    def check_out(self):
        self.is_available = True
        print(f"Room {self.room_number} has been checked out.")

class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.reservations = []

    def make_reservation(self, room, check_in_date, check_out_date):
        if room.is_available:
            room.book_room()
            reservation = Reservation(self, room, check_in_date, check_out_date)
            self.reservations.append(reservation)
            return reservation
        else:
            print(f"Sorry, the room {room.room_number} is not available.")
            return None

class Reservation:
    def __init__(self, customer, room, check_in_date, check_out_date):
        self.customer = customer
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.total_price = (self.check_out_date - self.check_in_date).days * self.room.price

    def get_reservation_details(self):
        return (f"Customer: {self.customer.name}\n"
                f"Room Number: {self.room.room_number}\n"
                f"Room Type: {self.room.room_type}\n"
                f"Check-In Date: {self.check_in_date}\n"
                f"Check-Out Date: {self.check_out_date}\n"
                f"Total Price: {self.total_price} USD")

class Hotel:
    def __init__(self, hotel_name):
        self.hotel_name = hotel_name
        self.rooms = []
        self.customers = []

    def add_room(self, room):
        self.rooms.append(room)
    
    def display_rooms(self):
        for room in self.rooms:
            availability = "Available" if room.is_available else "Not Available"
            print(f"Room {room.room_number}, Type: {room.room_type}, Price: {room.price}, Status: {availability}")
    
    def check_in_customer(self, customer, room_number, check_in_date, check_out_date):
        room = next((room for room in self.rooms if room.room_number == room_number), None)
        if room:
            customer.make_reservation(room, check_in_date, check_out_date)
            self.customers.append(customer)
        else:
            print("Room not found.")
            

# Create hotel
hotel = Hotel("Luxury Inn")

# Add rooms to the hotel
room1 = Room(101, "Single", 100)
room2 = Room(102, "Double", 150)
room3 = Room(103, "Suite", 300)

hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)

# Display all rooms
hotel.display_rooms()

# Create customers
customer1 = Customer("Alice", "123-456-789")
customer2 = Customer("Bob", "987-654-321")

# Customer 1 makes a reservation
check_in_date = date(2025, 3, 15)
check_out_date = date(2025, 3, 18)

reservation = customer1.make_reservation(room1, check_in_date, check_out_date)

if reservation:
    print("Reservation Details:")
    print(reservation.get_reservation_details())

# Display rooms again after booking
hotel.display_rooms()

# Customer 2 attempts to book the same room
reservation2 = customer2.make_reservation(room1, check_in_date, check_out_date)

# Display rooms after booking attempts
hotel.display_rooms()

# Customer 1 checks out
room1.check_out()
hotel.display_rooms()
