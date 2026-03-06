


from datetime import datetime, timezone
from typing import Union
import uuid
from sqlalchemy import UUID, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.database.base import Base


class Skill(Base):
	__tablename__ = "skills"
	
	id: Mapped[uuid.UUID] = mapped_column(
		UUID(as_uuid=True),
		primary_key=True,
		default=uuid.uuid4
	)
	
	user_id: Mapped[uuid.UUID] = mapped_column(
		ForeignKey("users.id")
	)
	
	name: Mapped[str] = mapped_column(
		unique=True
	)
	
	is_completed: Mapped[bool] = mapped_column(
		default=False
	)
	
	created_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True),
		default=lambda: datetime.now(timezone.utc)
	)
	
	updated_at: Mapped[Union[datetime, None]] = mapped_column(
		DateTime(timezone=True),
		default=lambda: datetime.now(timezone.utc),
		onupdate=lambda: datetime.now(timezone.utc)
	)

