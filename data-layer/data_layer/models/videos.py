from data_layer.models.base import Base
import sqlalchemy as sql

class Video:
    __tablename__ = 'video'
    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String)
    description = sql.Column(sql.String)

    def __repr__(self):
        return f"<Note (id={self.id}, title={self.title})>"