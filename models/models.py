from sqlalchemy import MetaData, Table, Column, \
    Integer, String, TIMESTAMP, ForeignKey, JSON
from datetime import datetime

metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    # primary_key=True уникальное значение перыичный ключь
    Column("id", Integer, primary_key=True),
    # nullable=False означает что запрещено значение null, none
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

users =Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    # TIMESTAMP, default=datetime.utcnow это время когда была \
    # сделана регистрация
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    # внешений ключь на таблицу id
    Column("role_id", Integer, ForeignKey("roles_id")),
)

# alembic init migrations применяем команду в терминале


