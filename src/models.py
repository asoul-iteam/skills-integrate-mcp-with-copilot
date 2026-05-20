"""Database models for activities and users"""

from sqlalchemy import Column, Integer, String, ForeignKey, Table, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Association table for many-to-many relationship between activities and participants
activity_participants = Table(
    'activity_participants',
    Base.metadata,
    Column('activity_id', Integer, ForeignKey('activities.id'), primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True)
)

class User(Base):
    """User model for students and teachers"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    grade_level = Column(String, nullable=True)
    is_teacher = Column(Boolean, default=False)
    
    # Relationship
    activities = relationship(
        "Activity",
        secondary=activity_participants,
        back_populates="participants"
    )

class Activity(Base):
    """Activity model for extracurricular activities"""
    __tablename__ = "activities"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    schedule = Column(String)
    max_participants = Column(Integer)
    
    # Relationship
    participants = relationship(
        "User",
        secondary=activity_participants,
        back_populates="activities"
    )
