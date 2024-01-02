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
    