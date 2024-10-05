import json,sys,os, time
# sys.path.append(r"R:\inventory_management_system\Indixpert-FSD-April-Python-Pr01\rahul")
import uuid
import re # Import the re module for regular expressions 


sys.path.append(os.path.dirname(__file__))

user_login_data = r"data_base/user/user_list.json"
def save_user_data(data):
    try: 
        with open(user_login_data, 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []

    users.append(data)
    
    with open(user_login_data, 'w') as file:
        json.dump(users, file, indent=4)
        
def load_user_data():
    try:
        with open(user_login_data, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except PermissionError:
        print(f"Permission denied: {user_login_data}")
        return []
    except json.JSONDecodeError:
        print(f"Invalid JSON in {user_login_data}")
        return []

def generate_user_id():
    return "SN" + str(uuid.uuid4())[:5]

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None
    
def is_email_registered(user_email):
    users = load_user_data()
    for user in users:
        if user["email"]==user_email:
            return True
        else:
            return False
        
def valid_password(new_password):
    if len(new_password)>=8:
        return True
    
def user_authenticated(user_name, user_id):
    import merging_all_codes
    merging_all_codes.main_menu(user_name, user_id)
    
    
def opening_dashboard():
    print("\n\nLoading your Dashboard...",end="")
    for i in range (10):
        time.sleep(.4)
        print(".", end="")
        
        
def user_sign_up_data():
    users = load_user_data()
    
    if len(users) >=10:
        print("registration limit reached. only 10 users can sign up.")
        return
    
    user_id = generate_user_id()
    first_name = input("Your First name: ").strip()
    last_name = input("Your Last name: ").strip()
    
    while True:
        user_email = input("Email ID: ").strip()
        if not validate_email(user_email):
            print("Error: Invalid email format. please enter a valid email address.")
        else:
            break
    
    if is_email_registered(user_email):
        print(f"user already registered with this email: {user_email}")
        return
    
    while True:
        new_password = input("create  password: ").strip()
        
        if valid_password(new_password):
            break
        else:
            print("password must be at least 8 characters long. Please try again") 
            
    confirm_password = input("Confirm password: ").strip()
    
    if new_password == confirm_password:
        new_user = {
            "user_id": user_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": user_email,
            "password": new_password
        }
        
        save_user_data(new_user)
        print("\nRegistration successful.")
    else:
        print("Passwords do not match. Please try again.")
        

def user_login_dataa():
    while True:
        user_email = input("Email ID: ").strip()
        if not validate_email(user_email):
            print("Invalid email format. Please enter a valid email address.")
        else:
            break
        

    password = input("User password: ").strip()

    users = load_user_data()

    
    flag = False
    for user in users:
        if user["email"] == user_email:
            if user["password"] == password:
                
                opening_dashboard()
                user_authenticated(user["first_name"], user["user_id"])
                return 
            else:
                print("Invalid password. Please try again.")
                return
        else:
            flag = True
    if flag:
        print("Sorry! You are new user, Please Sign Up first")
    return False 


def normal_user():
    while True:
        print("\n1: Log In")
        print("2: Sign up")
        print("3: Main menu")
        try:
            choice = int(input("Enter choice: ").strip())
            if choice == 1:
                user_login_dataa()
                
                    
            elif choice == 2:
                user_sign_up_data()
                

            elif choice == 3:
                break

            else:
                print("Not valid input\n")
        except ValueError:
            print("Enter integer value")
            
def admin_login():
    print("~ [ADMIN_LOGIN] ~\n")
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    

    if any(u['username'] == username and u['password'] == password and u.get('is_admin', False) for u in admin_login()):
        print("Admin login successful!")
        return True
    else:
        print("Invalid admin username or password.")
    return False

def delete_user_data():
    users_data = admin_login()
    if users_data:
        print("Current Users:")
        for idx, user in enumerate(users_data, start=1):
            print(f"{idx}. {user['username']}")

        try:
            user_idx = int(input("Enter the number of the user to delete: ")) - 1
            
            if 0 <= user_idx < len(users_data):
                confirmation = input(f"Are you sure you want to delete user '{users_data[user_idx]['username']}'? (yes/no): ")
                if confirmation.lower() == 'yes':
                    deleted_user = users_data.pop(user_idx)
                    save_user_data(users_data)
                    print(f"User '{deleted_user['username']}' deleted successfully.")
                else: 
                    print("User deletion canceled.")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No users available to delete.")

def update_user_data():
    users_data = admin_login()
    if users_data:
        print("Current Users:")
        for idx, user in enumerate(users_data, start=1):
            print(f"{idx}. {user['username']}")

        try:
            user_idx = int(input("Enter the number of the user to change: ")) - 1
            
            if 0 <= user_idx < len(users_data):
                user_to_edit = users_data[user_idx]
                print(f"Editing user: {user_to_edit['username']}")
                
                print("Hint -[The file is created from the username, so if you change the username, another file will be accessed. Do you still want to change the username?]")
                attribute = input("Which attribute do you want to change? (first_name, last_name, username, password): ")

                if attribute in user_to_edit:
                    new_value = input(f"Enter new value for {attribute}: ")
                    if attribute == "password":
                        new_value = valid_password()  
                    
                    user_to_edit[attribute] = new_value  
                    save_user_data(users_data)  
                    print(f"User '{user_to_edit['username']}' updated successfully.")
                else:
                    print("Invalid attribute.")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No users available to change.")


def login_user_data():
    users_data = admin_login()
    if not users_data:
        print("No users available.")
        return
    class InventoryManagementSystem:
        def __init__(self, username):
            self.username = username
                    # Initialize other attributes and methods as needed

    print("Current Users:")
    for idx, user in enumerate(users_data, start=1):
        print(f"{idx}. {user['username']}")
            # ... other code ...

    try:#-
        user_idx = int(input("Enter the number of the user to view options: ")) - 1
        def login_user_data():
                users_data = admin_login()
                if not users_data:
                    print("No users available.")
                    return

        if 0 <= user_idx < len(users_data):
            selected_user = users_data[user_idx]
            print(f"Selected User: {selected_user['username']}")
            inventory_system = InventoryManagementSystem(selected_user['username'])
            users_data(inventory_system)
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")
        print("Current Users:")
        for idx, user in enumerate(users_data, start=1):
                print(f"{idx}. {user['username']}")
#+
                try:#+
                    user_idx = int(input("Enter the number of the user to view options: ")) - 1
#+
                    if 0 <= user_idx < len(users_data):
                        selected_user = users_data[user_idx]
                        print(f"Selected User: {selected_user['username']}")
                        inventory_system = InventoryManagementSystem(selected_user['username'])
                        users_data(inventory_system)
                    else:#+
                        print("Invalid selection.")
                except ValueError:#+
                    print("Please enter a valid number.")

        
def admin_menu():
    while True:
        print("\n~~")
        print("* [ADMIN_MENU] *")
        print("")
        print("1. Delete User Data")
        print("2. Update User Data")
        print("3. Login User Data")
        print("4. Exit Admin Menu\n")  
        choice = input("Enter your choice: ")

        if choice == "1":
            delete_user_data()
        elif choice == "2":
            update_user_data()
        elif choice == "3":
            login_user_data()
        elif choice == "4":  
            print("Exiting Admin Menu.")
            break
        else:
            print("Invalid choice. Please try again.")

def dashboard():
    print("\n*************** welcome to Inventory management system **************\n\n")
    while True:
        print("\n1: Normal User")
        print("2: Admin")
        print("0: Exit")
        
        try:
            choice = int(input("Enter your choice: ").strip())
            
            if choice == 1:
                normal_user()
                    
            elif choice == 2:
                if admin_login():                   
                    admin_menu()
            elif choice == 0:
                print("\nExiting the system...")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("only integer values are allowed")