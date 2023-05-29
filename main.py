import matplotlib.pyplot as plt
import pandas as pd
import sys


def plot_reprint() -> None:
    """
    Plot a pie, showing the percentage of cards who are reprint of others cards
    """

    df = pd.read_csv("./cards.csv", usecols=["artist", "name", "isReprint"])
    total_print = df.shape[0]
    df = df["isReprint"].value_counts().rename({0: "original card", 1: "reprint"})

    df.plot(
        kind="pie",
        autopct="%1.1f%%",
        ylabel="",
        title=f"From {total_print} printed card",
    )

    plt.show()


def plot_artist() -> None:
    """
    Plot the number of card by each illustrated by each artist,
    seperate the cards illustrated by one artist and the cards illustrated
    by a duo of artist. Some artist are in multiple duo.
    """

    df = pd.read_csv("./cards.csv", usecols=["artist", "name", "isReprint"]).dropna()
    df["mask"] = df["artist"].str.contains("&")
    df = df[["artist", "name", "mask"]].drop_duplicates()

    df_solo = df[~df["mask"]].value_counts("artist", ascending=True)
    df_duo = df[df["mask"]].value_counts("artist", ascending=True)

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


def plot_mana_cost() -> None:
    """
    Plot the cards by their mana cost
    """

    df = pd.read_csv("./cards.csv", usecols=["name", "manaValue"])
    df = df.drop_duplicates().value_counts("manaValue").sort_index()

    plot = df.plot(kind="bar", rot=0)
    plot.bar_label(plot.containers[0])
    plot.tick_params("y", which="both", left=False, labelleft=False)
    plot.set_xlabel("Mana value")
    plot.set_title("")

    plt.show()


def plot_most_reprinted_cards() -> None:
    """
    Plot the most reprinted cards excluding the lands
    """

    df = pd.read_csv("./cards.csv", usecols=["name", "types"])
    df = df.loc[(df["types"] != "Land")]  # exclude the lands
    df = df["name"].value_counts()[:10]  # select the top ten

    plot = df.plot(kind="bar", rot=0)
    plot.bar_label(plot.containers[0])
    plot.tick_params("y", which="both", left=False, labelleft=False)
    plot.set_title("Most reprinted cards (excluding lands)")
    plot.set_xlabel("")
    plt.show()


def print_choice():
    print("What do you want to see:")
    print("1 : Artist participation")
    print("2 : Mana cost")
    print("3 : Ten most reprinted cards")
    print("4 : Percentage of cards reprinted")
    print("5 : Quit")


def main():
    while True:
        print_choice()
        input_ = input().strip()

        match input_:
            case "1":
                return plot_artist()

            case "2":
                return plot_mana_cost()

            case "3":
                return plot_most_reprinted_cards()

            case "4":
                return plot_reprint()

            case "5":
                sys.exit()

            case _:
                print("Invalid input\n")
                continue


if __name__ == "__main__":
    main()
