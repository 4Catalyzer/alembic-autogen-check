import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
OutOfSyncBase = declarative_base()


class Widget(Base):
    __tablename__ = "widgets"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, index=True)


class WidgetUpdated(OutOfSyncBase):
    __tablename__ = "widgets"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
