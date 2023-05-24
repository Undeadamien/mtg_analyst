import pandas as pd
import matplotlib.pyplot as plt


def plot_reprint(df: pd.DataFrame):

    total_print = df.shape[0]

    df = df["isReprint"]\
        .value_counts()\
        .rename({0: "original card", 1: "reprint"})

    plot = df.plot(kind="pie", autopct="%1.1f%%", ylabel="",
                   title=f"From {total_print} printed card")


def card_by_artist(df: pd.DataFrame):

    df["mask"] = df["artist"].str.contains("&")

    # remove the two sided cards
    df = df[["artist", "name", "mask"]]\
        .drop_duplicates()

    # seperate the solo and duo illustration
    df_solo = df[~df["mask"]]\
        .value_counts("artist")\
        .sort_values(ascending=True)

    df_duo = df[df["mask"]]\
        .value_counts("artist")\
        .sort_values(ascending=True)

    # start plotting
    fig, axes = plt.subplots(nrows=2)
    fig.suptitle("Number of cards illustrated per artist")

    solo_plot = df_solo.plot(kind="line", ax=axes[1])
    solo_plot.tick_params("x", which="both", bottom=False, labelbottom=False)
    solo_plot.set_xlabel(f"{df_solo.shape[0]} unique artist")
    solo_plot.set_title("")

    duo_plot = df_duo.plot(kind="line", ax=axes[0])
    duo_plot.tick_params("x", which="both", bottom=False, labelbottom=False)
    duo_plot.set_xlabel(f"{df_duo.shape[0]} different duo of artist")
    duo_plot.set_title("")


def main():

    df = pd.read_csv("./raw_data/cards.csv")
    df = df.dropna(subset=["artist", "name", "isReprint"])

    plot_reprint(df)
    card_by_artist(df)

    plt.show()


if __name__ == "__main__":
    main()
