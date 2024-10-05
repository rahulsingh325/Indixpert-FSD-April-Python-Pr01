import os,json

def checking_product_information(JSON_data):
    if not os.path.exists(JSON_data):
        print("Sorry! Database file does not exist.")       
        return
    with open (JSON_data, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = [] 

        if len(data) == 0:
            print("No data found in the stock database.")
            return
        else:
            product_name = input("Enter the product name: ").strip().lower()

            for product in data:
                if product["product"]["name"]==product_name:
                    print(f"{product["product"]["quantity"]} Units of {product_name} are left in your stock. Which id {product["product_id"]}")    
                    
                # for push