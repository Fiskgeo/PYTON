
from sqlalchemy import create_engine, text

class TeacherTable:

    @staticmethod
    def insert_teacher(session, email, group_id=1):
        """Простая вставка учителя"""
        session.execute(
            text("INSERT INTO teacher (email, group_id) VALUES (:email, :group_id)"),
            {"email": email, "group_id": group_id}
        )
        session.commit()
        return email

    @staticmethod
    def get_count(session):
        return session.execute(text("SELECT COUNT(*) FROM teacher")).scalar()

    @staticmethod
    def get_teacher_by_email(session, email):
        result = session.execute(
            text("SELECT teacher_id, email, group_id FROM teacher WHERE email = :email"),
            {"email": email}
        ).fetchone()
        if result:
            return {"id": result[0], "email": result[1], "group_id": result[2]}
        return None

    @staticmethod
    def update_teacher_email(session, old_email, new_email):
        session.execute(
            text("UPDATE teacher SET email = :new_email WHERE email = :old_email"),
            {"new_email": new_email, "old_email": old_email}
        )
        session.commit()

    @staticmethod
    def delete_teacher(session, email):
        session.execute(
            text("DELETE FROM teacher WHERE email = :email"),
            {"email": email}
        )
        session.commit()