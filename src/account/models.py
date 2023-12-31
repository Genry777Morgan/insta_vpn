from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean, MetaData, BigInteger
from database import Base


metadata = MetaData()


class Account(Base):
    __tablename__ = "account"

    metadata = metadata
    id = Column(BigInteger, primary_key=True, autoincrement=False)
    name = Column(String)
    number = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
