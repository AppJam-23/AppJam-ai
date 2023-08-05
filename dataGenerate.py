import random
import names
import mysql.connector

# MYSQL_USERNAME= root
# MYSQL_PASSWORD= mysql
# MYSQL_DATABASE= AppJam-23
# MYSQL_HOST= svc.sel4.cloudtype.app
# MYSQL_PORT= 32676

def random_float(min_val, max_val):
    return round(random.uniform(min_val, max_val), 1)

def insert_data():
    # Change this line with your connection
    connection = mysql.connector.connect(host="svc.sel4.cloudtype.app", user="root", password="mysql", database="AppJam-23", port="32676")
    cursor = connection.cursor()

    for i in range(100):
        age = random.randint(14, 17)
        name = names.get_full_name().replace("'", "''")
        gender = random.randint(0, 1)
        temperature = random_float(35.0, 39.0)
        step = random.randint(5000, 15000)
        heart = random.randint(60, 100)
        sleep = random.randint(360, 540)
        status = random.choices([0, 1, 2], weights=[70, 20, 10], k=1)[0]
        suspected = 1 if status == 1 else 0
        patient = 1 if status == 2 else 0

        insert_query = f"INSERT INTO `People_Info` (`id`, `Name`, `Age`, `Gender`, `Temperature`, `Step`, `Heart`, `Sleep`, `Suspected`, `Patient`) VALUES ({i + 1}, '{name}', {age}, {gender}, {temperature}, {step}, {heart}, {sleep}, {suspected}, {patient});"
        
        cursor.execute(insert_query)
        connection.commit()

    cursor.close()
    connection.close()

insert_data()
