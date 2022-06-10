from flask import Flask, send_file, make_response
import json
import os


app = Flask(__name__)

files_location = "./Files"


@app.route("/api/v1/<device>/AllVersions")
def getFWVersionsByDevice(device):
    if validateDevice(device):
        directory = f"{files_location}/{device}"
        FW_version_list = [file[:-4] for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
        return json.dumps(FW_version_list)
    else:
        return f"Device \"{device}\" not found"


@app.route("/api/v1/AllDevices")
def getAllDevices():
    devices = getDevices()
    print(devices)
    return json.dumps(devices)


@app.route("/api/v1/<device>/<version>/download")
def downloadFW(device, version):
    file = f"{files_location}/{device}/{version}.txt"
    response = make_response(send_file(file))
    response.headers["filename"] = f"{version}.txt"
    response.headers["device"] = f"{device}"
    return response
    
    
def getDevices():
    devices = [name for name in os.listdir(files_location) if os.path.isdir(os.path.join(files_location, name))]
    return devices


def validateDevice(device):
    devices = getDevices()
    return device in devices


def validateVersion(device, version):
    if validateDevice(device):
        pass
    else:
        return False


app.run(debug=True)