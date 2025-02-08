def execute_query(self, cursor, query):
    try:
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    except Exception as e:
        print(f"Error executing query: {e}")
        return None