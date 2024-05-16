from datetime import datetime
from decimal import Decimal
from typing import Any, Dict
import fastavro
import io

from sqlalchemy import text
def determine_age_group(birth_date):
    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    if age < 18:
        return "Under 18"
    elif 18 <= age < 25:
        return "18-24"
    elif 25 <= age < 35:
        return "25-34"
    elif 35 <= age < 45:
        return "35-44"
    elif 45 <= age < 55:
        return "45-54"
    elif 55 <= age < 65:
        return "55-64"
    else:
        return "65+"

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d

            
def process_customer_table(file_content,data_updated,unique_dates,pool):
    customer_data = data_updated["dim_customer"]
    print("customer stsrt")
    change_is_big = False
    with io.BytesIO(file_content) as f:
        reader = fastavro.reader(f)
        if(sum(1 for line in reader)>20):
           with pool.connect() as db_conn:
                    query = """
                                    SELECT
                                      c.id,p.birthday,p.sex 
                                    FROM
                                      person p
                                    JOIN 
                                    customer c ON p.id = c.person_data_id 
                            """
                    result = db_conn.execute(text(query))
                    rows = result.fetchall()
                   
                    dict = {row[0]: row[1:] for row in rows}
                    print(len(dict))
                    change_is_big = True
    with io.BytesIO(file_content) as f:
        reader = fastavro.reader(f)
        for record in reader:
            if 'payload' in record and record['source_metadata']['change_type'] == 'INSERT':
                payload_data = record['payload']
                id = payload_data.get('id')
                person_data_id = payload_data.get('person_data_id')
                if(change_is_big):
                    key_to_find = Decimal(id)
                    row = dict.get(key_to_find)
                    if row is None:
                        continue
                else:
                    with pool.connect() as db_conn:
                        query = """
                                    SELECT
                                      p.birthday,p.sex 
                                    FROM
                                      person p
                                    JOIN 
                                    customer c ON p.id = c.person_data_id 
                                    WHERE 
                                    p.id =:person_data_id"""
                        result = db_conn.execute(text(query),{"person_data_id": person_data_id})
                        row = result.fetchone()
                if row is not None:
                    age_group = determine_age_group(row[0])
                    customer_data.append({
                    "id":id,
                    "sex":row[1],
                    "age_group":age_group
                })
    print("customer end")                
                
    

def process_manager_table(file_content,data_updated,unique_dates, pool):
    manager_data = data_updated["dim_manager"]
    print("manager start")
    change_is_big = False
    with io.BytesIO(file_content) as f:
        reader = fastavro.reader(f)
        if(sum(1 for line in reader)>20):
           with pool.connect() as db_conn:
                    query = """
                            SELECT m.id, p.birthday, p.sex, a.city, CONCAT(a.building_number, '-', a.flat_number) AS store_number
                            FROM manager m
                            JOIN person p ON m.person_data_id = p.id
                            JOIN traiding_point t ON m.trading_point_id = t.id
                            JOIN address a ON t.address_id=a.id
                            """
                    result = db_conn.execute(text(query))
                    rows = result.fetchall()
                   
                    dict = {row[0]: row[1:] for row in rows}
             
                    print(len(dict))
                    change_is_big = True
    with io.BytesIO(file_content) as f:
        reader = fastavro.reader(f)
        for record in reader:
            if 'payload' in record and record['source_metadata']['change_type'] == 'INSERT':
                payload_data = record['payload']
                id = payload_data.get('id')
                traiding_point = payload_data.get('traiding_point')
                person_data_id = payload_data.get('person_data_id')
            if(change_is_big):
                key_to_find = Decimal(id)
                row = dict.get(key_to_find)
                if row is None:
                    continue
            else:
                with pool.connect() as db_conn:
                        query = """
                                SELECT p.birthday, p.sex, a.city, CONCAT(a.building_number, '-', a.flat_number) AS store_number
                                FROM manager m
                                JOIN person p ON m.person_data_id = p.id
                                JOIN trading_point t ON m.trading_point = t.id
                                JOIN address a ON t.address_id=a.id
                                WHERE t.id = :traiding_point AND p.id = :person_data_id
                                """
                        result = db_conn.execute(text(query), {"traiding_point": traiding_point, "person_data_id": person_data_id})
                        row = result.fetchone()
            if row is not None:
                age_group = determine_age_group(row[0])
                manager_data.append({
                            "id":id,
                            "traiding_point":row[3],
                            "city":row[2],
                            "sex":row[1],
                            "age_group":age_group
                    })
    print("manager end")
              


def process_order_table(file_content,data_updated,unique_dates,pool):
    print("orderstart")
    order_data = data_updated["dim_order"]
    change_is_big =False
    dict ={}
    
                    
    with io.BytesIO(file_content) as f:
        reader = fastavro.reader(f)
        if(sum(1 for line in reader)>20):
           with pool.connect() as db_conn:
                    query = """
                               SELECT o.id, vb.company_size,vb.name
                                FROM "orders" o
                                JOIN vendor_brand vb ON o.vendor_brand_id = vb.id
                            """
                    result = db_conn.execute(text(query))
                    rows = result.fetchall()
                   
                    dict = {row[0]: row[1:] for row in rows}
               
                    print(len(dict))
                    change_is_big = True
    with io.BytesIO(file_content) as f:
        reader = fastavro.reader(f)
        for record in reader:
            if 'payload' in record and record['source_metadata']['change_type']== 'INSERT':
                payload_data = record['payload']   
                id = payload_data.get('id')
                jewellery_type = payload_data.get('jewellery_type')
                main_color = payload_data.get('main_color')
                main_metal = payload_data.get('main_metal')
                main_gem = payload_data.get('main_gem')
                assay = payload_data.get('assay')
                weight = payload_data.get('weight')
                if(change_is_big):
                    key_to_find = Decimal(id)
                    row = dict.get(key_to_find)
                    if row is None:
                        continue
                else:
                    with pool.connect() as db_conn:
                        query = """
                                SELECT vb.factory_size,vb.name
                                    FROM "orders" o
                                    JOIN vendor_brand vb ON o.vendor_brand_id = vb.id
                                    WHERE o.id = :id;
                                """
                        result = db_conn.execute(text(query), {"id": id})
                        row = result.fetchone()
                if row is not None:
                    order_data.append({
                        'id': id,
                        'vendor': row[1],
                        'type': jewellery_type,
                        'gem': main_gem,
                        'metal': main_metal,
                        'assay': assay,
                        'color': main_color, 
                        'weight': weight,
                        'vendor_size':row[0]
                    })
    print("order_end")
    print(len(order_data))
    print(order_data[0])
      
                 

def process_payment_table(file_content,data_updated,unique_dates,pool):
        payment_data = data_updated["fact_payment"]
        date_data = data_updated["dim_date"]
        change_is_big = False
        dict={}
        print("payment start")
        with io.BytesIO(file_content) as f:
            reader = fastavro.reader(f)
            if(sum(1 for line in reader)>20):
                with pool.connect() as db_conn:
                    query = """
                            SELECT
                                p.id,
                                c.amount - c.amount_paid AS remaining_amount,
                                o.customer_id,
                                c.order_id,
                                o.manager_id
                            FROM payment p
                            JOIN
                                contract c ON p.contract_id = c.id
                            JOIN
                                "orders" o ON o.id = c.order_id
                            """
                    result = db_conn.execute(text(query))
                    rows = result.fetchall()
                    dict = {row[0]: row[1:] for row in rows}
               
                    print(len(dict))
                    change_is_big = True
        with io.BytesIO(file_content) as f:
            reader = fastavro.reader(f)
            for record in reader:
                 if 'payload' in record and record['source_metadata']['change_type']== 'INSERT':
                    payload_data = record['payload']   
                    id = payload_data.get('id')
                    amount = payload_data.get('amount')
                    payment_date = payload_data.get('payment_date')
                    if(change_is_big):
                        key_to_find = Decimal(id)
                        row = dict.get(key_to_find)
                        if row is None:
                            continue
                    else:
                        with pool.connect() as db_conn:
                            query = """
                                SELECT
                                    c.amount - c.amount_paid AS remaining_amount,
                                    o.customer_id,
                                    c.order_id,
                                    o.manager_id
                                FROM payment p
                                JOIN
                                    contract c ON p.contract_id = c.id
                                JOIN
                                    "orders" o ON o.id = c.order_id
                                WHERE
                                    p.id = :id;"""
                                
                            result = db_conn.execute(text(query), {"id": id})
                            row = result.fetchone()                   

                    if row is not None:
                        payment_data.append({
                                "date":payment_date.strftime('%Y-%m-%d'),
                                "order_id":row[2],
                                "customer_id":row[1],
                                "manager_id":row[3],
                                "amount":amount,
                                "pay_left":row[0],
                            })
    
                    if payment_date not in unique_dates:  
                        unique_dates.add(payment_date)
                        date_data.append({
                                "date": payment_date,
                                "month":payment_date.strftime("%B %Y"),
                                "year":payment_date.year,
                                "quarter_number":str((payment_date.month - 1) // 3 + 1) +" "+str(payment_date.year),
                                "day_of_week":payment_date.strftime("%A")
                            })
        print("payment end")
        print(len(payment_data))

        
                  
def process_storage_table(file_content,data_updated,unique_dates,pool):
    print("storage start")
    delivered_data = data_updated["fact_delivered_order"]
    date_data = data_updated["dim_date"]
    change_is_big = False
    with io.BytesIO(file_content) as f:
        reader = fastavro.reader(f)
        if(sum(1 for line in reader)>20):
            with pool.connect() as db_conn:
                query = """
                            SELECT
                                s.id,
                                o.customer_id,
                                o.manager_id,
                                s.real_weight - o.weight AS accurancy_weight,
                                o.vendor_cost,
                                s.deliver_date - o.conclusion_date AS delivery_delay,
                                c.amount 
                            FROM
                                storage s
                            JOIN
                                "orders" o ON s.order_id = o."id"
                            JOIN 
                                contract c ON c.order_id = o.id
                            """
                result = db_conn.execute(text(query))
                rows = result.fetchall()
                   
                dict = {row[0]: row[1:] for row in rows}
             
                print(len(dict))
                change_is_big = True
    with io.BytesIO(file_content) as f:
        reader = fastavro.reader(f)
        for record in reader:
            if 'payload' in record and record['source_metadata']['change_type'] == 'INSERT':
                payload_data = record['payload']
                id = payload_data.get('id')
                order_id = payload_data.get('order_id')
                deliver_date = payload_data.get('deliver_date')
                if(change_is_big):
                    key_to_find = Decimal(id)
                    row = dict.get(key_to_find)
                    if row is None:
                        continue
                else:
                    with pool.connect() as db_conn:
                        query = """
                            SELECT
                                o.customer_id,
                                o.manager_id,
                                s.real_weight - o.weight AS accurancy_weight,
                                o.vendor_cost,
                                s.deliver_date - o.conclusion_date AS delivery_delay,
                                c.amount 
                            FROM
                                storage s
                            JOIN
                                "orders" o ON s.order_id = o."id"
                            JOIN 
                                contract c ON c.order_id = o.id
                            WHERE
                                s.id = :id;

                            """
                                
                        result = db_conn.execute(text(query), {"id": id})
                        row = result.fetchone()               
                
                if(row is not None and deliver_date is not None) :
                    delivered_data.append({
                        "date":deliver_date.strftime('%Y-%m-%d'),
                        "order_id":order_id,
                        "customer_id":row[0],
                        "manager_id":row[1],
                        "accurancy_weight": row[2],
                        "cost": row[3],
                        "profit":float(row[5]) - float(row[3]),
                        "production_duration": row[4]
                    })
                if deliver_date not in unique_dates:  
                        unique_dates.add(deliver_date)
                        date_data.append({
                            "date": deliver_date,
                            "month":deliver_date.strftime("%B %Y"),
                            "year":deliver_date.year,
                            "quarter_number":str((deliver_date.month - 1) // 3 + 1) +" "+str(deliver_date.year),
                            "day_of_week":deliver_date.strftime("%A")
                            })
    print("storage end")
    print(delivered_data[0])
            
data_instructions: Dict[str, Any] = {
    'customer': process_customer_table,
   'manager': process_manager_table,
    'order': process_order_table,
   'payment':process_payment_table,
    'storage':process_storage_table,
}