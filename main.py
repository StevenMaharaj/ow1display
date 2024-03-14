from data import get_data


def main():
    # data = get_deribit_options_data()

    df = get_data("deribit")
    print(df[["symbol", "mid", "S", "IV", "d", "g"]])
    print(df.info())


if __name__ == "__main__":
    main()
