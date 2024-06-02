from nopers import *
session = factory()

u = session.query(Employee).where(Employee.last_name == "King").first()

dp1 = Department()
dp1.department_id = 695
dp1.department_name = "CatsFightingArmor"
dp1.manager_id = 103
dp1.location_id = 1800
#session.add(dp1)

j = Jobs()
j.job_id = "SHA_MAN"
j.job_title = "shaman"
j.min_salary = "5000"
j.max_salary = "100000"
#session.add(j)

jh1=JobHistory()
jh1.department_id=dp1.department_id
jh1.employee_id=u.employee_id
jh1.start_date = "00.22.63"
jh1.end_date = "11.22.63"
jh1.job_id = "SHA_MAN"
#session.add(jh1)

c2 = session.query(Location).where(Location.street_address == "2011 Interiors Blvd").first()
dp1.location_id = c2.location_id
u.department_id = dp1.department_id
u.job_id = jh1.job_id

session.commit()
print(u.__repr__())

