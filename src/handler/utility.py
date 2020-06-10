# ---------------------------------------------------------------------------------------------------------------------- #
# Project   :-> Self Organising Maps
# Authors   :-> Sudharsan
# E-mail    :-> sudharsansci@gmail.com

# ---------------------------------------------------------------------------------------------------------------------- #
# Import packages
# ---------------------------------------------------------------------------------------------------------------------- #
import cv2
import glob
import matplotlib.pyplot as plt
from src.som.som_1d import *


# -----> Frames to Video <----- #
def frames_to_video(directory: str, file_name: str):
    """
    A function to create a video of the
    Args:
        directory: string
            Directory of the folder that contains individual frames
        file_name: string
            Desired name for the output video file
    Returns: None

    """
    img_array = []
    for filename in glob.glob(directory + '/*.png'):
        img = cv2.imread(filename)
        img_array.append(img)
    out = cv2.VideoWriter(file_name + '.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, img_array[0].shape)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()


def implement_som1d(data: np.array) -> SOM_1D:
    """
    A function to Implement SOM 1D
    Args:
        data: np.array
            Input Data

    Returns: Object
        SOM_1D Object

    """
    som_obj = SOM_1D()
    som_obj.initializer(data)
    som_obj.fit()
    return som_obj


def save_data(data: list or np.array, path: str, file_name: str = 'data', file_format: str = 'csv') -> None:
    """
    Save the weights to the disk
    Args:
        file_format: str
            file format type
        path: str
            path to root dir
        file_name: str
            File name for the file to store weights
        data: np.array
            data of the SOM Model

    Returns: None

    """
    data = pd.DataFrame(data)
    if file_format == 'csv':
        data.to_csv(path + '/models/weights/' + file_name)
    else:
        print('file format is not supported, try something else')


def load_data(path: str, file_name: str, file_format: str = 'csv') -> np.array:
    """

    Args:
        file_format: str
            File format type
        path: str
            Path to the file
        file_name:
            name of the file

    Returns: np.array
        Returns the loaded data
    """
    if file_format == 'csv':
        return pd.read_csv(path + file_name).to_numpy()[:, 1:]
    else:
        print('file format is not supported, try something else')


def visualize_data(obj: SOM_1D, title: str) -> None:
    fig = plt.figure(figsize=(10, 10))
    data, = plt.plot(obj.data[:, 0], obj.data[:, 1], 'ro')
    weights, = plt.plot(obj.weights[:, 0], obj.weights[:, 1], 'b.')
    if obj.loop_path:
        path, = plt.plot(obj.weights[:, 0], obj.weights[:, 1], 'y--')
        plt.plot([obj.weights[0, 0], obj.weights[-1, 0]], [obj.weights[0, 1], obj.weights[-1, 1]], 'y--')
    else:
        path, = plt.plot(obj.weights[:, 0], obj.weights[:, 1], 'y--')
    plt.legend([data, weights, path], ['Data', 'Weights', 'Path'])
    plt.title('Solution to Travelling Salesman Problem')
    plt.savefig('../results/output/solution.png')
    plt.show()