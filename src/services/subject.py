from .base import BaseService

class SubjectService(BaseService):
    table_name = "subjects"

    def fetch_subjects(self):
        try:
            return [], None
        except mysql.connector.Error as err:
            return None, f"Error: {err}"

    def create_subject(self, new_data):
        connection = self.get_database_connection()
        if not connection:
            return "Database connection not available."

        try:
            cursor = connection.cursor()
            query = f"INSERT INTO {
                self.table_name} (`order`, `code`, `name`) VALUES (%s, %s, %s)"
            cursor.execute(query, new_data)
            connection.commit()
            cursor.close()
            connection.close()
            return None
        except mysql.connector.IntegrityError as err:
            if err.errno == 1062:
                return "Duplicate code."
            return f"Error: {err}"
        except mysql.connector.Error as err:
            return f"Error: {err}"

    def update_subject(self, subject_id, new_data):
        connection = self.get_database_connection()
        if not connection:
            return "Database connection not available."

        try:
            cursor = connection.cursor()
            query = f"UPDATE {
                self.table_name} SET `order` = %s, `code` = %s, `name` = %s WHERE `id` = %s"
            cursor.execute(query, (*new_data, subject_id))
            connection.commit()
            cursor.close()
            connection.close()
            return None
        except mysql.connector.IntegrityError as err:
            if err.errno == 1062:
                return "Duplicate code."
            return f"Error: {err}"
        except mysql.connector.Error as err:
            return f"Error: {err}"

    def delete_subject(self, subject_id):
        connection = self.get_database_connection()
        if not connection:
            return "Database connection not available."

        try:
            cursor = connection.cursor()
            query = f"DELETE FROM {self.table_name} WHERE `id` = %s"
            cursor.execute(query, (subject_id,))
            connection.commit()
            cursor.close()
            connection.close()
            return None
        except mysql.connector.Error as err:
            return f"Error: {err}"
