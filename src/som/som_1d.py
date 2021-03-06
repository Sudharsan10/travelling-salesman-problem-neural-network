# ---------------------------------------------------------------------------------------------------------------------- #
# Project   :-> Self Organising Maps
# Authors   :-> Sudharsan
# E-mail    :-> sudharsansci@gmail.com

# ---------------------------------------------------------------------------------------------------------------------- #
# Import packages
# ---------------------------------------------------------------------------------------------------------------------- #
import numpy as np
import pandas as pd
from src.som.som import SOM


class SOM_1D(SOM):
    """
    SOM_1D is a Child class inheriting SOM parent class for performing 1D Self Organizing Maps algorithm implementation

    Functions:
        -> initializer()                : A function to initialise all the required parameters to perform 1D SOM fitting
        -> compute_neighbourhood_prob() : A function to compute the gaussian probability for neighbourhood in 1D
        -> fit()                        : A function to perform 1D SOM fitting to the given data
    """

    def __init__(self):
        super().__init__()
        self.len = None
        self.BMU = None
        self.dist = None
        self.data = None
        self.weights = None
        self.data_dim = None
        self.data_set = None
        self.save_file = False
        self.save_count = 1
        self.neighborhood_prob = None

        # -----> Variables initialize <----- #
        self.N = 50
        self.sample_count = 0.5
        self.lattice = np.arange(self.N)

        # -----> Flags <----- #
        self.loop_path = True
        self.random_sample = False
        self.save_file = False
        self.frames = {}
        self.weights_df = None

        # -----> Hyper parameter Constants <----- #
        self.lr_const = 0.04
        self.epochs_const = 1000
        self.neighbors_radius_const = 0

    def initializer(self, data: np.array) -> None:
        """
        Initialise the data and data associated variables
        Args:
            data: np.array
                Data set

        Returns: None

        """
        self.len = data.__len__()
        self.N = 50 if 50 > self.len*5 else self.len*5
        self.neighbors_radius_const = self.neighbors_radius_const if self.neighbors_radius_const > 2*self.len else 2*self.len
        self.data_dim = data.shape
        self.data_set = data.copy()

        self.lattice = np.arange(self.N)
        self.weights = np.min(data, axis=0) \
                       + (np.max(data, axis=0) - np.min(data, axis=0)) \
                       * np.random.ranf((self.N, 2))

        # -----> Hyper parameter Constants <----- #
        self.time_const = self.epochs_const / np.log(self.neighbors_radius_const)
        if self.random_sample:
            idx = np.random.choice(np.arange(self.len), int(self.sample_count * self.len))
            self.data = data[idx]
        else:
            self.data = data.copy()

    def compute_neighborhood_prob(self, index: int, epoch: int) -> np.array:
        """

        Args:
            index: int
                BMU value
            epoch: int
                Current epoch

        Returns: np.array
            Returns an array of neighborhood probability
        """
        sigma = self.compute_neighborhood_size(epoch)
        lateral_dist = abs(self.lattice - index)
        if self.loop_path:
            lateral_dist = np.minimum(lateral_dist, self.N - lateral_dist)
        return np.exp(-lateral_dist ** 2 / (2 * sigma ** 2)).reshape(-1, 1)

    def fit(self) -> None:
        """
        It implements the 1D SOM

        Returns: None

        """
        for epoch in range(1, self.epochs_const + 1):
            np.random.shuffle(self.data)
            if epoch < 5 or epoch % self.save_count == 0:
                self.frames[epoch] = self.weights.copy()
            for data_point in self.data:
                self.dist = self.find_euclidean_distance(data_point, self.weights)
                self.BMU = self.find_BMU(self.dist)
                self.neighborhood_prob = self.compute_neighborhood_prob(self.BMU, epoch)
                self.lr = self.compute_learning_rate(epoch)
                self.update_weights(data_point)

        if self.save_file:
            self.weights_df = pd.DataFrame(self.frames)
