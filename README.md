

###  Random Password Generator (Python CLI)

Welcome to the **Random Password Generator**, a simple and interactive Python-based tool that helps you generate secure passwords with ease. Whether you need a string-only password, digits-only, or a mix of everything (including special characters), this program has got you covered!

---

##  Features

- Generate passwords based on user preference:
  -  Only letters (both uppercase and lowercase)
  -  Only numbers (0–9)
  -  Mixed (letters + digits + special characters)
- Ensures at least one letter and digit in mixed passwords
- Interactive CLI experience with confirmation prompts
- Prevents empty or weak password generation

---

##  How It Works

1. The program greets the user and asks for the type of password they want to generate.
2. Based on the selection, it asks for the desired password length.
3. The password is generated and printed on screen.

---

##  Usage

### Run the program:
```bash
python random_password_generator.py
```

### You’ll be prompted with:
```
Hello, <Welcome to the random password generator>
What type of password would you like to Generate:
1. Only characters (Strings)
2. Numbers only (Integers)
3. Mixed password (String + Integer + Special Characters)
4. Exit
```

Then, follow the prompts to enter the password length and confirm your choice.

---

##  Example

```
Enter the choice in number: 3
Enter the length of the password that should be generated: 10
Hey once again, your choice was 10 length of mixed password right? (Y/N)
Y
Your generated password is: x3T@8f#Z1&
```

---

##  Behind the Scenes

- The `RandomPasswordGenerator` class handles all logic.
- Uses Python's `random` and `string` libraries.
- Guarantees variety in characters when choosing the mixed option.
- Inserts missing characters (if any) after checking the generated string.

---

##  File Structure

```
random_password_generator.py  # Main program file
README.md                     # Project overview and instructions
```

---

##  Requirements

No external libraries needed. Works with Python 3.6+

---

##  Author

**Mahammad Thameez (Thammi)**  
Just a curious mind building tools to make life easier — one Python script at a time.  
 [GitHub Profile]: (https://github.com/thammi-mhd)

---

##  License

This project is open-source and available under the [MIT License](LICENSE).

```

