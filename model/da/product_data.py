import mysql.connector


class ProductData:
    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="mft"
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, name, brand, quantity, buyer_price, seller_price):
        self.connect()
        self.cursor.execute(
            "INSERT INTO PRODUCT (name, brand, quantity, buyer_price, seller_price) VALUES (%s,%s,%s,%s,%s)",
            [name, brand, quantity, buyer_price, seller_price])
        self.connection.commit()
        self.disconnect()

    def edit(self, quantity, buyer_price, seller_price, id):
        self.connect()
        self.cursor.execute("UPDATE PRODUCT SET name=%s, brand=%s, quantity=%s, buyer_price=%s,  seller_price=%s WHERE ID=%s",
                            [quantity, buyer_price, seller_price, id])
        self.connection.commit()
        self.disconnect()

    def remove(self, id):
        self.connect()
        self.cursor.execute("DELETE FROM PRODUCT WHERE ID=%s",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM PRODUCT ORDER BY NAME")
        product_list = self.cursor.fetchall()
        self.disconnect()
        return product_list if product_list else None

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("SELECT * FROM PRODUCT WHERE ID=%s",
                            [id])
        product = self.cursor.fetchall()
        self.disconnect()
        return product[0] if product else None
