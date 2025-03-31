import numpy
import matplotlib.pyplot as plt  # Importing pyplot for creating plots

class ByteBungalowViz:
    def __init__(self, data):
        self.data = data

    def plot_median(self):
                                            # plot median data, label 
        median = self.data["median"]
        plt.plot(median)
        plt.title("Median Rental Prices")
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.show()

    def plot_mean(self):
                                            # Plotting mean data and labeling 
        mean = self.data["mean"]
        plt.plot(mean)
        plt.title("Mean Rental Prices")
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.show()

    def plot_upper_bound(self):
                                                #  upper bound data and setting labels
        upper_bound = self.data["upper_bound"]
        plt.plot(upper_bound)
        plt.title("Upper Bound Rental Prices")
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.show()

    def plot_lower_bound(self):
                                                    # lower bound data with labels
        lower_bound = self.data["lower_bound"]
        plt.plot(lower_bound)
        plt.title("Lower Bound Rental Prices")
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.show()

    def plot_mode(self):
                                                            # mode data and label the plot
        mode = self.data["mode"]
        plt.plot(mode)
        plt.title("Mode Rental Prices")
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.show()

    def run(self):
                                    # run functions to display  data
        self.plot_median()
        self.plot_mean()
        self.plot_upper_bound()
        self.plot_lower_bound()
        self.plot_mode()

if __name__ == "__main__":
                                                                    # Sample data 
    data = {
        "median": [1000, 1200, 1500, 1800, 2000],
        "mean": [1100, 1300, 1600, 1900, 2100],
        "upper_bound": [1500, 1800, 2000, 2200, 2500],
        "lower_bound": [500, 600, 700, 800, 900],
        "mode": [1000, 1200, 1500, 1800, 2000]
    }
    viz = ByteBungalowViz(data)
    viz.run()
