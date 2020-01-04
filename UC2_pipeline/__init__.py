import json
import os
import subprocess
#from fabric import Connection
import requests
import uuid

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


def run_pipeline(observation, **kargs):
    print(kargs)
    # Request for staging data from LOFAR LTA
    stageid = str(uuid.uuid4())
#    webhook = "http://localhost:8000/stage/" + stageid
    webhook = "http://localhost:8000/sessions"
#    webhook = "http://eaa0f304.ngrok.io"
    srmuris = ["srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/lofar/ops/projects/lofarschool/246403/L246403_SAP000_SB000_uv.MS_7d4aa18f.tar"]
#    tarfiles = observation.split("|")
#    srmuris = tarfiles # [ tarfiles[0] ] # testing
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
        "webhook": {"method": "post", "url": webhook, "headers": {}},
        "options": {},
    }

#    print(kargs)
    for kw in kargs:
        if kw == "staging":
            url = kargs[kw]["url"] + url
            data["cmd"]["credentials"]["lofarUsername"] = kargs[kw]["login"]
            data["cmd"]["credentials"]["lofarPassword"] = kargs[kw]["pwd"]
    reqData = json.dumps(data)
    print("===REQ URL=", url)
    print("===REQ DATA=", reqData)
    res = requests.post(url, headers=headers, data=reqData)
    print(res)
    res_data = json.loads(res.content.decode("utf8"))
    #    res_val = "xenon-flow job id: " + res_data["id"]
    print("Your staging request ID is ", str(res_data["requestId"]))
    return res


#def run_pipeline(observation, **kargs):
#    # Start your pipeline here
#    url = '/jobs'
#    headers = {
#        'Content-Type': 'application/json',
#    }
#    data = {
#        "input": {}
#    }
#    #    print(kargs)
#    for kw in kargs:
#        if kw == "xenon_server_url":
#            url = kargs[kw] + url
#        elif kw == "api_key":
#            headers["api-key"] = kargs[kw]
#        elif kw == "workflow_name":
#            data["name"] = kargs[kw]
#        elif kw == "workflow_cwl":
#            data["workflow"] = kargs[kw]
#    res = requests.post(url, headers=headers, data=json.dumps(data))
#    # Parse HttpResponse and return xenon-flow job id for later use
#    # check content of res.data and retrieve res.data['id']???
#    #    print(res.content)
#    res_data = json.loads(res.content.decode("utf8"))
#    #    print("===xenon job id: ", res_data["id"])
#    res_val = "xenon-flow job id: " + res_data["id"]
#    return res
##    return "Testing ..."
