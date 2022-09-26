
class Contact:

    def __init__(self, first_name, last_name, telephone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.telephone_number = telephone_number

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    #dont know if the insertion of contact should go in here or in the dbconnection class, or a
    #totally different class?