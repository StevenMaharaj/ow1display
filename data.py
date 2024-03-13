import asyncio
import json
from typing import Any

# import pandas as pd
# import requests
import websockets


def get_deribit_options_data() -> dict[str, Any]:
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


# data = get_deribit_options_data()
# print(data))
