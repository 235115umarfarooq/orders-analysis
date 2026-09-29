import sqlite3

conn = sqlite3.connect("orders.db")
cur = conn.cursor()

# Query (c): Cities with average order amount > 5000
print("Cities with avg order > 5000:")
cur.execute("""
SELECT c.city, AVG(o.amount) AS avg_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.city
HAVING AVG(o.amount) > 5000;
""")
for row in cur.fetchall():
    print(row)

conn.close()