#############################
#  Database Setting
#############################
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///sample.db', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

#############################
#  Model
#############################
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))

Base.metadata.create_all(engine)

#############################
#  CRUD Create
#############################
User1 = User(name='Joe',age=21,grade='First')
User2 = User(name='Dan',age=25,grade='Second')
User3 = User(name='Gene',age=28,grade='Fifth')

# session.add(User1)
session.add_all([User1,User2,User3])

session.commit()

#############################
# CRUD Read
#############################
Users = session.query(User)

for User in Users:
    print(User.name,User.age,User.grade)