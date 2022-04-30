import googleapiclient.discovery
import os

def predict_json(project, model, instances, version=None):
    """Send json data to a deployed model for prediction.

    Args:
        project (str): project where the Cloud ML Engine Model is deployed.
        model (str): model name.
        instances ([Mapping[str: Any]]): Keys should be the names of Tensors
            your deployed model expects as inputs. Values should be datatypes
            convertible to Tensors, or (potentially nested) lists of datatypes
            convertible to tensors.
        version: str, version of the model to target.
    Returns:
        Mapping[str: any]: dictionary of prediction results defined by the
            model.
    """
    # Create the ML Engine service object.
    # To authenticate set the environment variable
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="utils/model-almanac-291915-5821b27fb095.json"
    service = googleapiclient.discovery.build('ml', 'v1')
    name = 'projects/{}/models/{}'.format(project, model)

    if version is not None:
        name += '/versions/{}'.format(version)

    response = service.projects().predict(
        name=name,
        body={'instances': instances}
    ).execute()

    if 'error' in response:
        raise RuntimeError(response['error'])

    return response['predictions']


# instances = [{'X1': 0.98, 'X2': 514.5, 'X3': 294.0, 'X4': 110.25, 'X5': 7.0, 'X6': 3.0,
#                     'X7': 0.0, 'X8': 0.0},
#             {'X1': 0.98, 'X2': 514.5, 'X3': 294.0, 'X4': 110.25, 'X5': 7.0, 'X6': 4.0,
#                     'X7': 0.0, 'X8': 0.0}]

# prediction = predict_json("model-almanac-291915", "HEATING_MODEL", instances, version="v1")
# print(prediction)