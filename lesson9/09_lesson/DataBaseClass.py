from sqlalchemy import create_engine, text

class TeacherTable:
    @staticmethod
    def insert_teacher(conn, email):
        conn.execute(text(
            "INSERT INTO teacher(email) VALUES (:email)"),
                     {"email" :email})
        #conn.commit()

    @staticmethod
    def get_count(conn):
        result = conn.execute(text(
            "SELECT COUNT (*) FROM teacher"
        )).scalar()
        return result

    @staticmethod
    def find_teacher_by_email(conn, email):
        result = conn.execute(text("SELECT teacher_id FROM teacher WHERE email = :email"),
                              {"email":email}).fetchone()
        if result:
            return  result[0]
        return None

    @staticmethod
    def get_teacher_by_id(conn, teacher_id):
        result = conn.execute(text("SELECT teacher_id, email FROM teacher WHERE teacher_id = :id"), {"id": teacher_id}).fetchone()
        if result:
            return {"id": result[0], "email":result[1]}
        return None

    @staticmethod
    def update_teacher_email(conn, teacher_id, new_email):
        conn.execute(text("UPDATE teacher SET email =:new_email WHERE id = :id"),
                     {"new_email" :new_email, "id" : teacher_id})
        #conn.commit()

    @staticmethod
    def delete_teacher(conn, email):
        conn.execute(text("DELETE FROM teacher WHERE email = :email"), {"email": email})
        #conn.commit()

    @staticmethod
    def delete_teacher_by_id(conn, teacher_id):
        conn.execute(text("DELETE FROM teacher WHERE id = :id"), {"id": teacher_id})
        #conn.commit()