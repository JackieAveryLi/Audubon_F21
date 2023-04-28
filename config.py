import torch

# Flags for training detector
BIRD_ONLY = True
SUBSET = True

# Constants
DEVICE = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
SEED = 2023

# Configurations
CONFIG = {
    'model': ('bird_only', 2) if BIRD_ONLY else ('species', 23),  # NOTE: 23 is read from database/class_id.csv,
    'data_split': (0.04, 0.005, 0.005) if SUBSET else (0.8, 0.1, 0.1),
    "batch_size": 1 if SUBSET else 8
}

# Hyperparameters
HYPERPARAMS = {
    'num_epoch': 5,
    "l_r": 0.002,
}

# Paths
PLOTS_PATH = "./plots/"
DATA_PATH = "./database/"
IMG_PATH = DATA_PATH + 'detection/raw_data/images/'
OLD_CSV_PATH = DATA_PATH + 'detection/raw_data/csv_files_old/'
NEW_CSV_PATH = DATA_PATH + 'detection/raw_data/csv_files_new/'
TILED_IMG_PATH = DATA_PATH + 'detection/tiled_data/images/'
TILED_OLD_CSV_PATH = DATA_PATH + 'detection/tiled_data/csv_files_old/'
TILED_NEW_CSV_PATH = DATA_PATH + 'detection/tiled_data/csv_files_new/'
CROPPED_PATH = DATA_PATH + 'cropped/'
DETECTOR_PATH = DATA_PATH + 'models/' + CONFIG['model'][0] + '/'

# Annotations mapping relations
DESC_MAPPING = {
    'Great Egret Flying': 'Great Egret Adult',
    'Reddish Egret Flying': 'Reddish Egret Adult',
    'White Ibis Juvenile': 'White Ibis Adult',
    'Black Skimmer flying': 'Black Skimmer Adult',
    'Great Blue Heron Flying': 'Great Blue Heron Adult',
    'Laughing Gull Flying': 'Laughing Gull Adult',
    'Brown Pelican In Flight': 'Brown Pelican Adult',
    'Brown Pelican - Wings Spread': 'Brown Pelican Adult',
    'Mixed Tern Flying': 'Mixed Tern Adult',
    'Reddish Egret Chick': 'Reddish Egret Adult',
    'Laughing Gull Juvenile': 'Laughing Gull Adult',
    'Brown Pelican Wings Spread': 'Brown Pelican Adult',
    'Black Crowned Night Heron Adult': 'Black-Crowned Night Heron Adult',
    'Tri-Colored Heron Adult': 'Tricolored Heron Adult',
    'Cattle Egret Flying': 'Cattle Egret Adult',
    'Trash/Debris': 'Debris',
    'Great Egret/White Morph Adult': 'Great Egret or White Morph Adult'
}
ON_DELETE = [
    'Great Blue Heron Egg',
    'White Ibis Nest',
    'Double-Crested Cormorant Adult',
    'Great Blue Heron Nest',
    'American Avocet Adult',
    'Trash',
    'American Oystercatcher'
]
