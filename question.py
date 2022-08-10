class department:
    def __init__(self,dept_name,designation,staff_id):
        self.__dept_name=dept_name
        self.__staff_id=staff_id
        self.__designation=designation
    def get_dept_name(self):
        return self.__dept_name
    def get_staff_id(self):
        return self.__staff_id
    def get_designation(self):
        return self.__designation
    def update_staff_details(self,prom_designation):
        self.__designation=prom_designation
        self.__dept_name="CSE"

class college:
    def __init__(self,location,dept_list):
        self.location=location
        self.__dept_list=dept_list
    def get_dept_list(self):
        return self.__dept_list
    def display(self):
        for  dept in self.__dept_list:
            print(dept.get_dept_name(),dept.get_designation(),dept.get_staff_id())
dept1=department("CSE","Asst professor", 2001)
dept2=department("ISE","professor",2001)
colg=college("zone",[dept1,dept2])
dept2.update_staff_details("principal")
colg.display()