"""
    Import data from a local CSV file to a PostgreSQL database table using pandas and psycopg2. 'null' values in the CSV file get replaced by real NULL values.

    Source:
    https://gist.github.com/stefanthoss/0443a0368abca44863bccb8e51103e23
"""

import pandas
import numpy
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.types import *


engine = create_engine('postgresql+psycopg2://postgres:HoangChi181116@localhost:5432/Economic_And_Growth_Indicators_For_VN')

columns = [
    'country_name',
    'country_iso3',
    'year',
    'indicator_name',
    'indicator_code',
    'value'
]

dataframe = pandas.read_csv(
    'economy-and-growth-indicators-for-vietnam-1.csv', names=columns
) # .replace(to_replace='null', value=numpy.NaN)

dataframe.drop([0, 1]).to_sql(
    'Economic_Information',
    engine,
    index=False,
    if_exists='replace',
    dtype={
        'country_name': String(),
        'country_iso3': String(),
        'year': Integer(),
        'indicator_name': String(),
        'indicator_code': String(),
        'value': Float()
    }
)