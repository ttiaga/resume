#!/usr/bin/python
from bottle import route, request, response, run
from bottle import static_file
import os
from flask import Flask
from flask import request
from flask import Flask, render_template, request, url_for
from flask import Flask, redirect

#df = xlrd.open_workbook('Book2.xls')

#@route('/search/<name>', method='GET')
#def search(name='No Name'):
#    outJson= []

#    for index,result in df.iterrows():
#	outJson.append(result.to_json())
#    return json.dumps(outJson)
#file = open ("ted.json", "r")
#resume = file.read()


#returning something


@route('/ted/')
def ted_list(filename):
	return static_file(filename, root='ted.json')
run(host='10.0.0.4', port=8080, debug=True)
