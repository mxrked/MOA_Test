from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import BLOB, Column, Table, Integer, String, VARCHAR, Date, Time, ForeignKey, Numeric, NVARCHAR, Float, NCHAR

Base = declarative_base()

class TempUser(Base):
    __tablename__ = "hold 5_Users"

    User_ID = Column(Integer, primary_key=True, nullable=False)
    Employee_ID = Column(Integer, ForeignKey("Employee.EmployeeID"))
    User_Name = Column(NCHAR(10), nullable=False)
    Email_Address = Column(VARCHAR(), nullable=False)
    Password = Column(VARCHAR(), nullable=False)
