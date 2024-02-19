import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect("D:/PyLearn7/Class codes/session 22/todo_list.db")
        self.cursor = self.con.cursor()

    def get_tasks(self):
        query = "SELECT * FROM tasks"
        result = self.cursor.execute(query)
        tasks = result.fetchall()
        return tasks
    
    def add_new_task(self, new_title, new_description):
        try:
            query = f"INSERT INTO tasks(title, description) VALUES('{new_title}', '{new_description}')"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False
        
    def remove_a_task(self, id):
        try:
            query = f"DELETE FROM tasks WHERE id='{id}'"        #B
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False

    def task_done(self, id, situation):
        query = f"UPDATE tasks SET is_done='{situation}' WHERE id='{id}' "    #A
        self.cursor.execute(query)
        self.con.commit()