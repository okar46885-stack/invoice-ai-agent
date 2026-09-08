from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Text, DateTime, JSON
from sqlalchemy.sql import func

Base = declarative_base()

class CopilotSuggestion(Base):
    __tablename__ = "copilot_suggestions"
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(String, index=True, nullable=False)
    field_name = Column(String, nullable=False)
    suggestion_value = Column(Text, nullable=False)
    confidence = Column(Float, nullable=False)
    provenance = Column(JSON, nullable=True)
    reason = Column(Text, nullable=True)
    provider = Column(String, nullable=True)
    status = Column(String, default="proposed", nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class CopilotFeedback(Base):
    __tablename__ = "copilot_feedback"
    id = Column(Integer, primary_key=True, index=True)
    suggestion_id = Column(Integer, nullable=True)
    document_id = Column(String, index=True, nullable=True)
    field_name = Column(String, nullable=True)
    action = Column(String, nullable=False)
    corrected_value = Column(Text, nullable=True)
    reviewer_id = Column(String, nullable=False)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class CopilotAuditLog(Base):
    __tablename__ = "copilot_audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String, nullable=False)
    payload = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
