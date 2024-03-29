import mysql.connector

class PersonDa:
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

    def save(self,name, family, phone):
        self.connect()
        self.cursor.execute("INSERT INTO PERSON (name, family, phone) VALUES (%s,%s)",
                            [name, family])
        self.connection.commit()
        self.disconnect()

    def edit(self,id, name, family, phone):
        self.connect()
        self.cursor.execute("UPDATE PERSON SET NAME=%s, FAMILY=%s, phone=%s WHERE ID=%s",
                            [name,family,phone,id])
        self.connection.commit()
        self.disconnect()

    def remove(self,id):
        self.connect()
        self.cursor.execute("DELETE FROM PERSON WHERE ID=%s",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM PERSON ORDER BY FAMILY")
        person_list = self.cursor.fetchall()
        self.disconnect()
        return person_list if person_list else None


    def find_by_id(self,id):
        self.connect()
        self.cursor.execute("SELECT * FROM PERSON WHERE ID=%s",
                            [id])
        person = self.cursor.fetchall()
        self.disconnect()
        return person[0] if person else None