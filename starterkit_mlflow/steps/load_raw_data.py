"""
Downloads the MovieLens dataset and saves it as an artifact
"""
from logging import raiseExceptions
import requests
import tempfile
import os
import zipfile
import pyspark
import mlflow
import click


@click.command(help="Download the boston_housing dataset")
@click.option("--filename", default="boston_housing")
@click.option("--file_ext", default=".csv")
@click.option("--data_directory", default="sample_data")
@click.option("--url", default="https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv")
def load_raw_data(filename:str, file_ext: str, data_directory: str, url: str):
   
    with mlflow.start_run() as mlrun:
        local_dir = tempfile.mkdtemp()
        local_filename = filename + file_ext
        local_filepath = os.path.join(local_dir, local_filename)

        __download_file(url, local_filepath)

        downloaded_file_is_saved = os.path.exists(local_filepath)
        if(not downloaded_file_is_saved):
            raise Exception(f'your downloaded {local_filepath} file was not saved')

        print("Uploading ratings: %s" % local_filepath)
        mlflow.log_artifact(local_filepath, data_directory)

def __download_file(url: str, filename: str):
    print("Downloading %s to %s" % (url, filename))

    r = requests.get(url, stream=True)
    with open(filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)

if __name__ == "__main__":
    load_raw_data()