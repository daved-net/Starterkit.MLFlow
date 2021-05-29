import os
import pandas
from src.startup import Startup

Startup()
project_dir = os.environ['PROJECT_DIR']
dataset_rel_filepath = os.environ['DATASET_FILEPATH']
dataset_abs_filepath = os.path.join(project_dir,dataset_rel_filepath)
df = pandas.read_csv(dataset_abs_filepath)
print(df.head())
