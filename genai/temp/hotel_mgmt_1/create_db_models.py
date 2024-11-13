# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


class Hotel(Base):
    """description: Stores information about hotels."""
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    star_rating = Column(Integer, nullable=False)
    total_room_count = Column(Integer)  # For storing the sum of all hotel's room count


class Room(Base):
    """description: Represents individual rooms within hotels."""
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_id = Column(Integer, ForeignKey('hotels.id'), nullable=False)
    room_number = Column(String, nullable=False)
    room_type = Column(String, nullable=False)
    price = Column(DECIMAL, nullable=False)
    status = Column(String, nullable=False)  # e.g., available, occupied


class Guest(Base):
    """description: Details for guests staying at the hotel."""
    __tablename__ = 'guests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String)
    email = Column(String)
    booking_count = Column(Integer)  # For storing count of bookings by the guest



class Booking(Base):
    """description: Information about room bookings by guests."""
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=False)
    guest_id = Column(Integer, ForeignKey('guests.id'), nullable=False)
    check_in_date = Column(DateTime, nullable=False)
    check_out_date = Column(DateTime, nullable=False)
    total_cost = Column(DECIMAL)  # Sum of Room.price * duration of stay



class Amenity(Base):
    """description: Amenities available in hotels."""
    __tablename__ = 'amenities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # e.g., Wi-Fi, Pool
    description = Column(String)



class HotelAmenity(Base):
    """description: Junction table linking hotels with their available amenities."""
    __tablename__ = 'hotel_amenities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_id = Column(Integer, ForeignKey('hotels.id'), nullable=False)
    amenity_id = Column(Integer, ForeignKey('amenities.id'), nullable=False)



class Employee(Base):
    """description: Employees working at the hotel."""
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_id = Column(Integer, ForeignKey('hotels.id'), nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    position = Column(String, nullable=False)  # e.g., Manager, Housekeeping
    salary = Column(Integer, nullable=False)



class Service(Base):
    """description: Services provided within the hotel (e.g., cleaning, room service)."""
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    cost = Column(DECIMAL, nullable=False)



class ServiceLog(Base):
    """description: Log of services requested by guests."""
    __tablename__ = 'service_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    booking_id = Column(Integer, ForeignKey('bookings.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    date_requested = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)  # e.g., completed, pending



class Payment(Base):
    """description: Payments made by guests for bookings and services."""
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    guest_id = Column(Integer, ForeignKey('guests.id'), nullable=False)
    booking_id = Column(Integer, ForeignKey('bookings.id'))
    service_log_id = Column(Integer, ForeignKey('service_logs.id'))
    amount = Column(DECIMAL, nullable=False)
    payment_date = Column(DateTime, nullable=False)
    method = Column(String, nullable=False)  # e.g., credit card, cash



class Complaint(Base):
    """description: Complaints from guests regarding service or facilities."""
    __tablename__ = 'complaints'

    id = Column(Integer, primary_key=True, autoincrement=True)
    guest_id = Column(Integer, ForeignKey('guests.id'), nullable=False)
    booking_id = Column(Integer, ForeignKey('bookings.id'), nullable=False)
    date_filed = Column(DateTime, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, nullable=False)  # e.g., resolved, unresolved



class Maintenance(Base):
    """description: Records of maintenance activities for rooms and facilities."""
    __tablename__ = 'maintenance'

    id = Column(Integer, primary_key=True, autoincrement=True)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    date_scheduled = Column(DateTime, nullable=False)
    date_completed = Column(DateTime)
    description = Column(String, nullable=False)
    status = Column(String, nullable=False)  # e.g., completed, scheduled



# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

from datetime import date

# Hotel Test Data
hotel1 = Hotel(id=1, name="Grand Palace", address="123 King St", star_rating=5, total_room_count=10)
hotel2 = Hotel(id=2, name="Ocean View", address="456 Sea Rd", star_rating=4, total_room_count=15)
hotel3 = Hotel(id=3, name="Mountain Retreat", address="789 Hill Ln", star_rating=3, total_room_count=20)
hotel4 = Hotel(id=4, name="City Center", address="101 Urban Dr", star_rating=4, total_room_count=25)

# Room Test Data
room1 = Room(id=1, hotel_id=1, room_number="101", room_type="Deluxe", price=200, status="available")
room2 = Room(id=2, hotel_id=1, room_number="102", room_type="Standard", price=150, status="occupied")
room3 = Room(id=3, hotel_id=2, room_number="201", room_type="Suite", price=300, status="available")
room4 = Room(id=4, hotel_id=2, room_number="202", room_type="Single", price=100, status="occupied")

# Guest Test Data
guest1 = Guest(id=1, first_name="John", last_name="Doe", phone_number="123456789", email="johndoe@example.com", booking_count=2)
guest2 = Guest(id=2, first_name="Jane", last_name="Smith", phone_number="987654321", email="janesmith@example.com", booking_count=1)
guest3 = Guest(id=3, first_name="Jim", last_name="Beam", phone_number="234567890", email="jimbeam@example.com", booking_count=1)
guest4 = Guest(id=4, first_name="Jack", last_name="Daniel", phone_number="345678901", email="jackdaniel@example.com", booking_count=0)

# Booking Test Data
booking1 = Booking(id=1, room_id=1, guest_id=1, check_in_date=date(2023, 11, 1), check_out_date=date(2023, 11, 5), total_cost=800)
booking2 = Booking(id=2, room_id=2, guest_id=1, check_in_date=date(2023, 11, 6), check_out_date=date(2023, 11, 10), total_cost=600)
booking3 = Booking(id=3, room_id=3, guest_id=2, check_in_date=date(2023, 11, 3), check_out_date=date(2023, 11, 7), total_cost=1200)
booking4 = Booking(id=4, room_id=4, guest_id=3, check_in_date=date(2023, 11, 8), check_out_date=date(2023, 11, 12), total_cost=400)

# Amenity Test Data
amenity1 = Amenity(id=1, name="Wi-Fi", description="High-speed internet")
amenity2 = Amenity(id=2, name="Pool", description="Olympic-sized swimming pool")
amenity3 = Amenity(id=3, name="Gym", description="Fully equipped gym")
amenity4 = Amenity(id=4, name="Spa", description="Relaxing wellness spa")

# HotelAmenity Test Data
hotel_amenity1 = HotelAmenity(id=1, hotel_id=1, amenity_id=1)
hotel_amenity2 = HotelAmenity(id=2, hotel_id=1, amenity_id=2)
hotel_amenity3 = HotelAmenity(id=3, hotel_id=2, amenity_id=3)
hotel_amenity4 = HotelAmenity(id=4, hotel_id=3, amenity_id=4)

# Employee Test Data
employee1 = Employee(id=1, hotel_id=1, first_name="Alice", last_name="Johnson", position="Manager", salary=50000)
employee2 = Employee(id=2, hotel_id=1, first_name="Bob", last_name="Lee", position="Housekeeping", salary=30000)
employee3 = Employee(id=3, hotel_id=2, first_name="Charlie", last_name="Brown", position="Receptionist", salary=35000)
employee4 = Employee(id=4, hotel_id=3, first_name="Dana", last_name="White", position="Chef", salary=40000)

# Service Test Data
service1 = Service(id=1, name="Room Service", description="Deluxe menu available 24/7", cost=50)
service2 = Service(id=2, name="Laundry", description="Fast and reliable service", cost=20)
service3 = Service(id=3, name="Tour Guide", description="Explore local attractions", cost=100)
service4 = Service(id=4, name="Car Rental", description="Premium vehicles available", cost=150)

# ServiceLog Test Data
service_log1 = ServiceLog(id=1, booking_id=1, service_id=1, date_requested=date(2023, 11, 2), status="completed")
service_log2 = ServiceLog(id=2, booking_id=2, service_id=2, date_requested=date(2023, 11, 6), status="completed")
service_log3 = ServiceLog(id=3, booking_id=3, service_id=3, date_requested=date(2023, 11, 4), status="pending")
service_log4 = ServiceLog(id=4, booking_id=4, service_id=4, date_requested=date(2023, 11, 9), status="pending")

# Payment Test Data
payment1 = Payment(id=1, guest_id=1, booking_id=1, amount=800, payment_date=date(2023, 11, 1), method="credit card")
payment2 = Payment(id=2, guest_id=1, booking_id=2, amount=600, payment_date=date(2023, 11, 6), method="credit card")
payment3 = Payment(id=3, guest_id=2, booking_id=3, amount=1200, payment_date=date(2023, 11, 3), method="cash")
payment4 = Payment(id=4, guest_id=3, booking_id=4, amount=400, payment_date=date(2023, 11, 8), method="cash")

# Complaint Test Data
complaint1 = Complaint(id=1, guest_id=1, booking_id=1, date_filed=date(2023, 11, 2), description="Aircon not working", status="resolved")
complaint2 = Complaint(id=2, guest_id=2, booking_id=3, date_filed=date(2023, 11, 4), description="Room service delay", status="unresolved")
complaint3 = Complaint(id=3, guest_id=3, booking_id=4, date_filed=date(2023, 11, 9), description="Shower not draining", status="resolved")
complaint4 = Complaint(id=4, guest_id=4, booking_id=2, date_filed=date(2023, 11, 7), description="TV remote missing", status="unresolved")

# Maintenance Test Data
maintenance1 = Maintenance(id=1, room_id=1, date_scheduled=date(2023, 11, 1), date_completed=date(2023, 11, 2), description="Monthly aircon maintenance", status="completed")
maintenance2 = Maintenance(id=2, room_id=2, date_scheduled=date(2023, 11, 2), date_completed=date(2023, 11, 3), description="Shower repair", status="completed")
maintenance3 = Maintenance(id=3, room_id=3, date_scheduled=date(2023, 11, 10), description="Re-carpeting", status="scheduled")
maintenance4 = Maintenance(id=4, room_id=4, date_scheduled=date(2023, 11, 11), description="Wi-Fi upgrade", status="scheduled")


session.add_all([hotel1, hotel2, hotel3, hotel4, room1, room2, room3, room4, guest1, guest2, guest3, guest4, booking1, booking2, booking3, booking4, amenity1, amenity2, amenity3, amenity4, hotel_amenity1, hotel_amenity2, hotel_amenity3, hotel_amenity4, employee1, employee2, employee3, employee4, service1, service2, service3, service4, service_log1, service_log2, service_log3, service_log4, payment1, payment2, payment3, payment4, complaint1, complaint2, complaint3, complaint4, maintenance1, maintenance2, maintenance3, maintenance4])
session.commit()
