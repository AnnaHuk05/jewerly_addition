import hashlib
import json
import random
import csv
from datetime import datetime, timedelta
import string
import uuid

print(uuid.uuid4)

# Read the input JSON file
with open('csvjson.json', 'r') as file:
    data = json.load(file)

def generate_company_creation_date():
    today = datetime.now()
    min_creation_date = today - timedelta(days=200*365)  # Мінімальна дата створення компанії (60 років)
    max_creation_date = today - timedelta(days=0.2*365)  # Максимальна дата створення компанії (18 років)
    creation_date = min_creation_date + timedelta(seconds=random.randint(0, int((max_creation_date - min_creation_date).total_seconds())))
    return creation_date

def generate_order_status():
    statuses = ['pending', 'processed', 'in stock', 'shipped', 'paid']
    return random.choice(statuses)
def short_uuid_to_int(short_uuid):
    return int(short_uuid, 16)

def short_uuid():
   
    unique_id = uuid.uuid4()
    hashed_id = hashlib.sha1(str(unique_id).encode()).hexdigest()[:8]
    return hashed_id
# Приклад використання
def generate_id():
    short_id = short_uuid()
    integer_value = short_uuid_to_int(short_id)
    return integer_value

# Виклик функції


def calculate_vendor_cost(price_in_usd_str):
    if price_in_usd_str:  
        try:
            price_in_usd = float(price_in_usd_str)
            cost_lower_bound = int(price_in_usd / 10)
            cost_upper_bound = int(price_in_usd / 2)
            vendor_cost = price_in_usd - random.randint(cost_lower_bound, cost_upper_bound)
        except ValueError:
            vendor_cost = 0  
    else:
        vendor_cost = 0  

    return vendor_cost
def clean_string(value):
    if not value or "'" in value:
        return "n|a"
    else:
        return value
    
def is_unique_id(this_id, seen_ids):
    if this_id not in seen_ids and not None and not '' and not "":
        seen_ids.add(this_id)
        return True
    else:
        return False
def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))
def generate_vendor_name():
    prefixes = ['Luxury', 'Diamond', 'Gems', 'Sparkle', 'Elegance', 'Exquisite', 'Paris', 'Milan', 'New York', 'London', 'Tokyo', 'Los Angeles', 'Kyiv', 'Lviv', 'Kharkiv', 'Odesa', 'Dnipro']
    suffixes = ['Jewels', 'Creations', 'Gems', 'Boutique', 'Designs', 'Collections']
    return f"{random.choice(prefixes)} {random.choice(suffixes)}"
#персональні дані
def generate_personal_data(num_entries):
    first_names = ['Ivan', 'Olena', 'Petro', 'Mariya', 'Vasyl', 'Anna', 'Mykhailo', 'Tetiana', 'Oleksandr', 'Nataliia', 'Yevhen', 'Liudmyla', 'Oksana', 'Yurii', 'Olha', 'Serhii', 'Halyna', 'Andrii', 'Natalia', 'Kateryna']
    last_names = ['Ivanenko', 'Petrenko', 'Sydorenko', 'Kovalenko', 'Mykhailenko', 'Bondarenko', 'Shevchenko', 'Kovalchuk', 'Kovalenko', 'Pavlenko', 'Melnyk', 'Shevchuk', 'Bondar', 'Koval', 'Tkachenko', 'Kavchenko', 'Lysenko', 'Moroz', 'Savchenko', 'Zaytseva']
    for name in first_names:
        if name and name in ['Ivan', 'Petro', 'Vasyl', 'Mykhailo', 'Oleksandr', 'Yevhen', 'Yurii', 'Serhii', 'Andrii']:
            sex = "male"
        elif name:
            sex = "female"

    phone_prefix = '+380'
    
    for i in range(1, num_entries + 1):
        id = generate_id()
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        phone_number = f"{phone_prefix}{random.randint(100000000, 999999999)}"
        # Генеруємо дату народження в діапазоні 18-60 років від поточної дати
        today = datetime.now()
        min_birth_date = today - timedelta(days=60*365) # Мінімальна дата народження (60 років)
        max_birth_date = today - timedelta(days=18*365) # Максимальна дата народження (18 років)
        birthday = min_birth_date + timedelta(seconds=random.randint(0, int((max_birth_date - min_birth_date).total_seconds())))
        
        personal_info = {
            "id": id,
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "birthday": birthday.strftime('%Y-%m-%d'), # Перетворюємо дату в рядок у форматі YYYY-MM-DD
            "sex": sex
        }
        
        personal_data.append(personal_info)
    return id

def generate_random_date():
    start_date = datetime.now() - timedelta(days=5*365)
    end_date = datetime.now()
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
def generate_random_open_time():
    # Генерація випадкового часу відкриття у форматі HH:MM:SS
    return datetime.strptime(f"{random.randint(8, 9)}:{random.randint(0, 59)}:00", '%H:%M:%S')

def generate_random_closed_time(open_time):
    # Генерація випадкового часу закриття торгової точки, який є 10 годин після відкриття
    closed_time = open_time + timedelta(hours=10)
    return closed_time.strftime('%H:%M:%S')

extracted_order_data = []
extracted_brand_data = []
extracted_address_data = []
extracted_contract_data = []
personal_data = []
payment_data = []
customer_data = []
storage_data =[]
manager_data = []
order_ids = set()
vendor_ids = set()
customer_ids = set()
manager_ids = set()
trading_point_data = []
consultations = []
remainder_data = []
addresses = []
ids = set()
cities = ['Kyiv', 'Lviv', 'Kharkiv', 'Odesa', 'Dnipro', 'New York', 'London', 'Paris', 'Tokyo', 'Los Angeles']
streets = ['Main St', 'High St', 'Oak St', 'Park Ave', 'Broadway', 'Queen St', 'Market St', 'Abbey Rd', 'Sunset Blvd']
#адреса
print(generate_id())
for address in range(1,100):
    id =generate_id()
    if(is_unique_id(id,ids)):
        extracted_address_data.append({
            
                "id": id,
                "city": random.choice(cities),
                "street": random.choice(streets),
                "building_number": random.randint(1, 100),
                "flat_number":  random.randint(1, 50)
        })
#магазин
for i in range(1, 27):
    open_time = generate_random_open_time()
    phone_prefix = '+380'
    random_string = ''.join(random.choices(string.ascii_lowercase, k=8))
    email = random_string + "@gmail.com"
    id =generate_id()
    if(is_unique_id(id,ids)):
        trading_point_info = {
            "id": id,
            "address_id": random.choice(extracted_address_data)["id"],
            "phone_number": f"{phone_prefix}{random.randint(100000000, 999999999)}",
            "email": email,  # Генеруємо випадкову електронну адресу
            "open_time": open_time.strftime('%H:%M:%S'),  # Перетворюємо час в строковий формат
            "closed_time": generate_random_closed_time(open_time), # Випадковий час закриття
            "area": round(random.uniform(50, 200), 2),  # Площа торгової точки
            "establish_date": generate_random_date().strftime('%Y-%m-%d')  # Дата відкриття торгової точки
            }
        trading_point_data.append(trading_point_info)
    
#менеджер
for manager_info in range(100):
        manager_id = generate_id()
        if(is_unique_id(manager_id,manager_ids)):
            manager_info2 = {
                "id": manager_id,
                "trading_point_id": random.choice(trading_point_data)["id"],
                "person_data_id": generate_personal_data(1),
                "salary": random.randint(2000, 5000),  # Зарплата за консультацію
                "hire_date": generate_random_date().strftime('%Y-%m-%d')  # Дата найму менеджера
            }
            manager_data.append(manager_info2)

#замовлення
for orderData in data:
    order_id = orderData['Order ID']
    datetime_str = orderData["Order datetime"]
    datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S %Z')
    date = datetime_obj.date()
    if(is_unique_id(order_id, order_ids)):
        if(orderData['User ID']==""):
            continue
        extracted_order_data.append({
            'id': orderData['Order ID'],
            'customer_id': orderData['User ID'],
            'vendor_brand_id': orderData['Purchased product ID'],
            'manager_id': random.choice(manager_data)["id"],
            'jewellery_type': clean_string(str(orderData["Category alias"]).replace('jewelry.', '')),
            'main_color': clean_string(orderData.get('Main color', '')),
            'main_metal': clean_string(orderData.get('Main metal', '')),
            'main_gem': clean_string(orderData.get('Main gem', '')),
            'assay': random.randint(50, 100),
            'weight': round(random.uniform(1, 100),3),
            'status': generate_order_status(),
            'vendor_cost': calculate_vendor_cost(orderData.get('Price in USD', '')),
            'conclusion_date':date.strftime('%Y-%m-%d')
        })

#бренд  
for brandData in data:
     vendor_id=brandData['Purchased product ID']
     company_sizes = ["Small", "Medium", "Large", "Startup", "Global"]
     
     address_id= random.choice(extracted_address_data)["id"]
     
     if(is_unique_id(vendor_id,vendor_ids)):
        extracted_brand_data.append({
            'id': brandData['Purchased product ID'],
            'address_id':address_id,
            'name':generate_vendor_name(),
            'company_size':random.choice(company_sizes),
            'establish_date':generate_company_creation_date().strftime('%Y-%m-%d')
        })

#користувач        
for customer in data:
    customer_id = customer["User ID"]
    if is_unique_id(customer_id, customer_ids):
        if(customer_id!=""):   
            customer_data.append({
                'id': customer_id,
                'person_data_id': generate_personal_data(1)
            
        })

#консультація
for i in range(0,len(extracted_order_data)):
    duration = random.randint(20,90)
    id =generate_id()
    if(is_unique_id(id,ids)):
        consultations.append({
          "id":id,
          "manager_id":random.choice(manager_data)["id"],
          "customer_id":random.choice(customer_data)["id"],
          "start_time":generate_random_date().strftime('%Y-%m-%d %H:%M:%S'),
          "end_time":(datetime.strptime(extracted_order_data[i]["conclusion_date"], '%Y-%m-%d')+timedelta(minutes=duration)).strftime('%Y-%m-%d %H:%M:%S'),
           "cost":duration*round(random.uniform(0.2,1),2)
      })


#оплата
for i in range(1, 50000):
        id = generate_id()
        choice = random.randint(1,3)
        consultation =0
        contract_id =0
        date = datetime.now()
        if(choice%2==0):
            consultation = random.choice(consultations)
            consultation_id = consultation["id"]
            amount = consultation["cost"]
            date= generate_random_date()
            contract_id = None
        else:
            contract_id = random.choice(extracted_contract_data)["id"]
            contract = next(item for item in extracted_contract_data if item["id"] == contract_id)
            amount_left = contract["amount"] - contract["amount_paid"] 
            amount = round(random.uniform(0, amount_left), 2)
            consultation_id =None
            conclusion_date = datetime.strptime(contract["conclusion_date"], '%Y-%m-%d')
            expired_date = datetime.strptime(contract["expired_date"], '%Y-%m-%d')
            random_days = random.randint(0, (expired_date - conclusion_date).days)
            date = (conclusion_date + timedelta(days=random_days))
        
        if(is_unique_id(id,ids)):
            payment_info = {
                "id": id,
                "consultation_id": consultation_id,
                "contract_id": contract_id,
                "amount":amount,
                "payment_date":date.strftime('%Y-%m-%d')
            }
            payment_data.append(payment_info)    

#нагадування
for contract in extracted_contract_data:
    conclusion_date = datetime.strptime(contract["conclusion_date"], '%Y-%m-%d')
    expired_date = datetime.strptime(contract["expired_date"], '%Y-%m-%d')
    remainder_count = (expired_date - conclusion_date).days%30
    reminder_date = conclusion_date
   
    
    for i in range(remainder_count):
        if(len(remainder_data)>50000):
            break
        id =generate_id()
        if(is_unique_id(id,ids)):
           
            reminder_date =reminder_date + timedelta(days=30)
            remainder_data.append({
                "id":id,
                "contract_id":contract["id"],
                "reminder_date": reminder_date.strftime('%Y-%m-%d'),
                "need_to_pay": contract["amount"]/remainder_count
   })
#склад
for order in extracted_order_data:
    if(order["status"]=="in stock"):
        trading_point = None
        for manager_info in manager_data:
            if manager_info['id'] == order["manager_id"]:
                trading_point = manager_info['trading_point_id']
                break
        id =generate_id()
        if(is_unique_id(id,ids)):
            storage_data.append({
                "id":id,
                "order_id":order["id"],
                "real_weight":order["weight"]+round(random.uniform(-1,1),3),
                "trading_point_id": trading_point,
                "deliver_date":(datetime.strptime(order["conclusion_date"], '%Y-%m-%d')+timedelta(days=random.randint(3,30))).strftime('%Y-%m-%d'),
            })
   

with open('order.json', 'w') as file:
    json.dump(extracted_order_data, file, indent=4)

with open('brand.json', 'w') as file:
    json.dump(extracted_brand_data, file, indent=4)

with open('address.json', 'w') as file:
    json.dump(extracted_address_data, file, indent=4)


with open('personal_data.json', 'w') as file:
    json.dump(personal_data, file, indent=4)

with open('payment.json', 'w') as file:
    json.dump(payment_data, file, indent=4)


with open('customer.json', 'w') as file:
    json.dump(customer_data, file, indent=4)


with open('manager.json', 'w') as file:
    json.dump(manager_data, file, indent=4)


with open('trading_point.json', 'w') as file:
    json.dump(trading_point_data, file, indent=4)

with open('consultation.json', 'w') as file:
    json.dump(consultations, file, indent=4)

with open('storage.json', 'w') as file:
    json.dump(storage_data, file, indent=4)

with open('reminder.json', 'w') as file:
    json.dump(remainder_data, file, indent=4)


