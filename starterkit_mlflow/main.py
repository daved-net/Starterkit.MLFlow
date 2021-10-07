import click
import os

from setting import Setting
import mlflow
from utils.config import Config

import mlflow
from mlflow.utils import mlflow_tags
from mlflow.entities import RunStatus
from mlflow.utils.logging_utils import eprint

from mlflow.tracking.fluent import _get_experiment_id

def _get_or_run(entrypoint, parameters, git_commit, use_cache=True):
   print(f"Launching new run for entrypoint={entrypoint} and parameters={parameters}")
   submitted_run = mlflow.run("/workspace/starterkit_mlflow/", entrypoint, parameters=parameters)
   return mlflow.tracking.MlflowClient().get_run(submitted_run.run_id)


config = Config(os.path.join(os.path.abspath(__file__)))
config.from_object('setting.DevelopmentSetting')

experiment_name = config['EXPERIMENT_NAME']
mlflow.set_experiment(experiment_name)
experiment = mlflow.get_experiment_by_name(experiment_name)

print("Experiment_id: {}".format(experiment.experiment_id))
print("Artifact Location: {}".format(experiment.artifact_location))
print("Tags: {}".format(experiment.tags))
print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))




@click.command()
@click.option("--als-max-iter", default=10, type=int)
@click.option("--keras-hidden-units", default=20, type=int)
@click.option("--max-row-limit", default=100000, type=int)
def workflow(als_max_iter, keras_hidden_units, max_row_limit):
   # Note: The entrypoint names are defined in MLproject. The artifact directories
   # are documented by each step's .py file.
      with mlflow.start_run() as active_run:

         os.environ["SPARK_CONF_DIR"] = os.path.abspath(".")
         git_commit = active_run.data.tags.get(mlflow_tags.MLFLOW_GIT_COMMIT)
         load_raw_data_run = _get_or_run("load_raw_data", {}, git_commit)

         print("finished")
         # ratings_csv_uri = os.path.join(load_raw_data_run.info.artifact_uri, "ratings-csv-dir")
         # etl_data_run = _get_or_run(
         #     "etl_data", {"ratings_csv": ratings_csv_uri, "max_row_limit": max_row_limit}, git_commit
         # )
         # ratings_parquet_uri = os.path.join(etl_data_run.info.artifact_uri, "ratings-parquet-dir") 
         # # We specify a spark-defaults.conf to override the default driver memory. ALS requires
         # # significant memory. The driver memory property cannot be set by the application itself.
         # als_run = _get_or_run(
         #     "als", {"ratings_data": ratings_parquet_uri, "max_iter": str(als_max_iter)}, git_commit
         # )
         # als_model_uri = os.path.join(als_run.info.artifact_uri, "als-model") 
         # keras_params = {
         #     "ratings_data": ratings_parquet_uri,
         #     "als_model_uri": als_model_uri,
         #     "hidden_units": keras_hidden_units,
         # }
         # _get_or_run("train_keras", keras_params, git_commit, use_cache=False)


if __name__ == "__main__":
   workflow()