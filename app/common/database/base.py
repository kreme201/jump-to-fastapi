from datetime import datetime

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

from app.common.database.session import session


class CustomBase:
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime, nullable=True)

    query = session.query_property()

    def save(self):
        if self.id is None:
            self.created = datetime.now()
        else:
            self.updated = datetime.now()

        session.add(self)
        return self

    def delete(self):
        session.delete(self)
        return self


Base = declarative_base(cls=CustomBase)
