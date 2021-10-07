
# Introduction - MLFlow SDK Starter Kit

*A startkit to get up and running with MLFlow inside a Development Container using Visual Studio Code.*

MLflow is a platform to streamline machine learning development, including tracking experiments, packaging code into reproducible runs, and sharing and deploying models. MLflow offers a set of lightweight APIs that can be used with any existing machine learning application or library (TensorFlow, PyTorch, XGBoost, etc), wherever you currently run ML code (e.g. in notebooks, standalone applications or the cloud). MLflow's current components are:

MLflow Tracking: An API to log parameters, code, and results in machine learning experiments and compare them using an interactive UI.
MLflow Projects: A code packaging format for reproducible runs using Conda and Docker, so you can share your ML code with others.
MLflow Models: A model packaging format and tools that let you easily deploy the same model (from any ML library) to batch and real-time scoring on platforms such as Docker, Apache Spark, Azure ML and AWS SageMaker.
MLflow Model Registry: A centralized model store, set of APIs, and UI, to collaboratively manage the full lifecycle of MLflow Models.

Github: https://github.com/mlflow/mlflow

Here, we focus on designing  [*Machine Learning Operations*](https://azure.microsoft.com/en-us/services/machine-learning/mlops/#features) with the goal to create a reproducible work environment for Data Science teams.

### Context
Why a starterkit?

-   Convention over configuration: Decrease the number of decisions a datascientist/engineer has to make and eliminate the complexity of having to configure all and each of the areas of model development.
-   Tightly coupled example code: Most MLOps frameworks and tooling disclose examples that are entangled into the framework itself. This repository is focused on delivering a decoupled solution where core functionality will be abstracted from the framework code.
-   Undocumented Design decisions: Even though some frameworks/platforms provide the ability to connect with your platform of choice, I as well as others have experienced that often certain design decision are left undocumented, that make it difficult to review how various subsystems work together (Misconfiguration can have serious repercussions).

### [](https://github.com/daved-net/Starterkit.MLFlow/blob/main/README.md#design-decisions)Design decisions

Within this repository you will find that the underlying design decisions have been taken into account:

-   Multi stage environment (L-DTSP) supporting CI/CD
    -   Local Environment = Your workstation, either your laptop, remote VM or anything similar
    -   Development Environment = For all development work (modifying internal libraries, functions and steps) and any other experimental work with minimal access to sensitive/restricted data
    -   Test Environment = Any preparatory test work. Testing the automated data pipelines, software performance (test cpu/gpu allocation). This stage should have a set of data that is a representation of the actual data (so all sensitive information should be masked or mocked)
    -   Staging = Gatekeeper before moving to production. This stage should have a subset of the data in your online systems (including sensitive information).
    -   Production = The live environment where your model (API) will be consumed by other systems. This environment is integrated into the feedback loop.
-   Model API is seperated from business logic (Following the Single Responsibility principle)
-   OOP-principles

## Resources

 -  [9 Tips for productionalizing Machine Learning](https://medium.com/microsoftazure/9-advanced-tips-for-production-machine-learning-6bbdebf49a6f) by @pythiccoder 
 - [MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)

 - [Converting to ONNX](https://github.com/onnx/tutorials#converting-to-onnx-format)

# 1. Prerequisites

**Frameworks & Libraries**

2. [Docker version >= 19.03.1](https://docs.docker.com/docker-for-windows/install/)
3. [Python version >= 3.7](https://www.python.org/downloads/)  

**Visual Studio Code (Plugins)**

4. [Visual Studio Code >= Version 1.3](https://code.visualstudio.com/docs)
5. [Remote - Container (Dev Container)](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
6. [VsCode extension: Python](https://marketplace.visualstudio.com/itemsitemName=ms-python.python) 
itemName=jithurjacob.nbpreviewer)

## Quickstart 

1. Open the project directory in vscode 
2. `cmd + shift + p` and search for `Remote-Containers: Open Folder in Container` and hit enter
3. Wait for the commands to execute and the container to build. (This might take a while when running dev containers for the first time, due to Image downloads etc.)
4. Start the main script by navigating to the debug tab (you can easily configure your own project launch scripts in .vscode/launch.json) [How to setup 'Launch Configurations'](https://code.visualstudio.com/docs/editor/debugging#_launch-configurations)

## Troubleshooting

*  Is docker running Linux Containers? This project runs Linux based containers, therefore, it does not run on Windows directly or in Windows containers.
*  Remember port forwaring is used. If you have existing applications running on the same port, you might not be able to access your resource
* https://code.visualstudio.com/docs/remote/create-dev-container
* https://docs.docker.com/config/containers/container-networking/
    
