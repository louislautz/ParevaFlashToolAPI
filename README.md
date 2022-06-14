# ParevaFlashToolAPI

This repo is a Test-API for the Pareva Flashtool.
It runs on the Flask Webframework and has three endpoints:
- GET "/api/v1/```device```/AllVersions", which returns all available FW-Versions of a specific device
- GET "/api/v1/AllDevices", which returns a list of all available devices
- GET "/api/v1/```device```/```version```/download", which downloads a specific FW-Version of a specific device
  
It runs on localhost as its just a test API.

## How to use this project
  
1. clone this repo: ```git clone https://github.com/louislautz/ParevaFlashTool.git```

2. open the virtual environment: ```pipenv shell```

    2.1. if you dont have pipenv installed yet, install it with: ```pip install pipenv```

3. Install all dependencies: ```pipenv install```

4. Export flask-related environment variables
    
    ```export FLASK_APP=API```
  
    ```export FLASK_ENV=development```
  
5. Run the API: ```flask run```
