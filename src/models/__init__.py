from src.database.todolist import db

tags_tasks_association = db.Table(
    "tags_tasks",
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"), primary_key=True),
    db.Column("task_id", db.Integer, db.ForeignKey("tasks.id"), primary_key=True),
)
