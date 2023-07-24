import pymysql
import json
from sqlhelper import MySqlHelper

# 打开数据库连接
conn = pymysql.connect(host='116.62.242.237', port=3306, user='cvml', passwd='cvml123456', db='data', charset='utf8')

cursor = conn.cursor()

sql = "create table if not exists TL_BWJ3 (ID int, TowerNo nvarchar(32), TowerTypeName nvarchar(32), " \
      "BaseHeight float, FrontSpan float, LineAngle float, LonLB float, LatLB float, Altitude float, " \
      "LeftGroundAngle float, RightGroundAngle float, LightningDensity float, GroundObjHeight float, " \
      "Terrain nvarchar(32), GroundResis float,XCStringGroupName nvarchar(32), FrontCondLineK nvarchar(32), " \
      "FrontEarthLineK nvarchar(32), CNVLineTypeGroupName nvarchar(32))"
cursor.execute(sql)
with open('./details/TL_BWJ3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for item in data:
        sql = f"insert into TL_BWJ3 values ({item['ID']},'{item['TowerNo']}','{item['TowerTypeName']}'," \
              f"{item['BaseHeight']},{item['FrontSpan']},{item['LineAngle']},{item['LonLB']},{item['LatLB']}," \
              f"{item['Altitude']},{item['LeftGroundAngle']},{item['RightGroundAngle']},{item['LightningDensity']}," \
              f" {item['GroundObjHeight']},'{item['Terrain']}',{item['GroundResis']},'{item['XCStringGroupName']}'," \
              f"'{item['FrontCondLineK']}','{item['FrontEarthLineK']}','{item['CNVLineTypeGroupName']}')"
        cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
