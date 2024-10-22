
from database import conn
from faker import Faker
from random import randint, uniform, choice
import time
import sys
from gen_cnpj import gera_cnpj
import threading

connection = conn()
cursor = connection.cursor()

customers = []
providers = []
orders = []
products = []

fake = Faker('pt_BR')


# Creating product name
def create_product():
    first_name = fake.word()
    last_name = fake.word()

    return f"{first_name} {last_name}"

# Creating 100 customers
for _ in range(1000):
    
    customer = {
        'name': fake.name(),
        'age': randint(18, 61),
        'email': fake.email(),
        'phone': fake.phone_number()      
    }
    customers.append(customer)
    
# Creating 20 providers
for _ in range(100):
    provider = {
        'name': fake.company(),
        'register': gera_cnpj(),
        'contact': fake.phone_number()
    }
    providers.append(provider)
    
# Creating 300 products
for _ in range(500):
    product = {
        'name': create_product(),
        'price': round(uniform(1, 500), 2),
        'provider_id': choice([i for i in range(len(providers))]),
        'available': randint(0, 500)
    }
    products.append(product)
    
# Creating 200 orders
for _ in range(2000):
    order = {
        'customer_id': choice([i for i in range(len(customers))]),
        'product_id': choice([i for i in range(len(products))]),
        'amount': choice([i for i in range(len(products))])
    }
    orders.append(order)

print('Registrando os dados no banco de dados ...')

# Save data on the database
def insert_customers():
    for customer in customers:
        cursor.execute(
            """
                INSERT INTO customers(name, age, phone, email) VALUES (?, ?, ?, ?)
            """, (customer['name'], customer['age'], customer['phone'], customer['email'])
        )
        connection.commit()


def insert_providers():
    for provider in providers:
        cursor.execute(
            """
                INSERT INTO providers(name, register, contact) VALUES (?, ?, ?)
            """, (provider['name'], provider['register'], provider['contact'])
        )    

        connection.commit()

     
def insert_products():
    for product in products:
        cursor.execute(
            """
                INSERT INTO products(name, price, provider_id, available) VALUES (?, ?, ?, ?)
            """, (product['name'], product['price'], product['provider_id'], product['available'])
        )
        connection.commit()


def insert_orders():
    for order in orders:
        cursor.execute(
            """
                INSERT INTO orders(customer_id, product_id, amount) VALUES (?, ?, ?)
            """, (order['customer_id'], order['product_id'], order['amount'])
        )
        connection.commit()

        
insert_customers()
insert_providers()
insert_products()
insert_orders()

connection.close()

print('Dados registrados com sucesso !')
