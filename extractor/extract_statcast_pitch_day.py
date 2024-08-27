from pydantic import BaseModel, field_validator
from pybaseball import statcast
from datetime import datetime
import pandas as pd


class DateValidator(BaseModel):
    query_date: str

    @field_validator('query_date')
    @classmethod
    def validate_date_format(cls, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError(f'{value} is not a valid date in the format YYYY-MM-DD')
        return value


def get_statcast_pitch_day(query_date: str) -> pd.DataFrame:
    # Validate the date string
    DateValidator(query_date=query_date)

    df_statcast_pitch_day = statcast(
        start_dt=query_date
    )

    # Sort the data frame
    # this is to ensure that primary key downstream is sequential for each pitch of each game
    sorted_df = df_statcast_pitch_day.sort_values(by=[
            'game_date',
            'game_pk',
            'inning',
            'inning_topbot',
            'at_bat_number',
            'pitch_number'
        ],
        ascending=[
            True,
            True,
            True,
            False,
            True,
            True
        ]
    )

    return sorted_df
