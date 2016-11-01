from bottle import run, request, post
import os

@post('/')
def index():
    postdata = request.body.readlines()
    with open("postreq.json", "w") as f:
        for line in postdata:
            f.write(line)
    os.system("python profile.py")
    return "Thank you. Your data processed and will ready to view soon."

if __name__ == "__main__":
    run(host='0.0.0.0', port=8080)
