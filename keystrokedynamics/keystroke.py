from flask import render_template
from flask import request, Response
from keystrokedynamics import app, nav, cross_origin

import json

import checkname
import profile
import bioauth

nav.Bar('top', [
    nav.Item('Home', 'index'),
    nav.Item('Create Profile', 'createprofile'),
    nav.Item('Authentication', 'auth'),
    nav.Item('Contact Us', 'contacts'),
    nav.Item('About Us', 'about'),
])

@app.route('/')
@cross_origin()
def index():
    return render_template('keystrpage.html')

@app.route('/createprofile', methods=['GET', 'POST'])
@cross_origin()
def createprofile():
    if request.method == 'POST':
        postdata = request.json
        user = request.headers["User"]
        typepost = request.headers["Type"]

        if " " in user:
            user.replace(" ", "_")

        if typepost == "is_in_DB":
            print "Checkname Status for", user, ": ",
            if checkname.is_record_exists(user):
                print "Alredy Exist"
                return Response("User Name Already Exist", mimetype="text/plain")
            else:
                print "New Name"
                return Response("OK", mimetype="text/plain")
        elif typepost == "Create_Profile":
            postfile = typepost + "_" + user + "POST.json"
            with open(postfile, "w") as f:
                f.write(json.dumps(postdata))

            if profile.new_profile(postfile):
                print "Profile Created"
                return Response("True", mimetype="text/plain")
            else:
                print "Fail. Something gone wrong"
                return Response("False", mimetype="text/plain")

    return render_template('createprofile.html')

@app.route('/auth', methods=['GET', 'POST'])
@cross_origin()
def auth():
    if request.method == 'POST':
        postdata = request.json
        user = request.headers["User"]
        typepost = request.headers["Type"]

        if " " in user:
            user.replace(" ", "_")
        if typepost == "is_in_DB":
            print "Checkname Status for", user, ": ",
            if checkname.is_record_exists(user):
                print "Alredy Exist"
                return Response("User Name Already Exist", mimetype="text/plain")
            else:
                print "New Name"
                return Response("OK", mimetype="text/plain")
        elif typepost == "Auth":
            postfile = typepost + "_" + user + "POST.json"
            with open(postfile, "w") as f:
                f.write(json.dumps(postdata))
            print "Auth begin for ", user
            return Response(bioauth.start_auth(postfile), mimetype="text/plain")
    return render_template('auth.html')

@app.route('/contacts')
@cross_origin()
def contacts():
    return render_template('contacts.html')

@app.route('/aboutus')
@cross_origin()
def about():
    return render_template('aboutus.html')


@app.route('/theend')
@cross_origin()
def theend():
    return render_template('theend.html')
