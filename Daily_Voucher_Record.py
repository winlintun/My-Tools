import psycopg2
from datetime import datetime


def create_databases():
    conn = psycopg2.connect(
        database='daily_record',
        user='postgres',
        password='toor',
        host='localhost',
        port='5432')
    conn.autocommit = True
    cursor = conn.cursor()
    sql = 'CREATE DATABASE daily_record';

    try:
        cursor.execute(sql)
        print("Successfully Database Create....")
    except (Exception, psycopg2.Error) as e:
        print("Your Database is already exists..\n", e)

    conn.close()


def create_table():
    conn = psycopg2.connect(
        database='daily_record',
        user='postgres',
        password='toor',
        host='localhost',
        port='5432'
    )

    conn.autocommit = True

    cursor = conn.cursor()

    sql = '''CREATE TABLE Daily_Voucher_Record (
    ID SERIAL NOT NULL UNIQUE,
    NAME VARCHAR(255) NOT NULL,
    NO_OF_VOUCHER INT NOT NULL,
    DATE_TIME VARCHAR(255) NOT NULL UNIQUE);'''
    try:
        cursor.execute(sql)
        print("Table created successfully.")
    except (Exception, psycopg2.Error) as e:
        print("Your table is already exists...\n", e)

    conn.close()


def data_insert():
    conn = psycopg2.connect(
        database='daily_record',
        user='postgres',
        password='toor',
        host='localhost',
        port='5432')
    conn.autocommit = True
    cursor = conn.cursor()

    show_data()
    print()
    sql = """INSERT INTO Daily_Voucher_Record (NAME, NO_OF_VOUCHER, DATE_TIME) VALUES(%s, %s, %s);"""
    name = str(input('Enter Name: '))
    no_of_voucher = int(input('Enter number of voucher: '))

    current_date = datetime.now().strftime('%d/%m/%Y %I:%M:%S %p')
    data = (name, no_of_voucher, current_date)
    try:
        cursor.execute(sql, data)
        conn.commit()
        print("Data entry is  successfully.....")
    except(Exception, psycopg2.Error) as e:
        print(e)


def show_data():
    conn = psycopg2.connect(
        database='daily_record',
        user='postgres',
        password='toor',
        host='localhost',
        port='5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Daily_Voucher_Record')

    rows = cursor.fetchall()

    for x in rows:
        print(x[0], '\t', x[1], '\t', x[2], '\t \t', x[3], '\t')
    conn.commit()


def update_data():
    conn = psycopg2.connect(
        database='daily_record',
        user='postgres',
        password='toor',
        host='localhost',
        port='5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()

    show_data()

    user = int(input('''
    1. Name update
    2. Number of voucher update
    > '''))

    while True:
        if user == 1:
            data_sql_update = '''UPDATE Daily_Voucher_Record SET NAME = %s WHERE id = %s;'''
            name_update = input("Enter Name: ")
            user_id = input("Enter you want to change user of id: ")
            cursor.execute(data_sql_update, (name_update, user_id))
            count = cursor.rowcount
            print(count, f"Id no:{user_id} name are change to {name_update} .")
            conn.commit()
            break

        elif user == 2:
            data_sql_update = '''UPDATE Daily_Voucher_Record SET NO_OF_VOUCHER = %s WHERE id = %s;'''
            no_of_voucher_update = input("Enter number of vouchers: ")
            user_id = input("Enter you want to change user of id: ")
            cursor.execute(data_sql_update, (no_of_voucher_update, user_id))
            count = cursor.rowcount
            print(count, f"Id no:{user_id} name are change to {no_of_voucher_update} .")
            conn.commit()
            break
        elif user == 3 or user == 4 or user == 5:
            break
        else:
            print("Wrong number!!!!")


def delete_data():
    conn = psycopg2.connect(
        database='daily_record',
        user='postgres',
        password='toor',
        host='localhost',
        port='5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    show_data()

    sql = '''DELETE FROM Daily_Voucher_Record WHERE id = %s;'''
    user_id = input("Enter you want to change user of id: ")
    cursor.execute(sql, user_id)
    print("Successfully deleted.")


if __name__ == '__main__':

    # create_databases()
    create_table()

    # main start
    program = ''

    while program != '100':

        print("""
        --------------------------------------------
            Welcome My Daily Voucher Note Program
        --------------------------------------------
        1. Data Entry
        2. Update Data
        3. Show Data
        4. Delete Data
        5. Exiting '100'""")
        data_entry = int(input('Enter Options: '))

        if data_entry == 1:
            data_insert()
        elif data_entry == 2:
            update_data()
        elif data_entry == 3:
            show_data()
        elif data_entry == 4:
            delete_data()
        elif data_entry == 5:
            exit()
        else:
            program = '100'
            exit()
