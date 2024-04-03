import mysql.connector


class PersonData:
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

    def save(self, name, family, phone):
        self.connect()
        self.cursor.execute("insert into person (name, family, phone) values (%s,%s,%s)",
                            [name, family, phone])
        self.connection.commit()
        self.disconnect()

    def edit(self, id_to_edit, name, family, phone):
        self.connect()
        self.cursor.execute("update person set name=%s, family=%s, phone=%s where person_id=%s",
                            [name, family, phone, id_to_edit])
        self.connection.commit()
        self.disconnect()

    def remove(self, id_to_remove):
        self.connect()
        self.cursor.execute("delete from person where person_id=%s",
                            [id_to_remove])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from person order by family")
        person_list = self.cursor.fetchall()
        self.disconnect()
        return person_list if person_list else None

    def find_by_id(self, id_to_find):
        self.connect()
        self.cursor.execute("select * from person where person_id=%s",
                            [id_to_find])
        person = self.cursor.fetchall()
        self.disconnect()
        return person[0] if person else None
