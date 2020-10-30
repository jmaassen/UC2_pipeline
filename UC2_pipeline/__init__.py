import json
import os
import subprocess
import requests
import re

def give_name():
    jsonfile = give_config()
    name = list(jsonfile.keys())[0]
    return name

def give_version():
    return "0.1"

def give_config():
    json_config_file = os.path.join(os.path.dirname(__file__), "data", "config.json")
    with open(json_config_file) as json_data:
        return json.load(json_data)

def give_argument_names(required=False):
    jsonfile = give_config()
    name = list(jsonfile.keys())[0]
    required = jsonfile[name]["schema"]["required"]
    properties = set(jsonfile[name]["schema"]["properties"].keys())
    if required:
        return required
    else:
        return properties


def run_pipeline(observation, observation2, **kargs):
    print(kargs)
    # Request for staging data from LOFAR LTA
    tarfiles = observation.split("|")
    srmuris = [] #tarfiles[:20] # testing
    for tfile in tarfiles:
        if re.search('SB0[0|1]', tfile):
            srmuris.append(tfile)

    url = '/stage'
    headers = {
        'Content-Type': 'application/json',
    }
    
    data = {
        "id": "staging",
        "cmd": {
            "type": "stage",
            "subtype": "lofar",
            "src": {
                "type": "srm",
                "paths": srmuris
            },
            "credentials": {}
        },
        "options": {},
    }
    
    #    print(kargs)
    for kw in kargs:
        if kw == "staging":
            url = kargs[kw]["url"] + url
            data["cmd"]["credentials"]["lofarUsername"] = kargs[kw]["login"]
            data["cmd"]["credentials"]["lofarPassword"] = kargs[kw]["pwd"]
    reqData = json.dumps(data)
    res = requests.post(url, headers=headers, data=reqData)
    res_data = json.loads(res.content.decode("utf8"))
    print("Your staging request ID is ", str(res_data["requestId"]))
    return res


