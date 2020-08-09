import json
import os
from pathlib import Path


def open_datafile(datafile):
    """
    Opens a test datafile by its name.
    :param datafile: (string) Name of the datafile.
    :return: Datafile content.
    :rtype: dict
    """
    datafile = Path(os.path.dirname(__file__)).parent / F"data/{datafile}"
    return json.loads(datafile.read_text())