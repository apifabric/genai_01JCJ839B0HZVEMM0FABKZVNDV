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
    """
    description: Table to store hotel branches
    """
    __tablename__ = 'hotel'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)
    contact_number = Column(String(15), nullable=False)


class Room(Base):
    """
    description: Table to store rooms available in the hotel
    """
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_id = Column(Integer, ForeignKey('hotel.id'), nullable=False)
    number = Column(String(10), nullable=False)
    type = Column(String(50), nullable=False)
    price_per_night = Column(Integer, nullable=False)


class Guest(Base):
    """
    description: Table to store guest information
    """
    __tablename__ = 'guest'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone_number = Column(String(15), nullable=False)
    email = Column(String(100), nullable=True)



class Reservation(Base):
    """
    description: Table to store reservation details
    """
    __tablename__ = 'reservation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    guest_id = Column(Integer, ForeignKey('guest.id'), nullable=False)
    room_id = Column(Integer, ForeignKey('room.id'), nullable=False)
    check_in_date = Column(Date, nullable=False)
    check_out_date = Column(Date, nullable=False)
    total_amount = Column(Integer, nullable=False)



class Service(Base):
    """
    description: Table to store services offered by the hotel
    """
    __tablename__ = 'service'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)



class ReservationService(Base):
    """
    description: Table to link reservations with services
    """
    __tablename__ = 'reservation_service'

    id = Column(Integer, primary_key=True, autoincrement=True)
    reservation_id = Column(Integer, ForeignKey('reservation.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('service.id'), nullable=False)


class Employee(Base):
    """
    description: Table to store employee information in the hotel
    """
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_id = Column(Integer, ForeignKey('hotel.id'), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    role = Column(String(50), nullable=False)
    salary = Column(Integer, nullable=False)


class MaintenanceRequest(Base):
    """
    description: Table to store maintenance requests for rooms
    """
    __tablename__ = 'maintenance_request'

    id = Column(Integer, primary_key=True, autoincrement=True)
    room_id = Column(Integer, ForeignKey('room.id'), nullable=False)
    description = Column(String(200), nullable=False)
    status = Column(String(50), nullable=False)
    request_date = Column(Date, nullable=False)


class Payment(Base):
    """
    description: Table to store payment details for reservations
    """
    __tablename__ = 'payment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    reservation_id = Column(Integer, ForeignKey('reservation.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    method = Column(String(50), nullable=False)


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

# Test Data for `Hotel` class
hotel1 = Hotel(name='Grand Plaza', address='123 Main St, Cityville', contact_number='123-456-7890')
hotel2 = Hotel(name='Sunny Inn', address='456 Beach Rd, Sunnyvale', contact_number='123-456-7891')
hotel3 = Hotel(name='Mountain Retreat', address='789 Hilltop Ave, Mountainview', contact_number='123-456-7892')
hotel4 = Hotel(name='Urban Suite', address='101 City St, Metropolis', contact_number='123-456-7893')

# Test Data for `Room` class
room1 = Room(hotel_id=1, number='101', type='Suite', price_per_night=200)
room2 = Room(hotel_id=1, number='102', type='Single', price_per_night=120)
room3 = Room(hotel_id=2, number='105', type='Suite', price_per_night=220)
room4 = Room(hotel_id=3, number='201', type='Double', price_per_night=150)

# Test Data for `Guest` class
guest1 = Guest(first_name='John', last_name='Doe', phone_number='555-1234', email='john@example.com')
guest2 = Guest(first_name='Jane', last_name='Smith', phone_number='555-5678', email='jane@example.com')
guest3 = Guest(first_name='Sam', last_name='Wright', phone_number='555-8765', email='sam@example.com')
guest4 = Guest(first_name='Alex', last_name='Brown', phone_number='555-4321', email='alex@example.com')

# Test Data for `Reservation` class
reservation1 = Reservation(guest_id=1, room_id=1, check_in_date=date(2024, 1, 10), check_out_date=date(2024, 1, 15), total_amount=1000)
reservation2 = Reservation(guest_id=2, room_id=2, check_in_date=date(2024, 2, 1), check_out_date=date(2024, 2, 3), total_amount=240)
reservation3 = Reservation(guest_id=3, room_id=3, check_in_date=date(2024, 3, 5), check_out_date=date(2024, 3, 10), total_amount=1100)
reservation4 = Reservation(guest_id=4, room_id=4, check_in_date=date(2024, 4, 15), check_out_date=date(2024, 4, 18), total_amount=450)

# Test Data for `Service` class
service1 = Service(name='Room Service', price=50)
service2 = Service(name='Massage', price=80)
service3 = Service(name='Laundry', price=30)
service4 = Service(name='Breakfast', price=25)

# Test Data for `ReservationService` class
reservation_service1 = ReservationService(reservation_id=1, service_id=1)
reservation_service2 = ReservationService(reservation_id=2, service_id=2)
reservation_service3 = ReservationService(reservation_id=3, service_id=3)
reservation_service4 = ReservationService(reservation_id=4, service_id=4)

# Test Data for `Employee` class
employee1 = Employee(hotel_id=1, first_name='Michael', last_name='Scott', role='Manager', salary=50000)
employee2 = Employee(hotel_id=2, first_name='Jim', last_name='Halpert', role='Receptionist', salary=30000)
employee3 = Employee(hotel_id=3, first_name='Pam', last_name='Beesly', role='Designer', salary=35000)
employee4 = Employee(hotel_id=4, first_name='Dwight', last_name='Schrute', role='Security', salary=32000)

# Test Data for `MaintenanceRequest` class
maintenance_request1 = MaintenanceRequest(room_id=1, description='Air conditioning repair', status='Pending', request_date=date(2024, 1, 12))
maintenance_request2 = MaintenanceRequest(room_id=2, description='Plumbing issue', status='Completed', request_date=date(2024, 1, 20))
maintenance_request3 = MaintenanceRequest(room_id=3, description='Wi-Fi connectivity problem', status='InProgress', request_date=date(2024, 2, 5))
maintenance_request4 = MaintenanceRequest(room_id=4, description='Room cleaning', status='Pending', request_date=date(2024, 3, 15))

# Test Data for `Payment` class
payment1 = Payment(reservation_id=1, amount=1000, date=date(2024, 1, 16), method='Credit Card')
payment2 = Payment(reservation_id=2, amount=240, date=date(2024, 2, 4), method='Cash')
payment3 = Payment(reservation_id=3, amount=1100, date=date(2024, 3, 11), method='Credit Card')
payment4 = Payment(reservation_id=4, amount=450, date=date(2024, 4, 19), method='Debit Card')


session.add_all([hotel1, hotel2, hotel3, hotel4, room1, room2, room3, room4, guest1, guest2, guest3, guest4, reservation1, reservation2, reservation3, reservation4, service1, service2, service3, service4, reservation_service1, reservation_service2, reservation_service3, reservation_service4, employee1, employee2, employee3, employee4, maintenance_request1, maintenance_request2, maintenance_request3, maintenance_request4, payment1, payment2, payment3, payment4])
session.commit()
