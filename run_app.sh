#!/bin/bash

# Get the conda Python prefix
PYTHON_PREFIX="$(python3 -c 'import sys; print(sys.prefix)')"

# Set up library paths to prioritize PyQt6 Qt libraries
export LD_LIBRARY_PATH="${PYTHON_PREFIX}/lib/python3.13/site-packages/PyQt6/Qt6/lib:${PYTHON_PREFIX}/lib:${LD_LIBRARY_PATH}"

# Use LD_PRELOAD to force load the correct Qt6Core library
export LD_PRELOAD="${PYTHON_PREFIX}/lib/python3.13/site-packages/PyQt6/Qt6/lib/libQt6Core.so.6"

# Run the app
python3 app_main.py
