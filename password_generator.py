import random
import string

class RandomPasswordGenerator:
    def __init__(self, x):
        self.x = x
        self.n = int(input("Enter the length of the password you want to generate: "))

        # Call the right method based on what type of password the user chose
        if self.x == 1:
            self.password = self.str_only()          # Only letters
        elif self.x == 2:
            self.password = self.integer_only()      # Only numbers
        elif self.x == 3:
            self.password = self.mixed_pass()        # Letters + numbers + symbols
        else:
            self.password = None                     # In case the choice is invalid

    def mixed_pass(self):
        print("Just to confirm, you want a mixed password of length", self.n, "? (Y/N)")
        cont = input()
        if cont == 'Y':
            # All the characters we want to include in a mixed password
            punctuation = "!@#$%^&*()-_=+[{]}|\\;:'\",<>.?/"
            characters = string.ascii_letters + string.digits + punctuation

            # Generate a random password from those characters
            temp = ''.join(random.choices(characters, k=self.n))

            # Make sure it includes at least one digit
            if not any(char.isdigit() for char in temp):
                temp = self.integer_only(0, temp)

            # Make sure it includes at least one letter
            if not any(char.isalpha() for char in temp):
                temp = self.str_only(0, temp)

            return temp
        else:
            return None  # If user says no, don’t generate anything

    def integer_only(self, n=1, temp=""):
        if n == 0:
            # This part is only called to *add* a number to an existing password (like mixed)
            index = random.randint(0, len(temp))
            temp = temp[:index] + random.choice(string.digits) + temp[index:]
            return temp
        else:
            # Normal case: user chose a numbers-only password
            print("Just to confirm, you want a number-only password of length", self.n, "? (Y/N)")
            cont = input()
            if cont == "Y":
                return ''.join(random.choices(string.digits, k=self.n))
            else:
                return None

    def str_only(self, n=1, temp=""):
        if n == 0:
            # This part is only called to *add* a letter to an existing password (like mixed)
            index = random.randint(0, len(temp))
            temp = temp[:index] + random.choice(string.ascii_letters) + temp[index:]
            return temp
        else:
            # Normal case: user chose a letters-only password
            print("Just to confirm, you want a letter-only password of length", self.n, "? (Y/N)")
            cont = input()
            if cont == "Y":
                return ''.join(random.choices(string.ascii_letters, k=self.n))
            else:
                return None


# Main program
x = 0
print("Hello! 👋 Welcome to the Random Password Generator.")

# Keep running until the user decides to exit
while x != 4:
    print("\nWhat type of password would you like to generate?")
    print("1. Letters only (A-Z, a-z)")
    print("2. Numbers only (0-9)")
    print("3. Mixed (letters + numbers + symbols)")
    print("4. Exit")

    x = int(input("Enter your choice (1/2/3/4): "))

    if x == 4:
        print("Thanks for using the password generator. See you next time! 👋")
        break

    # Create a password based on the user's choice
    passw = RandomPasswordGenerator(x)
    if passw.password:
        print("Here's your password:", passw.password)
    else:
        print("No password was generated.")
