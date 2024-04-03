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
            "insert into product (name, brand, quantity, buyer_price, seller_price) values (%s,%s,%s,%s,%s)",
            [name, brand, quantity, buyer_price, seller_price])
        self.connection.commit()
        self.disconnect()

    def edit(self, id_to_edit, name, brand, quantity, buyer_price, seller_price):
        self.connect()
        self.cursor.execute(
            "update product set name=%s, brand=%s, quantity=%s, buyer_price=%s,  seller_price=%s where product_id=%s",
            [name, brand, quantity, buyer_price, seller_price, id_to_edit])
        self.connection.commit()
        self.disconnect()

    def remove(self, id_to_remove):
        self.connect()
        self.cursor.execute("delete from product where product_id=%s",
                            [id_to_remove])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from product order by name")
        product_list = self.cursor.fetchall()
        self.disconnect()
        return product_list if product_list else None

    def find_by_id(self, id_to_search):
        self.connect()
        self.cursor.execute("select * from product where product_id=%s",
                            [id_to_search])
        product = self.cursor.fetchall()
        self.disconnect()
        return product[0] if product else None
