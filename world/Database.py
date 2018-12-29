import mysql.connector


class Database(object):
    """
    Connects and interacts with a MySQL database.
    """

    def __init__(self, config):
        self.config = config
        # Test database connection
        self.connect()
        self.disconnect()
        print("[Database] Connection successful")

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(**self.config["database"])
        except mysql.connector.Error as e:
            print("[Database] Could not connect to MySQL database: {}".format(e))

    def disconnect(self):
        try:
            self.cnx.close()
        except Exception as e:
            print("[Database] Could not close MySQL database: {}".format(e))

    def select(self, table, where, search):
        """Selects one row of data."""
        self.connect()
        # Returns as dictionary with columns
        cursor = self.cnx.cursor(dictionary=True)
        query = "SELECT * FROM {} WHERE {} = '{}'".format(table, where, search)
        data = None

        try:
            cursor.execute(query)
            data = cursor.fetchone()
            # Strings every value in dict
            data = {i: str(data[i]) for i in data}
        except Exception as e:
            print("Select query failed: {}".format(e))
            self.cnx.rollback()
        finally:
            cursor.close()
            self.disconnect()
            return data

    def update(self, table, field, new, where, search):
        """Updates data."""
        self.connect()
        cursor = self.cnx.cursor()
        query = "UPDATE {} SET {} = '{}' WHERE {} = '{}'".format(table, field, new, where, search)

        try:
            cursor.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("[Database] Update query failed: {}".format(e))
            self.cnx.rollback()
        finally:
            cursor.close()
            self.disconnect()

    def query(self):
        """Allows for specific querying."""
        pass
