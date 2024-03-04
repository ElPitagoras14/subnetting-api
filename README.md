# Subnetting API

## Description

Code written in python where the algorithm for IP segmentation with FLSM and VLSM techniques is used.

## Requirements

- Python 3.7+
- pip

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ElPitagoras14/subnetting-api.git
   cd subnetting-api
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Run the following command:

   ```bash
   pip install -r requirements/dev.txt
   ```

4. Create an .env file in the root of the project and add the following environment variables:

   ```env
   HOST=127.0.0.1
   PORT=8000
   DEBUG=True
   APP_NAME=main:app
   ```

## Running the Server

1. Make sure your virtual environment is activated (if you created one).

2. Navigate to the src folder and run the script:

   ```bash
   python main.py
   ```

3. If you use VSCode, you can use task to run the project.

The server should be running at `http://127.0.0.1:8000`.

## Usage

You can access the automatically generated FastAPI documentation at `http://127.0.0.1:8000/docs`.

## Author

- [Jonathan García](https://github.com/ElPitagoras14) - Computer Science Engineer
