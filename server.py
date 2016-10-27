from bottle import run, request, post
import subprocess
import os

@post('/')
def index():
    postdata = request.body.readlines()
    with open("postreq.json", "w") as f:
        for line in postdata:
            #print line
            f.write(line)
    os.system("python profile.py")
    return "OK"

if __name__ == "__main__":
    run(host='0.0.0.0', port=8080)
