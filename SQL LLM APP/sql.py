import sqlite3


connection = sqlite3.connect("mall1.db")


cursor = connection.cursor()


table_info = """
CREATE TABLE IF NOT EXISTS MALL_RECORD (
    ID INTEGER PRIMARY KEY,
    STORE_NAME VARCHAR(50),
    CATEGORY VARCHAR(50),
    LOCATION VARCHAR(50),
    OPENING_TIME VARCHAR(50),
    CLOSING_TIME VARCHAR(50),
    CONTACT_NUMBER VARCHAR(15),
    EMAIL VARCHAR(50),
    WEBSITE VARCHAR(50)
);
"""
cursor.execute(table_info)

data = [
    ('Store 1', 'Clothing', 'Ground Floor', '09:00 AM', '09:00 PM', '1234567890', 'store1@example.com', 'www.store1.com'),
    ('Store 2', 'Electronics', 'Second Floor', '10:00 AM', '08:00 PM', '9876543210', 'store2@example.com', 'www.store2.com'),
    ('Store 3', 'Books', 'Third Floor', '09:30 AM', '08:30 PM', '9998887776', 'store3@example.com', 'www.store3.com'),
    ('Store 4', 'Food', 'Food Court', '10:30 AM', '09:30 PM', '8887776665', 'store4@example.com', 'www.store4.com'),
    ('Store 5', 'Toys', 'Ground Floor', '09:00 AM', '08:00 PM', '7776665554', 'store5@example.com', 'www.store5.com'),
    ('Store 6', 'Cosmetics', 'First Floor', '10:00 AM', '09:00 PM', '6665554443', 'store6@example.com', 'www.store6.com'),
    ('Store 7', 'Sporting Goods', 'Second Floor', '09:30 AM', '08:30 PM', '5554443332', 'store7@example.com', 'www.store7.com'),
    ('Store 8', 'Home Decor', 'Third Floor', '10:30 AM', '09:30 PM', '4443332221', 'store8@example.com', 'www.store8.com'),
    ('Store 9', 'Jewelry', 'Ground Floor', '09:00 AM', '08:00 PM', '3332221110', 'store9@example.com', 'www.store9.com'),
    ('Store 10', 'Appliances', 'First Floor', '10:00 AM', '09:00 PM', '2221110009', 'store10@example.com', 'www.store10.com'),
    ('Store 11', 'Footwear', 'Second Floor', '09:30 AM', '08:30 PM', '1110009998', 'store11@example.com', 'www.store11.com'),
    ('Store 12', 'Accessories', 'Third Floor', '10:30 AM', '09:30 PM', '0009998887', 'store12@example.com', 'www.store12.com'),
    ('Store 13', 'Stationery', 'Ground Floor', '09:00 AM', '08:00 PM', '9998887776', 'store13@example.com', 'www.store13.com'),
    ('Store 14', 'Health & Beauty', 'First Floor', '10:00 AM', '09:00 PM', '8887776665', 'store14@example.com', 'www.store14.com'),
    ('Store 15', 'Furniture', 'Second Floor', '09:30 AM', '08:30 PM', '7776665554', 'store15@example.com', 'www.store15.com'),
    ('Store 16', 'Pet Supplies', 'Third Floor', '10:30 AM', '09:30 PM', '6665554443', 'store16@example.com', 'www.store16.com'),
    ('Store 17', 'Art & Craft', 'Ground Floor', '09:00 AM', '08:00 PM', '5554443332', 'store17@example.com', 'www.store17.com'),
    ('Store 18', 'Eyewear', 'First Floor', '10:00 AM', '09:00 PM', '4443332221', 'store18@example.com', 'www.store18.com'),
    ('Store 19', 'Automotive', 'Second Floor', '09:30 AM', '08:30 PM', '3332221110', 'store19@example.com', 'www.store19.com'),
    ('Store 20', 'Luggage', 'Third Floor', '10:30 AM', '09:30 PM', '2221110009', 'store20@example.com', 'www.store20.com'),
    
]

cursor.executemany("INSERT INTO MALL_RECORD (STORE_NAME, CATEGORY, LOCATION, OPENING_TIME, CLOSING_TIME, CONTACT_NUMBER, EMAIL, WEBSITE) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", data)

connection.commit()


print("The inserted Records are ")
data = cursor.execute("SELECT * FROM MALL_RECORD;")
for row in data:
    print(row)

connection.close()
