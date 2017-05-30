import json
from bottle import route, run
import pandas as pd

df = pd.read_csv('gotit.csv',sep=',')
#df = xlrd.open_workbook('Book2.xls')

@route('/search/<name>', method='GET')
def search(name='No Name'):
    outJson= []
    for index,result in df[df.Name == name].iterrows():
	outJson.append(result.to_json())
    return json.dumps(outJson)

run(host='10.0.0.4', port=8080, debug=True)
