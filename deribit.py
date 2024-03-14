import asyncio
import json
from datetime import datetime
from typing import Any

import pandas as pd
import websockets
from dateutil import tz


def fetch_data() -> dict[str, Any]:
    # Get the data from the Deribit API
    # ...
    msg = {
        "jsonrpc": "2.0",
        "id": 8772,
        "method": "public/get_book_summary_by_currency",
        "params": {"currency": "BTC", "kind": "option"},
    }

    async def call_api(msg):
        async with websockets.connect("wss://test.deribit.com/ws/api/v2") as websocket:
            await websocket.send(msg)
            while websocket.open:
                response = await websocket.recv()
                # do something with the response...
                response_json = json.loads(response)
                return response_json

    data = asyncio.get_event_loop().run_until_complete(call_api(json.dumps(msg)))
    if data is None:
        raise ValueError("No data returned from Deribit API")
    return data


def clean(df_raw: pd.DataFrame) -> pd.DataFrame:
    # Clean up the data
    # ...
    df_raw.dropna(axis=0, inplace=True)
    df = df_raw.rename(
        {
            "instrument_name": "symbol",
            "ask_price": "ask",
            "bid_price": "bid",
            "interest_rate": "r",
        },
        axis=1,
    )
    df["mid"] = (df["ask"] + df["bid"]) * 0.5
    df = df[["symbol", "bid", "mid", "ask", "r"]]

    if type(df) is not pd.DataFrame:
        raise ValueError("Data is not a pandas DataFrame")

    df["strike"] = df["symbol"].str.extract(r"-(\d+00)-").astype(float)
    explist = (
        df["symbol"].str.extract(r"(\d{2}[A-Z]+\d{2})").astype(str).values.flatten()
    )
    exp = list(map(exp_to_date, explist))

    df["expiry"] = exp
    return df


def exp_to_date(exp: str) -> datetime:
    day = int(exp[:2])
    month = month_to_num(exp[2:5])
    year = year_to_num(exp[5:])
    return datetime(year, month, day, 8, 0, 0, 0, tzinfo=tz.tzutc())


def year_to_num(year: str) -> int:
    year_dict = {
        "20": 2020,
        "21": 2021,
        "22": 2022,
        "23": 2023,
        "24": 2024,
        "25": 2025,
        "26": 2026,
        "27": 2027,
        "28": 2028,
        "29": 2029,
        "30": 2030,
    }
    return year_dict[year]


def month_to_num(month: str) -> int:
    month_dict = {
        "JAN": 1,
        "FEB": 2,
        "MAR": 3,
        "APR": 4,
        "MAY": 5,
        "JUN": 6,
        "JUL": 7,
        "AUG": 8,
        "SEP": 9,
        "OCT": 10,
        "NOV": 11,
        "DEC": 12,
    }
    return month_dict[month]


#  #   Column                    Non-Null Count  Dtype
# ---  ------                    --------------  -----
#  0   mid_price                 598 non-null    float64
#  1   volume_usd                598 non-null    float64
#  2   quote_currency            598 non-null    object
#  3   estimated_delivery_price  598 non-null    float64
#  4   creation_timestamp        598 non-null    int64
#  5   base_currency             598 non-null    object
#  6   underlying_index          598 non-null    object
#  7   underlying_price          598 non-null    float64
#  8   mark_iv                   598 non-null    float64
#  9   volume                    598 non-null    float64
#  10  interest_rate             598 non-null    float64
#  11  price_change              598 non-null    float64
#  12  open_interest             598 non-null    float64
#  13  ask_price                 598 non-null    float64
#  14  bid_price                 598 non-null    float64
#  15  instrument_name           598 non-null    object
#  16  mark_price                598 non-null    float64
#  17  last                      598 non-null    float64
#  18  low                       598 non-null    float64
#  19  high                      598 non-null    float64
#
