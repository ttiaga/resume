from bottle import route, run, static_file
from flask import send_file
import pandas as pd

df = pd.read_csv('gotit.csv',sep=',')
#df = xlrd.open_workbook('Book2.xls')

@route('/search', method='GET')
def ted():
	try:
		return ('ted.json')

	run(host='10.0.0.4', port=8080, debug=True)
