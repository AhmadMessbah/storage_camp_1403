import mysql.connector

class productDa:
    def connect(self,):
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

    def save(self,name, brand, count, price_b, price_s):
        self.connect()
        self.cursor.execute("INSERT INTO product (name, brand, count, price_b, price_s) VALUES (%s,%s,%s,%s,%s)",
                            [name,brand,count,price_b,price_s])
        self.connection.commit()
        self.disconnect()

    def edit(self, count, price_b, price_s, id):
        self.connect()
        self.cursor.execute("UPDATE product SET count=%s, price_b=%s,  price_s=%s WHERE ID=%s",
                            [count, price_b, price_s, id])
        self.connection.commit()
        self.disconnect()

    def remove(self,id):
        self.connect()
        self.cursor.execute("DELETE FROM product WHERE ID=%s",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM product ORDER BY NAME")
        product_list = self.cursor.fetchall()
        self.disconnect()
        return product_list if product_list else None


    def find_by_id(self,id):
        self.connect()
        self.cursor.execute("SELECT * FROM product WHERE ID=%s",
                            [id])
        product = self.cursor.fetchall()
        self.disconnect()
        return product[0] if product else None