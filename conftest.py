"""Make the ``validkit`` package importable during the test run."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
