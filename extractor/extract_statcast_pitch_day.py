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

    return df_statcast_pitch_day
