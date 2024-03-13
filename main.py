import pandas as pd

from data import get_data


def main():
    # data = get_deribit_options_data()

    DeribitDf = get_data("deribit")
    print(DeribitDf.head())
    # print(df.info())


if __name__ == "__main__":
    main()
