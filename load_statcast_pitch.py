from extractor.extract_statcast_pitch_day import get_statcast_pitch_day
from loader.engine import engine as db

from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()


class PitchDTO(Base):
    __tablename__ = 'statcast_pitch'
    id = Column(Integer, primary_key=True, autoincrement=True)
    game_pk = Column(Integer)
    pitch_number = Column(Integer)
    at_bat_number = Column(Integer)
    game_date = Column(Date)


def load_statcast_pitch():
    pitch_date = input("Enter date to retrieve Statcast pitches from: ")

    df_pitch = get_statcast_pitch_day(pitch_date)

    # Create table if it doesn't exist
    Base.metadata.create_all(db)

    # Insert data into the database
    for index, row in df_pitch.iterrows():
        new_row = PitchDTO(
            game_pk=row['game_pk'],
            pitch_number=row['pitch_number'],
            at_bat_number=row['at_bat_number'],
            game_date=row['game_date']
        )
        session.add(new_row)

    session.commit()


if __name__ == '__main__':

    load_statcast_pitch()
