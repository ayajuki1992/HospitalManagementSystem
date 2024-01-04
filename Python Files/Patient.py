class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode):
        self.__patient_firstname = first_name
        self.__patient_surname = surname
        self.__patient_age = age
        self.__patient_mobile = mobile
        self.__patient_postcode = postcode
        self.__doctor = 'None'
        self.__symptoms = []

    
    def full_name(self) :
        return f"{self.__patient_firstname} {self.__patient_surname}"       
     
    def get_doctor(self) :
       return self.__doctor
   
    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        return self.__symptoms

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
    
    def get_first_name(self) :
        return self.__first_name

    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name
      
    def get_surname(self) :
        return self.__surname

    def set_surname(self, new_surname):
        self.__surname = new_surname

    def get_age(self) :
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age
        
    def get_mobile(self) :
        return self.__patient_mobile
    
    def set_mobile(self,new_mobile):
        self.__patient_mobile = new_mobile
        
    def get_postcode(self) :
        return self.__patient_postcode
    
    def set_mobile(self,new_postcode):
        self.__patient_postcode = new_postcode