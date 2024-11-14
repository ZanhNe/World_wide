from app.extentions.extentions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, Numeric, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from typing import Optional, List
from datetime import datetime


class Location(db.Model):
    __tablename__ = 'location'
    location_id: Mapped[int] = mapped_column('location_id', primary_key=True, autoincrement=True)
    location_name: Mapped[str] = mapped_column('location_name', String(255), nullable=False)
    address : Mapped[Optional[str]] = mapped_column('address', String(500), nullable=True)
    latitude: Mapped[float] = mapped_column('latitude', Numeric(18, 16), nullable=False)
    longitude: Mapped[float] = mapped_column('longitude', Numeric(19, 16), nullable=False)

    country_id: Mapped[int] = mapped_column('country_id', ForeignKey('country.country_id'), nullable=False)
    country: Mapped['Country'] = relationship(back_populates='locations', lazy=True)

    users: Mapped[List['Trip']] = relationship(back_populates='location', lazy=True)

    


class Country(db.Model):
    __tablename__ = 'country'
    country_id: Mapped[int] = mapped_column('country_id', primary_key=True, autoincrement=True)
    country_name: Mapped[str] = mapped_column('country_name', String(255), nullable=False, unique=True)
    emoji: Mapped[str] = mapped_column('emoji', LONGTEXT(charset='utf8mb4', collation='utf8mb4_unicode_ci'), nullable=False)

    locations: Mapped[List['Location']] = relationship(back_populates='country', lazy=True)

class Trip(db.Model):
    __tablename__ = 'trip'
    trip_id: Mapped[int] = mapped_column('trip_id', primary_key=True, autoincrement=True)
    note: Mapped[Optional[str]] = mapped_column('note', LONGTEXT(charset='utf8mb4', collation='utf8mb4_unicode_ci'), nullable=True)
    tripped_date: Mapped[DateTime] = mapped_column('tripped_date', DateTime(timezone=True), default=datetime.now(), nullable=False)

    location_id: Mapped[int] = mapped_column('location_id', ForeignKey('location.location_id'), nullable=False)
    location: Mapped['Location'] = relationship(back_populates='users', lazy=True)
    
    user_id: Mapped[int] = mapped_column('user_id', ForeignKey('user.user_id'), nullable=False)
    user: Mapped['User'] = relationship(back_populates='locations', lazy=True)


class User(db.Model):
    __tablename__ = 'user'
    user_id: Mapped[int] = mapped_column('user_id', primary_key=True, autoincrement=True)
    user_name: Mapped[str] = mapped_column('user_name', String(500), nullable=False)
    account_name: Mapped[str] = mapped_column('account_name', String(500), nullable=False, unique=True)
    password: Mapped[str] = mapped_column('password', String(1000), nullable=False)
    avatar: Mapped[Optional[str]] = mapped_column('avatar', String(300), nullable=True)
    created_date: Mapped[DateTime] = mapped_column('created_date', DateTime(timezone=True), default=datetime.now())
    
    locations: Mapped[List['Trip']] = relationship(back_populates='user', lazy=True)




