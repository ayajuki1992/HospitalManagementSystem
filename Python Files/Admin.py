from Doctor import Doctor


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
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
            print('Enter the doctor\'s details:')
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
                self.view(doctors)
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

            if UpdateOP == (1):
                update_firstname = input("Please enter the NEW FORENAME for the doctor you are changing: ")
                doctors[doctor_index].set_first_name(update_firstname)
                print(f"The doctor's name has been changed to: {update_firstname}")
                
            if UpdateOP == (2):
                update_surname = input("Please enter the NEW SURNAME for the doctor you are changing: ")
                doctors[doctor_index].set_surname(update_surname)
                print(f"The doctor's name has been changed to: {update_surname}")
                
            if UpdateOP == (3):
                update_speciality = input("Please enter the NEW SPECIALITY for the doctor you are changing: ")
                doctors[doctor_index].set_speciality(update_speciality)
                print(f"The doctor's name has been changed to: {update_speciality}")
                
        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)
            try:
                doctor_index = int(input('Enter the ID of the doctor to be deleted: '))
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
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Patients`s Full Name      | Age |    Mobile     | Postcode ')
        if not patients:
                print("No patients currently registered.")
        else:
            for index, patient in enumerate(patients, start=1):
                print(f'{index} {patient.full_name()} - {patient.get_age()}- {patient.get_mobile()} - {patient.get_postcode()}')

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    selected_patient = patients[patient_index]
                    selected_doctor = doctors[doctor_index]
                    
                
                    selected_patient.link(selected_doctor)
                    selected_doctor.add_patient(selected_patient)
               
                
                    print('The patient is now assigned to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")

        patient_index = input('Please enter the patient ID: ')

        #ToDo12
        pass

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo13
        pass

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
            #ToDo14
            pass

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password

        elif op == 3:
            #ToDo15
            pass

        else:
            #ToDo16
            pass

