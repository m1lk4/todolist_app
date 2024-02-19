from datetime import datetime

from src.database.todolist_db import db


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    due_date = db.Column(db.DateTime)
    status = db.Column(db.String, default="New")
    priority = db.Column(db.String)
    list_id = db.Column(db.Integer, db.ForeignKey("lists.id"))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    list = db.relationship("List", back_populates="tasks")
