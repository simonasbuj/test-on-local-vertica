import vertica_python

class Service:

    def __init__(self):
        self.config = {"vertica_conn": {"password": "password", "host": "myhost"}}

        self.vertica_conn = self.config.get("vertica_conn")
    
    def query_vertica(self, query):
        with vertica_python.connect(**self.vertica_conn) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()

        return results