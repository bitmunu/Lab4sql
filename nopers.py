import datetime as dt

# Импортируем из библитеки SqlAlchemy нужные функции и классы
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, CheckConstraint
from sqlalchemy import Integer, String, Boolean, DateTime, Numeric, SmallInteger

# Импортируем из подмодуля ORM функции и классы, предназначенные для
# высокоуровневой работы с базой данных посредством построения объектной модели ORM
# (ORM ~ object-relational model)
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker


# Так просто надо сделать
class Basis(DeclarativeBase):
    pass


class Employee(Basis):
    __tablename__ = "employees"
    employee_id = Column(Integer(), primary_key=True)
    first_name = Column(String(150))
    last_name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False, unique=True, index=True)
    phone_number = Column(String(150))
    hire_date = Column(String(150), default=None, nullable=False)
    job_id = Column(String(150), ForeignKey('jobs.job_id'), nullable=False, index=True)
    salary = Column(Numeric(), unique=True, index=True)
    commission_pct = Column(Numeric(), nullable=True, index=True)
    manager_id = Column(Integer(), nullable=True)
    department_id = Column(Integer(), ForeignKey('departments.department_id'), nullable=True)


    jobs = relationship("Jobs", back_populates="employees", )
    departments = relationship("Department", back_populates="employees", )


    def __str__(self):
        return f"<{self.employee_id}> {self.first_name} {self.last_name} {self.email}@mail.ru"

    def __repr__(self):
        return (f"{self.email}@mail.ru {self.first_name} {self.last_name}; "
                f"{self.departments.__repr__()}; "
                f"{self.jobs.__repr__()} ")


class Department(Basis):
    __tablename__ = "departments"
    department_id = Column(Integer(), primary_key=True)
    department_name = Column(String(100), nullable=False)
    manager_id = Column(Integer())
    location_id = Column(Integer(), ForeignKey('locations.location_id'))

    employees = relationship("Employee", back_populates="departments")
    locations = relationship("Location", back_populates="departments")


    def __str__(self):
        return f"<{self.department_id}>: {self.department_name} "

    def __repr__(self):
        return f"{self.department_name} id({self.department_id}): {self.locations.__str__()}"


class Location(Basis):
    __tablename__ = "locations"
    location_id = Column(Integer(), primary_key=True)
    street_address = Column(String(150))
    postal_code = Column(String(150))
    city = Column(String(150), nullable=False)
    state_province= Column(String(150))
    country_id=Column(String(50))

    departments = relationship("Department", back_populates="locations")

    def __str__(self):
        return (f"<{self.location_id}>: {self.street_address}, {self.postal_code}, {self.city}, {self.state_province}, "
                f"{self.country_id}")

    def __repr__(self):
        return f"{self.country_id} id({self.location_id})"

class JobHistory(Basis):
    __tablename__ = "job_history"
    employee_id = Column(Integer(), nullable=False, primary_key=True)
    start_date=Column(String(150), nullable=False)
    end_date=Column(String(150), nullable=False)
    job_id = Column(String(150), ForeignKey('jobs.job_id'), nullable=False)
    department_id=Column(Integer(), default=None)

    jobs = relationship("Jobs", back_populates="job_history")

    def __repr__(self):
        return f"{self.start_date} - {self.end_date}"


class Jobs(Basis):
    __tablename__ = "jobs"
    job_id = Column(String(150), primary_key=True)
    job_title=Column(String(150), nullable=False)
    min_salary=Column(Integer())
    max_salary=Column(Integer())

    employees = relationship("Employee", back_populates="jobs")
    job_history = relationship("JobHistory", back_populates="jobs")

    def __str__(self):
        return f"<{self.job_id}>: {self.job_title}"

    def __repr__(self):
        return (f"{self.job_title} id({self.job_id}): з/п от {self.min_salary} до {self.max_salary}; "
                f"{self.job_history.__repr__()} ")


class Countries(Basis):
    __tablename__ = "countries"
    country_id = Column(String(100), primary_key=True)
    country_name = Column(String(100), nullable=False)
    region_id = Column(Integer(), ForeignKey('regions.region_id'))

    regions = relationship("Regions", back_populates="countries")


    def __str__(self):
        return f"{self.country_id}: {self.country_name}"

    def __repr__(self):
        return f"{self.country_name} id({self.country_id})"


class Regions(Basis):
    __tablename__ = "regions"
    region_id = Column(Integer(), primary_key=True)
    region_name = Column(String(100), unique=True, nullable=False)

    countries = relationship("Countries", back_populates="regions")

    def __str__(self):
        return f"{self.region_id}: {self.region_name}"

    def __repr__(self):
        return f"{self.region_name} ({self.region_id})"



engine = create_engine("sqlite:///MyDatabase/Staff.db?echo=True", pool_pre_ping=True)

Basis.metadata.create_all(engine)

factory = sessionmaker(bind=engine)


