import random

from nopers import *
c = random.randint(400, 500)
def add_employee(id):
        e1 = Employee(employee_id=id,
                      first_name="Kill",
                      last_name="La Kill",
                      email="thor",
                      phone_number="8999191921921",
                      hire_date="05.02.1992",
                      job_id="ST_CLERK",
                      salary=9000,
                      commission_pct=None,
                      manager_id=103,
                      department_id=10)
        session.add(e1)
        print(e1.__repr__())

session = factory()
add_employee(c)
#session.add(e1)
session.commit()

