from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, Date, JSON
from uuid import uuid4
from datetime import datetime

from config.database import Base


__all__ = ['TestModel']


class Test(Base):
    __tablename__ = 'system_test'
    __table_args__ = {
        'comment': '测试模型表',
    }
    
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    url = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    balance = Column(Float, nullable=False)
    is_active = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    birth_date = Column(Date, nullable=False)
    meta = Column(JSON, nullable=False)



system_test = Test.__table__