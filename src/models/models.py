from typing import List
from sqlalchemy import func, ForeignKey, Integer, DateTime, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from datetime import datetime
from src.database.database import engine

class Base(DeclarativeBase):
    pass

class Video(Base):
    __tablename__ = "videos"


    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    creator_id: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    video_created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    views_count: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)
    likes_count: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)
    comments_count: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)
    reports_count: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)


    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())


    snapshots: Mapped[List["VideoSnapshot"]] = relationship("VideoSnapshot", back_populates="video", cascade="all, delete-orphan")


class VideoSnapshot(Base):
    __tablename__ = "video_snapshots"


    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    video_id: Mapped[int] = mapped_column(Integer, ForeignKey("videos.id", ondelete="CASCADE"), index=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, index=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    views_count: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)
    likes_count: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)
    comments_count: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)
    reports_count: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)
    delta_views_count: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)
    delta_likes_count: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)
    delta_comments_count: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)
    delta_reports_count: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)


    video: Mapped[Video] = relationship("Video", back_populates="snapshots")


async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def inserd_test_data(file_name: str):
