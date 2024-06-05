#############################################
# Illustration de la  distribution normale  #
#############################################

import random
import matplotlib.pyplot as plt


def die(weights: list[int] = []) -> int:
    """
    Simulates rolling a weighted die.

    Args:
        weights (list[int]): A list of positive integer weights for each choice.

    Returns:
        int: The result of the roll (one of the choices).
    """
    weights = [1, 1, 1, 1, 1, 1]
    # weights = [100, 50, 1, 1, 50, 100] # Uncomment to introduce weights

    return random.choices(range(1, len(weights) + 1), weights=weights)[0]


def sum_dice_roll(n: int) -> list:
    return sum([die() for _ in range(n)])


def approximate_median_sum(n: int) -> int:
    numbers = [1, 2, 3, 4, 5, 6]
    total = 0
    for i in range(n):
        total += numbers[i % len(numbers)]
    return total


def main() -> None:

    # Parameters
    rolls = 10_000  # Number of rolls
    dice = 10  # Number of dice per roll

    # Creat the lists
    sums = [sum_dice_roll(dice) for _ in range(rolls)]
    frequency = [sums.count(i) for i in range(dice, 6*dice+1)]

    # Get poles and median
    print(f"{dice}*1: {sums.count(dice)}")
    print(f"Median: {approximate_median_sum(dice)}")
    print(f"{dice}*6: {sums.count(6*dice)}")

    # Create a bar plot
    plt.bar(range(dice, 6*dice+1), frequency)

    # # Add a gird
    plt.grid(True)

    # # Add title
    plt.title(
        f"Fréquence des sommes\nNombre des lancers : {rolls} - Nombre des dès à chaque lancer : {dice}.")

    # # Label the axes
    plt.xlabel("Somme des dés lancés")
    plt.ylabel("Fréquence des sommes")

    # # Show the plot
    plt.show()
    print("beep \a")


if __name__ == "__main__":
    main()
