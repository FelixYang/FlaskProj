#_*_coding:utf-8_*_

from sqlalchemy.orm import mapper, sessionmaker
from datetime import datetime
from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, Date, Unicode, String
from sqlalchemy import create_engine

engine = create_engine("sqlite:/// cc_info.db", echo=False)
metadata = MetaData()

ptv_info = Table ("ptv_info", metadata,
                   Column("employ_id", Unicode(10), primary_key=True),
                   Column("user_id", Unicode(6), unique=True, nullable=False),
                   Column("name", Unicode(16), unique=True, nullable=False),
                   Column("email", Unicode(255),unique=True, nullable=False),
                   Column("password", Unicode(40), default="Aa123456",nullable=False),
                   Column("first_name", Unicode(255), default="张"),
                   Column("last_name", Unicode(255), default="三")
                )

proj_info = Table("porj_info", metadata,
                  Column("model_num", Unicode(20), primary_key=True),
                  Column("project_num", Unicode(20), unique=True, nullable=False),
                  Column("custom", Unicode(255), nullable=False)
)

team_info = Table("team_info", metadata,
                Column('model_num', Unicode(255),primary_key=True, ForeignKey('porj_info.model_num')),
                Column("PM", Unicode(255), nullable=False),
                Column("QPTV", Unicode(255), nullable=False),
                Column("SW", Unicode(255), nullable=True),
                Column("ME", Unicode(255), nullable=True),
                Column("EE", Unicode(255), nullable=True),
                Column("PTV", Unicode(255), nullable=True),
                Column("PQM", Unicode(255), nullable=True),
                Column("SQM", Unicode(255), nullable=True),
                Column("PUR", Unicode(255), nullable=True),
                Column("PE", Unicode(255), nullable=True),
                Column("ME", Unicode(255), nullable=True),
                )

metadata.create_all(engine)