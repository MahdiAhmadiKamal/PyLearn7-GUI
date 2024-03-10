import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect("alarm_database.db")
        self.cursor = self.con.cursor()

    def get_alarms(self):
        query = "SELECT * FROM alarms_table"
        result = self.cursor.execute(query)
        tasks = result.fetchall()
        return tasks
    
    def add_new_alarm(self, new_time, new_name):
        try:
            query = f"INSERT INTO alarms_table(time, name) VALUES('{new_time}', '{new_name}')"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False
        
    def remove_an_alarm(self, id):
        try:
            query = f"DELETE FROM alarms_table WHERE id='{id}'"    
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False
        
    def edit_an_alarm(self, id, edited_time):

        try:
            query = f"UPDATE alarms_table SET time='{edited_time}' WHERE id='{id}'"     
            result = self.cursor.execute(query)
            # result.fetchone()
            self.con.commit()
            return True
        except:
            return False
        
    def alarm_done(self, id, situation):
        query = f"UPDATE alarms_table SET is_done='{situation}' WHERE id='{id}'"  
        self.cursor.execute(query)
        self.con.commit()
