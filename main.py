import random

import psycopg2

try:
    conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="postgres",
                            host="localhost",
                            port="5432")
    cursor = conn.cursor()
    # cursor.execute('SELECT * FROM "Jobs"')

    for i in range(101):
        name = random.randint(1, 40)
        car = random.randint(1, 40)
        service = random.randint(1, 9)
        cursor.execute(f'INSERT INTO "Jobs" ("Job_client", "Job_cars", "Job_services") VALUES ({name}, {car}, {service})')

    # Сохраняем изменения и закрываем базу данных
    conn.commit()
    print('Success, ёпта')
    conn.close()

#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
#     cursor.close()
#     conn.close()
#
except psycopg2.Error as e:
    print('Error: ', e)
