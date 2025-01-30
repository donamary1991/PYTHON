class Employee:
   company_name='Tata Elxsi '
   profession='Senior Engineer'
   def admission(self,id,fname,lname,age):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
   def print_value(self):
        print(self.id,self.fname,self.lname,self.age,Employee.company_name,Employee.profession)


emp1=Employee()
emp1.admission(1,'Nikhil','Sukhtar',26)
emp1.print_value()
emp1.admission(2,'Akhil','Singh',33)
emp1.print_value()
emp1.admission(3,'Jennu','Akki',30)
emp1.print_value()
emp1.admission(1,'Prathyaksha','Viren',28)
emp1.print_value()
emp1.admission(1,'Aakash','Bhaji',24)
emp1.print_value()
