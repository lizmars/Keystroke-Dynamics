from bottle import run, request, post

@post('/')
def index():
    postdata = request.body.readlines()
    for line in postdata:
        print line
    return "OK"

if __name__ == "__main__":
    run(host='0.0.0.0', port=8080)
