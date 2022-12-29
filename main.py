from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///sample.db', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))

Base.metadata.create_all(engine)

student1 = Student(name='Joe',age=21,grade='First')
student2 = Student(name='Dan',age=25,grade='Second')
student3 = Student(name='Gene',age=28,grade='Fifth')

# session.add(student1)
session.add_all([student1,student2,student3])

session.commit()

students = session.query(Student)

for student in students:
    print(student.name,student.age,student.grade)