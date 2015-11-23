from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
attendance = Table('attendance', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('people', Integer),
    Column('date', DateTime),
    Column('court_id', Integer),
)

court = Table('court', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('address', String(length=128)),
    Column('lat', Float),
    Column('lng', Float),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['attendance'].create()
    post_meta.tables['court'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['attendance'].drop()
    post_meta.tables['court'].drop()
