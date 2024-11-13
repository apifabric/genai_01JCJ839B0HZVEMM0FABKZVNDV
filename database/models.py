# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 13, 2024 07:53:08
# Database: sqlite:////tmp/tmp.enARiJpH6t-01JCJ839B0HZVEMM0FABKZVNDV/hotel_mgmt/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Guest(SAFRSBaseX, Base):
    """
    description: Table to store guest information
    """
    __tablename__ = 'guest'
    _s_collection_name = 'Guest'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone_number = Column(String(15), nullable=False)
    email = Column(String(100))

    # parent relationships (access parent)

    # child relationships (access children)
    ReservationList : Mapped[List["Reservation"]] = relationship(back_populates="guest")



class Hotel(SAFRSBaseX, Base):
    """
    description: Table to store hotel branches
    """
    __tablename__ = 'hotel'
    _s_collection_name = 'Hotel'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)
    contact_number = Column(String(15), nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    EmployeeList : Mapped[List["Employee"]] = relationship(back_populates="hotel")
    RoomList : Mapped[List["Room"]] = relationship(back_populates="hotel")



class Service(SAFRSBaseX, Base):
    """
    description: Table to store services offered by the hotel
    """
    __tablename__ = 'service'
    _s_collection_name = 'Service'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    ReservationServiceList : Mapped[List["ReservationService"]] = relationship(back_populates="service")



class Employee(SAFRSBaseX, Base):
    """
    description: Table to store employee information in the hotel
    """
    __tablename__ = 'employee'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    hotel_id = Column(ForeignKey('hotel.id'), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    role = Column(String(50), nullable=False)
    salary = Column(Integer, nullable=False)

    # parent relationships (access parent)
    hotel : Mapped["Hotel"] = relationship(back_populates=("EmployeeList"))

    # child relationships (access children)



class Room(SAFRSBaseX, Base):
    """
    description: Table to store rooms available in the hotel
    """
    __tablename__ = 'room'
    _s_collection_name = 'Room'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    hotel_id = Column(ForeignKey('hotel.id'), nullable=False)
    number = Column(String(10), nullable=False)
    type = Column(String(50), nullable=False)
    price_per_night = Column(Integer, nullable=False)

    # parent relationships (access parent)
    hotel : Mapped["Hotel"] = relationship(back_populates=("RoomList"))

    # child relationships (access children)
    MaintenanceRequestList : Mapped[List["MaintenanceRequest"]] = relationship(back_populates="room")
    ReservationList : Mapped[List["Reservation"]] = relationship(back_populates="room")



class MaintenanceRequest(SAFRSBaseX, Base):
    """
    description: Table to store maintenance requests for rooms
    """
    __tablename__ = 'maintenance_request'
    _s_collection_name = 'MaintenanceRequest'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    room_id = Column(ForeignKey('room.id'), nullable=False)
    description = Column(String(200), nullable=False)
    status = Column(String(50), nullable=False)
    request_date = Column(Date, nullable=False)

    # parent relationships (access parent)
    room : Mapped["Room"] = relationship(back_populates=("MaintenanceRequestList"))

    # child relationships (access children)



class Reservation(SAFRSBaseX, Base):
    """
    description: Table to store reservation details
    """
    __tablename__ = 'reservation'
    _s_collection_name = 'Reservation'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    guest_id = Column(ForeignKey('guest.id'), nullable=False)
    room_id = Column(ForeignKey('room.id'), nullable=False)
    check_in_date = Column(Date, nullable=False)
    check_out_date = Column(Date, nullable=False)
    total_amount = Column(Integer, nullable=False)

    # parent relationships (access parent)
    guest : Mapped["Guest"] = relationship(back_populates=("ReservationList"))
    room : Mapped["Room"] = relationship(back_populates=("ReservationList"))

    # child relationships (access children)
    PaymentList : Mapped[List["Payment"]] = relationship(back_populates="reservation")
    ReservationServiceList : Mapped[List["ReservationService"]] = relationship(back_populates="reservation")



class Payment(SAFRSBaseX, Base):
    """
    description: Table to store payment details for reservations
    """
    __tablename__ = 'payment'
    _s_collection_name = 'Payment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    reservation_id = Column(ForeignKey('reservation.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    method = Column(String(50), nullable=False)

    # parent relationships (access parent)
    reservation : Mapped["Reservation"] = relationship(back_populates=("PaymentList"))

    # child relationships (access children)



class ReservationService(SAFRSBaseX, Base):
    """
    description: Table to link reservations with services
    """
    __tablename__ = 'reservation_service'
    _s_collection_name = 'ReservationService'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    reservation_id = Column(ForeignKey('reservation.id'), nullable=False)
    service_id = Column(ForeignKey('service.id'), nullable=False)

    # parent relationships (access parent)
    reservation : Mapped["Reservation"] = relationship(back_populates=("ReservationServiceList"))
    service : Mapped["Service"] = relationship(back_populates=("ReservationServiceList"))

    # child relationships (access children)
