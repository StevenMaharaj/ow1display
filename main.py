import pandas as pd

# from data import get_deribit_options_data


def main():
    # data = get_deribit_options_data()
    # df = pd.DataFrame(data["result"])

    # df.to_csv("deribit_options.csv", index=False)
    df = pd.read_csv("deribit_options.csv")
    df.dropna(inplace=True)
    df = df[
        [
            "instrument_name",
            "bid_price",
            "ask_price",
            "underlying_price",
            "interest_rate",
        ]
    ]
    df["instrument_name"] = df["instrument_name"].astype(str)
    df["strike"] = df["instrument_name"].apply(lambda x: float(x.split("-")[2]))
    print(df.head())
    # print(df.info())


if __name__ == "__main__":
    main()


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
