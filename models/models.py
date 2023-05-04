import sqlalchemy
from sqlalchemy import MetaData, Table, Column, \
    Integer, String, TIMESTAMP, ForeignKey, JSON
from datetime import datetime

metadata = MetaData()

# primary_key=True уникальное значение перыичный ключь
# nullable=False означает что запрещено значение null, none

roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

# TIMESTAMP, default=datetime.utcnow это время когда была \
# сделана регистрация
# внешений ключь на таблицу id
# "role_id" сылается на верхнию таблицу roles

users =Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey("roles.id")),
)

# alembic init migrations применяем команду в терминале

# engine = sqlalchemy.create_engine(DATABASE_URL)
# metadata=create_all(engine)

