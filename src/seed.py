"""Seed script to populate the database with sample data"""

from database import SessionLocal, init_db
from models import Activity, User

def seed_database():
    """Initialize database and populate with sample data"""
    # Initialize database tables
    init_db()
    
    db = SessionLocal()
    
    # Check if data already exists
    if db.query(Activity).first() is not None:
        print("Database already contains data. Skipping seed.")
        db.close()
        return
    
    # Create sample users (students)
    students = [
        User(email="michael@mergington.edu", name="Michael", grade_level="10"),
        User(email="daniel@mergington.edu", name="Daniel", grade_level="11"),
        User(email="emma@mergington.edu", name="Emma", grade_level="9"),
        User(email="sophia@mergington.edu", name="Sophia", grade_level="10"),
        User(email="john@mergington.edu", name="John", grade_level="11"),
        User(email="olivia@mergington.edu", name="Olivia", grade_level="9"),
        User(email="liam@mergington.edu", name="Liam", grade_level="10"),
        User(email="noah@mergington.edu", name="Noah", grade_level="11"),
        User(email="ava@mergington.edu", name="Ava", grade_level="9"),
        User(email="mia@mergington.edu", name="Mia", grade_level="10"),
        User(email="amelia@mergington.edu", name="Amelia", grade_level="11"),
        User(email="harper@mergington.edu", name="Harper", grade_level="9"),
        User(email="ella@mergington.edu", name="Ella", grade_level="10"),
        User(email="scarlett@mergington.edu", name="Scarlett", grade_level="11"),
        User(email="james@mergington.edu", name="James", grade_level="9"),
        User(email="benjamin@mergington.edu", name="Benjamin", grade_level="10"),
        User(email="charlotte@mergington.edu", name="Charlotte", grade_level="11"),
        User(email="henry@mergington.edu", name="Henry", grade_level="9"),
    ]
    
    db.add_all(students)
    db.commit()
    
    # Create activities with initial participants
    activities_data = [
        {
            "name": "Chess Club",
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        {
            "name": "Programming Class",
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        {
            "name": "Gym Class",
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        {
            "name": "Soccer Team",
            "description": "Join the school soccer team and compete in matches",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 22,
            "participants": ["liam@mergington.edu", "noah@mergington.edu"]
        },
        {
            "name": "Basketball Team",
            "description": "Practice and play basketball with the school team",
            "schedule": "Wednesdays and Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 15,
            "participants": ["ava@mergington.edu", "mia@mergington.edu"]
        },
        {
            "name": "Art Club",
            "description": "Explore your creativity through painting and drawing",
            "schedule": "Thursdays, 3:30 PM - 5:00 PM",
            "max_participants": 15,
            "participants": ["amelia@mergington.edu", "harper@mergington.edu"]
        },
        {
            "name": "Drama Club",
            "description": "Act, direct, and produce plays and performances",
            "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
            "max_participants": 20,
            "participants": ["ella@mergington.edu", "scarlett@mergington.edu"]
        },
        {
            "name": "Math Club",
            "description": "Solve challenging problems and participate in math competitions",
            "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
            "max_participants": 10,
            "participants": ["james@mergington.edu", "benjamin@mergington.edu"]
        },
        {
            "name": "Debate Team",
            "description": "Develop public speaking and argumentation skills",
            "schedule": "Fridays, 4:00 PM - 5:30 PM",
            "max_participants": 12,
            "participants": ["charlotte@mergington.edu", "henry@mergington.edu"]
        }
    ]
    
    for activity_data in activities_data:
        participant_emails = activity_data.pop("participants", [])
        
        activity = Activity(**activity_data)
        
        # Add participants
        for email in participant_emails:
            user = db.query(User).filter(User.email == email).first()
            if user:
                activity.participants.append(user)
        
        db.add(activity)
    
    db.commit()
    db.close()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()
