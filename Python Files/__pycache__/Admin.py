from Doctor import Doctor
from Patient import Patient




class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = '', discharged_patients=None):
        self.__username = username
        self.__password = password
        self.address = address
        self.discharged_patients = discharged_patients

    doctors_list = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]


    def login(self) :
          
        print("-----Login-----")
        #Get the details of the admin

        entered_username = input('Enter the username: ')
        entered_password = input('Enter the password: ')

        # check if the username and password match the registered ones
        if entered_username == self.__username and entered_password == self.__password:
            print('Login successful!')
            return True
        else:
            print('Incorrect username or password.')
            return False

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
       print("-----Doctor Setup-----")
       print()
       print("Please enter the details necessary.")
       first_name = input("First Name: ")
       surname = input("Surname: ")
       speciality = input("Speciality: ")
       
       return f"{first_name} {surname} {speciality}"
       
       
       
    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op = input("Please select the menu you wish to enter: ")
 
        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print("Enter the doctor's details:")
            print()
            first_name = input("Please enter the name of the doctor you wish to register: ")
            print()
            surname = input("Please enter the surname of the doctor that you wish to register: ")
            print()
            speciality = input("Please enter the speciality of the doctor that you wish to register: ")
    
            
            
            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    break
                
            else:
                new_doctor = Doctor(first_name, surname, speciality)
                doctors.append(new_doctor)
                print()
                print("New doctor succesfully registered.")


        # View
        elif op == '2':
            print("-----List of Doctors-----")
            if not doctors:
                print("No doctors currently registered.")
            else:
                for index, doctor in enumerate(doctors, start=1):
                    print()
                 
                    print(f'{index} {doctor.full_name()} - {doctor.get_speciality()}')
                    print()

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view_doctors(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1. First name')
            print(' 2. Surname')
            print(' 3. Speciality')
            UpdateOP = int(input('Input: '))

            if UpdateOP == 1:
                update_firstname = input("Please enter the NEW FORENAME for the doctor you are changing: ")
                doctors[doctor_index].set_first_name(update_firstname)
                print(f"The doctor's name has been changed to: {update_firstname}")
                
            if UpdateOP == 2:
                update_surname = input("Please enter the NEW SURNAME for the doctor you are changing: ")
                doctors[doctor_index].set_surname(update_surname)
                print(f"The doctor's name has been changed to: {update_surname}")
                
            if UpdateOP == 3:
                update_speciality = input("Please enter the NEW SPECIALITY for the doctor you are changing: ")
                doctors[doctor_index].set_speciality(update_speciality)
                print(f"The doctor's name has been changed to: {update_speciality}")
                
        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view_doctors(doctors)
            try:
                doctor_index = int(input('Enter the ID of the doctor to be deleted: '))-1
                if 0 <= doctor_index < len(doctors):
                    deleteConfirmation = input(f"Are your SURE you want to delete {doctors[doctor_index].full_name()}? (Y/N): ")
                    
                    if deleteConfirmation == "Y" or "y":
                        del doctors[doctor_index]
                    else:
                        print(f"Deletion of {doctors[doctor_index].full_name()} ABORTED!")
                else:
                    print("The ID that was entered is not correct.")
            except ValueError:
                print("Invalid Input! Please ensure to write a VALID ID number!")

    def view_patient(self, patients):
        grouped_patients = self.group_patients_by_family(patients)

        for family_name, family_patients in grouped_patients.items():
            print(f'Family: {family_name}')
            for i, patient in enumerate(family_patients, start=1):
                print(f"{i:<3} |  {patient.full_name():<25} | {patient.get_doctor().full_name() if patient.get_doctor() else 'None':<28} | {patient.get_age():^4} | {patient.get_mobile():^14} | {patient.get_postcode():^9} | {''.join(patient.print_symptoms()) if patient.print_symptoms() else 'None':<20}")

    def write_patient_info_to_file(self, patients, file_path):
        with open(file_path, 'w') as file:
            grouped_patients = self.group_patients_by_family(patients)

            for family_name, family_patients in grouped_patients.items():
                file.write(f'Family: {family_name}\n')
                file.write('ID | Full Name                 | Doctor\'s Full Name        | Age | Mobile         | Postcode     | Symptoms\n')
                for i, patient in enumerate(family_patients, start=1):
                    file.write(f"{i:<3} | {patient.full_name():<25} | {patient.get_doctor().full_name() if patient.get_doctor() else 'None':<28} | {patient.get_age():^4} | {patient.get_mobile():^14} | {patient.get_postcode():^9} | {''.join(patient.print_symptoms()) if patient.print_symptoms() else 'None':<20}\n")

        print(f"Patient information has been written to {file_path}")

    
    def view_doctors(self, doctors):
        print("View Doctors:")
        print()
        print('ID |          Full Name           |      Speciality       ')
        for i, doctor in enumerate(doctors, start=1):
            print(i, f'  |  {doctor.full_name()}  |  {doctor.get_speciality()}')


    def group_patients_by_family(self, patients):
        grouped_patients = {}
        for patient in patients:
            family_name = patient.get_surname()
            if family_name not in grouped_patients:
                grouped_patients[family_name] = []

            grouped_patients[family_name].append(patient)

        return grouped_patients


    def assign_doctor_to_patient(self, patients, doctors):
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode   |   Symptoms ')
        self.view_patient(patients)
              
        try:
            # patient_index is the patient ID minus one (-1)
            patient_index = int(input('Enter the ID of the patient: ')) - 1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return  # stop the procedures
    
            symptoms_add = input("Enter the patient's symptom(s): ")
            patients[patient_index].symptom_new(symptoms_add)

            print("-----Doctors Select-----")
            print('Select the doctor that fits these symptoms:')
            patients[patient_index].print_symptoms()  # print the patient symptoms

            print('--------------------------------------------------')
            print('ID |          Full Name           |  Speciality   ')
            self.view_doctors(doctors)  # Make sure 'doctors' is a list, not a class

            doctor_index = int(input('Please enter the doctor ID: ')) - 1

            if 0 <= doctor_index < len(doctors):
                patients[patient_index].assign_doctor_to_patients(doctors[doctor_index])
                print(f"Assignment of {doctors[doctor_index].full_name()} to {patients[patient_index].full_name()} was successful.")
            else:
                print("Invalid ID")

        except ValueError:
            print("Invalid ID")



    def view_grouped_patients(self, grouped_patients):
        for family_name, family_patients in grouped_patients.items():
            print(f'Family: {family_name}')
            for i, patient in enumerate(family_patients, start=1):
                print(f'  {i}. {patient.full_name()} - {patient.get_doctor().full_name() if patient.get_doctor() else "None"}')


    def discharge(self, patients, discharge_patients):
        print("-----Discharge Patient-----")
        self.view_patient(patients)
        try:
            patient_index = int(input('Enter the ID of the patient to be discharged: ')) -1
            
            if 0 <= patient_index < len(patients):
                patient_to_discharge = patients[patient_index]
                discharge_Confirmation = input(f"Are your SURE you want to discharge {patients[patient_index].full_name()}? (Y/N): ")
                    
                if discharge_Confirmation.lower() == "y":

                    discharge_patients.append(patient_to_discharge)
                else:
                    print(f"Discharge of {patients[patient_index].full_name()} ABORTED!")
            else:
                print("The ID that was entered is not correct.")

        except ValueError:
            print("Invalid Input! Please ensure to write a VALID ID number!")

        return patients, discharge_patients
        

    def view_discharge(self, discharged_patients):


        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        for i, patient in enumerate(discharged_patients, start=1):
            print(f"{i}. {patient.full_name()} {patient.get_doctor()} {patient.get_age()} {patient.get_mobile()} {patient.get_postcode()}")
        else:
            print("No discharged patients")


    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
           new_username = input('Enter the new username: ')
           # validate the password
           if new_username == input('Enter the new username again: '):
               self.__username = new_username
           else:
            print("")
            print("Username re-verification failed! Username unchanged!")


        elif op == 2:
           new_password = input('Enter the new password: ')
            # validate the password
           if new_password == input('Enter the new password again: '):
                self.__password = new_password
           else:
                print("")
                print("Password re-verification failed! Password unchanged!")

        elif op == 3:
            new_address = input('Enter the new address: ')
            # validate the address
            if new_address == input('Re-enter the new address: '):
                self.address = new_address
                print("Address updated successfully!")
            else:
                print("")
                print("Address re-verification failed! Address unchanged!")

           

        else:
            print()
            print("Invalid input!")
            print()
            Admin.update_details()

