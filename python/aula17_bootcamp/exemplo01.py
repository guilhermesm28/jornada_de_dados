from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///test.db"

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

try:
    # insert user
    with Session() as session:
        user = User(name="John Doe", email="john.doe@example.com", password="password")
        session.add(user)
        session.commit()
        print(f"user inserted: {user.name}")

    # retrieve user by email
    user = session.query(User).filter_by(email="john.doe@example.com").first()
    print(f"user retrieved: {user.name}")

except Exception as e:
    session.rollback()
    print(f"Error occurred: {e}")
finally:
    session.close()
