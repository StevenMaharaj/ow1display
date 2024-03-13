from typing import Any, Dict

import pandas as pd

import deribit as dbt


def get_data(exchange: str) -> pd.DataFrame:
    if exchange == "deribit":
        # For Production
        # data: Dict[str, Any] = dbt.get_deribit_options_data()
        # df = pd.DataFrame(data["result"])

        # For Testing
        df = pd.read_csv("deribit_options.csv")

        # df.to_csv("deribit_options.csv", index=False)

        # clean up the data
        df = dbt.clean(df)
        return df
    else:
        return None
