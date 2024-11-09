import sqlite3

connection = sqlite3.connect('./part_time_larry/full_stack_trading_app/app.db')

cursor = connection.cursor()

# populate one by one
cursor.execute("INSERT INTO stock (symbol, company) VALUES ('AAPL', 'Apple')")
cursor.execute("INSERT INTO stock (symbol, company) VALUES ('MSFT', 'Microsoft')")
cursor.execute("INSERT INTO stock (symbol, company) VALUES ('TSLA', 'Tesla')")
cursor.execute("INSERT INTO stock (symbol, company) VALUES ('AMD', 'Advanced Micro Devices')")

connection.commit()
