class Account:
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    @staticmethod
    def check_email(email):
        return '@' in email

    def confirm_password(self):
        pwd = input("Confirm password >> ")
        return pwd == self.password

    def change_password(self):
        new_pass = input("Insert new password >> ")
        self.password = new_pass

    def forgotten_password(self):
        forgot = ''
        forgot = input("Have you forgotten your password? Y (yes), N (no) >> ")
        if forgot == 'Y':
            self.change_password()
        else:
            pass

# Create account
name = input("Insert your name >> ")
surname = input("Insert surname >> ")
email = input("Insert email >> ")
password = input("Insert password >> ")

a1 = Account(name, surname, email, password)

if not a1.check_email(email):
    print("Email is incorrect :(")
else:
    print("Email is correct :)")

a1.forgotten_password()
