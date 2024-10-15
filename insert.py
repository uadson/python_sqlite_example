from database import conn
from faker import Faker
from random import randint, uniform, choice
import time
import sys
from gen_cnpj import gera_cnpj


connection = conn()
cursor = connection.cursor()

custormers = []
providers = []
orders = []
products = []

fake = Faker('pt_BR')


### Creating progress bar
def progressBar(count_value, total, suffix=''):
    bar_length = 100
    filled_up_Length = int(round(bar_length* count_value / float(total)))
    percentage = round(100.0 * count_value/float(total),1)
    bar = '=' * filled_up_Length + '-' * (bar_length - filled_up_Length)
    sys.stdout.write('[%s] %s%s ...%s\r' %(bar, percentage, '%', suffix))
    sys.stdout.flush()
    

# 500 customers
for _ in range(500):
    
    customer = {
        'name': fake.name(),
        'age': randint(18, 61),
        'email': fake.email(),
        'phone': fake.phone_number()      
    }
    custormers.append(customer)
    
# 20 providers
for _ in range(20):
    provider = {
        'name': fake.company(),
        'register': gera_cnpj(),
        'contact': fake.phone_number()
    }
    providers.append(provider)
    
# 1000 products
for _ in range(1000):
    product = {
        'name': fake.name_nonbinary(),
        'price': round(uniform(5, 500), 2),
        'provider_id': choice([i for i in range(len(providers))])
    }
    products.append(product)
    
# 500 orders
for _ in range(500):
    order = {
        'customer_id': choice([i for i in range(len(custormers))]),
        'product_id': choice([i for i in range(len(products))]),
        'amount': choice([i for i in range(len(products))])
    }
    orders.append(order)

# Save data on the database
for customer in custormers:
    cursor.execute(
        """
            INSERT INTO customers(name, age, phone, email) VALUES (?, ?, ?, ?)
        """, (customer['name'], customer['age'], customer['phone'], customer['email'])
    )
    connection.commit()
    time.sleep(1)
    progressBar(1, len(custormers))
    
for provider in providers:
    cursor.execute(
        """
            INSERT INTO providers(name, register, contact) VALUES (?, ?, ?)
        """, (provider['name'], provider['register'], provider['contact'])
    )    

    connection.commit()
    time.sleep(1)
    progressBar(1, len(providers))
    
for product in products:
    cursor.execute(
        """
            INSERT INTO products(name, price, provider_id) VALUES (?, ?, ?)
        """, (product['name'], product['price'], product['provider_id'])
    )
    connection.commit()
    time.sleep(1)
    progressBar(1, len(products))
    
for order in orders:
    cursor.execute(
        """
            INSERT INTO orders(customer_id, product_id, amount) VALUES (?, ?, ?)
        """, (order['customer_id'], order['product_id'], order['amount'])
    )
    connection.commit()
    time.sleep(1)
    progressBar(1, len(orders))
    
connection.close()
