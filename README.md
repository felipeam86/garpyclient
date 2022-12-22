# Garpyclient: Basic library for authenticating and querying Garmin Connect


[![PyPI-Status](https://img.shields.io/pypi/v/garpyclient.svg)](https://pypi.org/project/garpyclient)
[![Tests](https://github.com/felipeam86/garpyclient/actions/workflows/test.yml/badge.svg)](https://github.com/felipeam86/garpyclient/actions/workflows/test.yml) 
[![Coveralls](https://coveralls.io/repos/github/felipeam86/garpyclient/badge.svg?branch=develop)](https://coveralls.io/github/felipeam86/garpyclient?branch=develop)



`garpyclient` is a simple library to communicate with Garmin Connect. It was extracted from
[garpy](https://github.com/felipeam86/garpy) and the idea is for this to become the core client
library of it in a next iteration. Ideally, `garpyclient` is intended to be used by other python libraries that want to download their data from Garmin Connect. It is kept simple on purpose so that
end users can build upon it with their own workflows. As an example, the following code will fetch the 
latest activity from your Garmin profile:


```python
from garpyclient import GarminClient

with GarminClient(username="user", password="pass") as client:
    activities = client.list_activities()
    response = client.get_activity(activities[0]["activityId"], fmt="original")
```

The file content will be found in `response.content`. The format of the file will depend on the parameter `fmt` to which you can pass the following values:

- For an overview of the activities: `summary` or `details`
- For data points of the activity: `gpx`, `tcx`, `original` (usually fit format) and `mkl`.


## Installation

``garpyclient`` requires Python 3.7 or higher on your system. 
Install with pip as follows:


```bash
    pip install -U garpyclient
```

If you are new to Python, I recommend you install [Miniconda](https://docs.conda.io/en/latest/miniconda.html). To my knowledge, it is the simplest way of installing a robust and
lightweight Python environment.


## Acknowledgements

The original library ([garpy](https://github.com/felipeam86/garpy)) is based on
[garminexport](https://github.com/petergardfjall/garminexport). I borrowed the GarminClient, refactored it to my taste and created a package from it.

