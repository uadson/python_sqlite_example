```
TBS_LIST = [
    {
        'id': 1, 
        'index': {
            'tb_name': 'customers',
            'columns': {
                'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
                'name': 'TEXT NOT NULL',
                'age': 'INTEGER',
                'phone': 'TEXT',
                'email': 'TEXT'
            }
        }
    },
    
    {
        'id': 2, 
        'index': {
            'tb_name': 'providers',
            'columns': {
                'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
                'name': 'TEXT NOT NULL',
                'register': 'TEXT',
                'contact': 'TEXT' 
            } 
        }
    },
    
    {
        'id': 3,
        'index': {
            'tb_name': 'orders',
            'columns': {
                'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
                'customer_id': 'INTEGER',
                'product_id': 'INTEGER',
                'amount': 'INTEGER',
                'FOREIGN KEY (customer_id)':  'REFERENCES customers (id)'
            }
        }
    },
    
    {
        'id': 4,
        'index': {
            'tb_name': 'products',
            'columns': {
                'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
                'name': 'TEXT NOT NULL',
                'price': 'REAL',
                'provider_id': 'INTEGER',
                'FOREIGN KEY (provider_id)': 'REFERENCES providers (id)'
            }  
        }
    },
]

with open('tables.json', 'w', encoding='utf-8') as file:
    json.dump(TBS_LIST, file, indent=4, ensure_ascii=False)
```