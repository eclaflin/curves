from extractor.extract_statcast_pitch_day import get_statcast_pitch_day
from .engine import engine as db
from models.statcast_pitch_day_models import Base, PitchDTO

from sqlalchemy.orm import sessionmaker

import pandas as pd

Session = sessionmaker(bind=db)
session = Session()

Base.metadata.create_all(db)


def load_statcast_pitch(date):
    pitch_date = date #input("Enter date to retrieve Statcast pitches from: ")

    df_pitch = get_statcast_pitch_day(pitch_date)

    for column in df_pitch.columns:
        df_pitch[column] = df_pitch[column].apply(lambda x: None if pd.isna(x) else x)

    # Insert data into the database
    for index, row in df_pitch.iterrows():
        new_row = PitchDTO(
            pitch_type=row['pitch_type'],
            game_date=row['game_date'],
            release_speed=row['release_speed'],
            release_pos_x=row['release_pos_x'],
            release_pos_z=row['release_pos_z'],
            player_name=row['player_name'],
            batter=row['batter'],
            pitcher=row['pitcher'],
            events=row['events'],
            description=row['description'],
            spin_dir=row['spin_dir'],
            spin_rate_deprecated=row['spin_rate_deprecated'],
            break_angle_deprecated=row['break_angle_deprecated'],
            break_length_deprecated=row['break_length_deprecated'],
            zone=row['zone'],
            des=row['des'],
            game_type=row['game_type'],
            stand=row['stand'],
            p_throws=row['p_throws'],
            home_team=row['home_team'],
            away_team=row['away_team'],
            type=row['type'],
            hit_location=row['hit_location'],
            bb_type=row['bb_type'],
            balls=row['balls'],
            strikes=row['strikes'],
            game_year=row['game_year'],
            pfx_x=row['pfx_x'],
            pfx_z=row['pfx_z'],
            plate_x=row['plate_x'],
            plate_z=row['plate_z'],
            on_3b=row['on_3b'],
            on_2b=row['on_2b'],
            on_1b=row['on_1b'],
            outs_when_up=row['outs_when_up'],
            inning=row['inning'],
            inning_topbot=row['inning_topbot'],
            hc_x=row['hc_x'],
            hc_y=row['hc_y'],
            tfs_deprecated=row['tfs_deprecated'],
            tfs_zulu_deprecated=row['tfs_zulu_deprecated'],
            fielder_2=row['fielder_2'],
            umpire=row['umpire'],
            sv_id=row['sv_id'],
            vx0=row['vx0'],
            vy0=row['vy0'],
            vz0=row['vz0'],
            ax=row['ax'],
            ay=row['ay'],
            az=row['az'],
            sz_top=row['sz_top'],
            sz_bot=row['sz_bot'],
            hit_distance_sc=row['hit_distance_sc'],
            launch_speed=row['launch_speed'],
            launch_angle=row['launch_angle'],
            effective_speed=row['effective_speed'],
            release_spin_rate=row['release_spin_rate'],
            release_extension=row['release_extension'],
            game_pk=row['game_pk'],
            pitcher_1=row['pitcher.1'],
            fielder_2_1=row['fielder_2.1'],
            fielder_3=row['fielder_3'],
            fielder_4=row['fielder_4'],
            fielder_5=row['fielder_5'],
            fielder_6=row['fielder_6'],
            fielder_7=row['fielder_7'],
            fielder_8=row['fielder_8'],
            fielder_9=row['fielder_9'],
            release_pos_y=row['release_pos_y'],
            estimated_ba_using_speedangle=row['estimated_ba_using_speedangle'],
            estimated_woba_using_speedangle=row['estimated_woba_using_speedangle'],
            woba_value=row['woba_value'],
            woba_denom=row['woba_denom'],
            babip_value=row['babip_value'],
            iso_value=row['iso_value'],
            launch_speed_angle=row['launch_speed_angle'],
            at_bat_number=row['at_bat_number'],
            pitch_number=row['pitch_number'],
            pitch_name=row['pitch_name'],
            home_score=row['home_score'],
            away_score=row['away_score'],
            bat_score=row['bat_score'],
            fld_score=row['fld_score'],
            post_away_score=row['post_away_score'],
            post_home_score=row['post_home_score'],
            post_bat_score=row['post_bat_score'],
            post_fld_score=row['post_fld_score'],
            if_fielding_alignment=row['if_fielding_alignment'],
            of_fielding_alignment=row['of_fielding_alignment'],
            spin_axis=row['spin_axis'],
            delta_home_win_exp=row['delta_home_win_exp'],
            delta_run_exp=row['delta_run_exp'],
            bat_speed=row['bat_speed'],
            swing_length=row['swing_length'],
        )
        session.add(new_row)

    session.commit()
