import json

def get_post_data():
    with open("postreq.json", 'r') as f:
        postdata = f.read()
    rawinput = json.loads(postdata)
    username = "".join(rawinput.keys())
    rdata = []
    for item in rawinput[username]:
        values = item.values()
        keylog = values[0].split(",")
        timelog = values[1].split(",")
        for i in xrange(len(keylog)):
            rdata.append([keylog[i],timelog[i]])
    return username, rdata

def get_postAuth_data():
    with open("postreq.json", 'r') as f:
        postdata = f.read()
    rawinput = json.loads(postdata)
    username = "".join(rawinput.keys())
    rdata = []
    for item in rawinput[username]:
        values = item.values()
        keylog = values[0].split(",")
        timelog = values[1].split(",")
        for i in xrange(len(keylog)):
            rdata.append([keylog[i],timelog[i]])
    return username, rdata
