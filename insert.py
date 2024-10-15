from database import conn
from faker import Faker
from random import randint
from time import sleep

connection = conn()
cursor = connection.cursor()

custormers = []

fake = Faker('pt_BR')

# Gerando mil registros aleatórios
for _ in range(1000):
    customer = {
        'name': fake.name(),
        'age': randint(18, 61),
        'phone': fake.phone_number()        
    }
    
    custormers.append(customer)

# Salvando os registros no banco de dados
for customer in custormers:
    cursor.execute(
        """
            INSERT INTO customers(name, age, phone) VALUES (?, ?, ?)
        """, (customer['name'], customer['age'], customer['phone'])
    )
    connection.commit()
    
    sleep(0.25)
connection.close()
