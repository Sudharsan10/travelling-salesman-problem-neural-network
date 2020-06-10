# ---------------------------------------------------------------------------------------------------------------------- #
# Project   :-> Self Organising Maps
# Authors   :-> Sudharsan
# E-mail    :-> sudharsansci@gmail.com

# ---------------------------------------------------------------------------------------------------------------------- #
# Import packages
# ---------------------------------------------------------------------------------------------------------------------- #
import numpy as np


class SOM:
    """
    SOM is a parent class for Self Organizing Maps algorithm implementation with some basic functionalities

    Functions:
        -> find_euclidean_distance()    : A function to calculate the euclidean distance between two points
        -> find_BMU()                   : A function to compute the Best matching Unit(BMU)
        -> update_weights()             : A function to perform weights updating
        -> compute_learning_rate()      : A function to compute a decaying learning rate after every epoch
        -> compute_neighbourhood_size() : A function to compute a decaying neighbourhood radius after every epoch
    """

    def __init__(self):
        self.lr = None
        self.size = None
        self.weights = None
        self.lr_const = None
        self.time_const = None
        self.epochs_const = None
        self.neighborhood_prob = None
        self.neighbors_radius_const = None
        print("Created an SOM class object...!")

    @staticmethod
    def find_euclidean_distance(d1: np.array, d2: np.array) -> np.array:
        """
        A static method to find distance between two points or two array of data points

        Args:
            d1: np.array
                data1
            d2: np.array
                data2

        Returns: None

        """
        return np.sqrt(np.sum((d1 - d2) ** 2, axis=1, keepdims=True))

    @staticmethod
    def find_BMU(dist: np.array) -> np.array:
        """
        A static method to find the index of an array with minimum heuristics

        Args:
            dist: np.array
                An array of distance values

        Returns: int

        """
        return np.argmin(dist)

    def update_weights(self, data_point: np.array) -> None:
        """
        A method to update weights of the model

        Args:
            data_point: np.array
                data

        Returns: None

        """
        self.weights += self.lr * self.neighborhood_prob * (data_point - self.weights)

    def compute_learning_rate(self, current_epoch: int) -> float:
        """
        A method to compute learning rate based on the current epoch

        Args:
            current_epoch: int
                Value of the current epoch

        Returns: float

        """
        return self.lr_const * np.exp(-current_epoch / self.epochs_const)

    def compute_neighborhood_size(self, current_epoch: int) -> float:
        """
        A method to compute neighborhood size for updating weighting based on current epoch

        Args:
            current_epoch:

        Returns: float

        """
        return self.neighbors_radius_const * np.exp(-current_epoch / self.time_const)