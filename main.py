import Contact
import DatabaseConnection


def main():
    db = DatabaseConnection.DatabaseConnection("contact_list")
    db.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
    ContactID  INTEGER PRIMARY KEY,
    FirstName  varchar(255),
    LastName   varchar(255),
    Telephone  varchar(20)
    )
    ''')

    while True:

        first_name = input("Please Enter First Name: ")
        if first_name == "quit": break
        last_name = input("Please Enter Last Name: ")
        if last_name == "quit": break
        telephone = input("Please Enter Telephone Number: ")
        if telephone == "quit": break
        db.insert(Contact.Contact(first_name, last_name, telephone))
        print("Successfully Inserted")
        continue


if __name__ == "__main__":
    main()
