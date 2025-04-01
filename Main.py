from DataStructures.Listings import Listing as Lst


def main():
    import matplotlib.pyplot as plt

    # Sample data
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 25, 30, 40]

    # Create the plot
    plt.plot(x, y, marker='o', linestyle='-', color='b', label="Line Graph")

    # Add labels and title
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Simple Line Plot with Matplotlib")

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()


main()