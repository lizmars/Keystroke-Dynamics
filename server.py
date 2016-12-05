from bottle import run, request, post
import os
import json
import subprocess

@post('/')
def index():
    #postdata = request.body.readlines()
    #with open("postreq.json", "w") as f:
    #    for line in postdata:
    #        f.write(line)
    postdata = request.json
    if postdata == 400:
        print "Error invaid JSON"
    else:
        user = request.get_header("User")
        typepost = request.get_header("Type")
        postfile = typepost + "_" + user + "POST.json"
        if " " in user:
            user.replace(" ", "_")
        with open(postfile, "w") as f:
            f.write(json.dumps(postdata))

        if typepost == "Create_Profile":
            #subprocess.call([python, "profile.py" + postfile])
            os.system("python profile.py " + postfile)

        elif typepost == "Auth":
            print typepost
            os.system("python auth.py " + postfile)
        return "Thank you. Your data processed and will ready to view soon."

if __name__ == "__main__":
    run(host='0.0.0.0', port=8080)
