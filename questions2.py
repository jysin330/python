class phone:
    # gym_plan_list=["personal",'group','crsfit','btcp']
    # gclassym_prc_list=['3500','4000','7800','9000']
    def __init_(self,phone_type,phone_cost):
        self.__phone_type=phone_type
        self.__phone_cost=phone_cost
        self.__total_cost=None
    def get_total_cost(self):
        return self.__total_cost
    def set_total_cost(self,value):
        self.__total_cost=value
    def calculate_total_cost(self,no_of_phones):
        self.__total_cost=no_of_phones*self.__phone_cost

class smartphone(phone):
    def __init_(self,phone_type,phone_cost,amenities_provided):
        super().__init__(phone_type,phone_cost)
        self.__amenities_provided=amenities_provided

    def calculate_total_cost(self,no_of_phones):
        super().calculate_total_cost(no_of_phones)
        for index in self.__amenities_provided:
            amenity=index.split(":")
            self.__total_cost=self.get_total_cost()+int(amenity[1])*int(amenity[2])
sp1=smartphone("smart",15000,["charger:1:800","ear-phones:1:1000"])
sp1.calculate_total_cost(1)
print(sp1.get_total_cost())