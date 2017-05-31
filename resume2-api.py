from bottle import run, route
from bottle import static_file
@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='')
run(host='10.0.0.4', port=8080, debug=True)
