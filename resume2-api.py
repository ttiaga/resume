#!/usr/bin/python
from bottle import run, route
from bottle import static_file
@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='/home/ttiaga/api/Resume')
run(host='10.0.0.4', port=8080, debug=True)
