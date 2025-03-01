from sqlalchemy import Column, Integer, Float, DateTime
from database.db import Base
from datetime import datetime

class SensorData(Base):
    __tablename__ = 'sensor_data'

    id = Column(Integer, primary_key=True)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    motion = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
