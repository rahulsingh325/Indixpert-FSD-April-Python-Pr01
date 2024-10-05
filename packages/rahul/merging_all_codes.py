import time,os



# sys.path.append(r"R:\inventory_management_system\Indixpert-FSD-April-Python-Pr01\rahul")

# JSON_data = r"stock.json"

import Adding_product_information
import update_stock_level
import checking_stock_level

def main_menu(user_name, user_id):  
    user_file = f"{user_name}'s_stock_{user_id}.json"
    JSON_data = r"data_base/inventory_data/" + user_file
    
    if os.name == "nt":
        os.system('cls')
    while True:
        input("\nPress Enter to dashboard: ")
        for i in range(3):
            time.sleep(.1)
            print(".",end ="")
        print( "\n\n******************************************************************" )
        print(f".............Welcome back, {user_name}!.............")
        print( "**********************************************************************" )
        print("\n1. Add a new product")
        print("2. Update the stock level")
        print("3. Check the stock level")
        print("0. Log out")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                Adding_product_information.add_product_in_stock(JSON_data)
            elif choice == 2:
                update_stock_level.update_product(JSON_data)
            elif choice == 3:
                checking_stock_level.checking_product_information(JSON_data)
            elif choice == 0:
                print("loging out...",end="")
                for i in range(6):
                    time.sleep(0.3)
                    print(".",end="")    
                    
                if os.name == 'nt':  
                    os.system('cls')
                                
                break
            else:
                print("Invalid choice. Please try again.")
                exiting_program()
        except ValueError:
            print("Invalid input. Please enter a number.")
            exiting_program()
            
def exiting_program():
    print("Exiting to dashboard",end="")
    for i in range(10):
        time.sleep(0.1)
        print(".",end="")
    print("\n")