import matplotlib.pyplot as plt
import pandas as pd


def plot_reprint(df: pd.DataFrame):
    """
    Plot a pie, showing the percentage of cards who are reprint of others cards
    """

    df = df.dropna(subset=["artist", "name", "isReprint"])

    total_print = df.shape[0]
    df = df["isReprint"].value_counts()
    df = df.rename({0: "original card", 1: "reprint"})

    plot = df.plot(kind="pie", autopct="%1.1f%%", ylabel="",
                   title=f"From {total_print} printed card")

    plt.show()


def plot_artist(df: pd.DataFrame):
    """
    Plot the number of card by each illustrated by each artist,
    seperate the cards illustrated by one artist and the cards illustrated
    by a duo of artist.
    """

    df = df.dropna(subset=["artist", "name", "isReprint"])

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

    plt.show()


def plot_mana_cost(df: pd.DataFrame):
    """
    Plot the cards by their mana cost
    """

    df = df.drop_duplicates(subset=["name", "manaValue"])\
        .value_counts("manaValue")\
        .sort_index()\

    plot = df.plot(kind="bar", rot=0)
    plot.bar_label(plot.containers[0])
    plot.tick_params("y", which="both", left=False, labelleft=False)
    plot.set_xlabel("Mana value")
    plot.set_title("")

    plt.show()


def main():

    df = pd.read_csv("./cards.csv")

    plot_mana_cost(df)
    plot_reprint(df)
    plot_artist(df)

if __name__ == "__main__":
    main()
