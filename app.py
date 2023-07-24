from flask import Flask, request, redirect, url_for, jsonify, session, make_response
import json
from sqlhelper import MySqlHelper
import pandas as pd

app = Flask(__name__)

head = ['ID', 'TowerNo', 'TowerTypeName', 'BaseHeight', 'FrontSpan', 'LineAngle', 'LonLB', 'LatLB', 'Altitude',
        'LeftGroundAngle', 'RightGroundAngle', 'LightningDensity', 'GroundObjHeight', 'Terrain', 'GroundResis',
        'XCStringGroupName', 'FrontCondLineK', 'FrontEarthLineK', 'CNVLineTypeGroupName']


@app.route('/data', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        name = request.json['name']
        pwd = request.json['pwd']
        table_name = request.json['table_name']

        if name == 'cvml' and pwd == 'cvml123456':
            with MySqlHelper() as cursor:
                cursor.execute(f'select * from {table_name}')
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=head)
                # 丢弃第一列
                data = df.to_dict(orient='records')
                data = json.dumps(data, ensure_ascii=False)
            return data
    else:
        return jsonify({'status': 'fail'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)
