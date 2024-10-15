import json
import time
from database import conn
import sys


### Creating progress bar
def progressBar(count_value, total, suffix=''):
    bar_length = 100
    filled_up_Length = int(round(bar_length* count_value / float(total)))
    percentage = round(100.0 * count_value/float(total),1)
    bar = '=' * filled_up_Length + '-' * (bar_length - filled_up_Length)
    sys.stdout.write('[%s] %s%s ...%s\r' %(bar, percentage, '%', suffix))
    sys.stdout.flush()
    
    
# Connecting with database
connection = conn()
cursor = connection.cursor()

# 
sql = []
sqlstr = ''

print('Creating tables in the database')

with open('tables.json', 'r') as file:
    tables = json.load(file)
    
    
    
    for n, table in enumerate(tables):
        sql.clear()
        sqlstr = ''        
        if table['id'] == n + 1:
            
            for key, value in table['index']['columns'].items():
                aux = f'\t{key} {value}'
                sql.append(aux)
            
            sqlstr = ',\n'.join(sql)
            
            cursor.execute(
                f"""
                    CREATE TABLE IF NOT EXISTS {table['index']['tb_name']} (
                        {sqlstr}
                    )
                """
            )
            
            connection.commit()
        time.sleep(1)
        progressBar(n+1, len(tables))
    
    connection.close()
        
print('\nTables created successfully')
