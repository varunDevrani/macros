import uuid
from datetime import datetime, timezone
from typing import Union

from sqlalchemy import UUID, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4
    )

    first_name: Mapped[Union[str, None]] = mapped_column()

    last_name: Mapped[Union[str, None]] = mapped_column()

    email: Mapped[str] = mapped_column()

    password_hash: Mapped[str] = mapped_column()

    profile_pic_url: Mapped[Union[str, None]] = mapped_column()

    is_verfied: Mapped[bool] = mapped_column(
    	default=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    deleted_at: Mapped[Union[datetime, None]] = mapped_column(
    	DateTime(timezone=True)
    )
