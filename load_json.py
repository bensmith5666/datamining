# f =  open('C:/Users/Ben/OneDrive - std.uestc.edu.cn/桌面/数据挖掘课程数据集/data-co.json', 'r',encoding='utf-8')
# data = [lines.strip('\n') for lines in f.readlines()]
# f.close()
# # print(data)
# f1= open('C:/Users/Ben/OneDrive - std.uestc.edu.cn/桌面/数据挖掘课程数据集/1.json','w',encoding='utf-8')
# f1.writelines(data)
# f1.close()

import ast
from json import encoder
import pandas as pd
import os
import numpy as np
import json

with open('C:/Users/Ben/OneDrive - std.uestc.edu.cn/桌面/数据挖掘课程数据集/1.json', 'r') as f:
    data = ast.literal_eval(f.read())
# print(type(data[0]))
node_data = pd.read_csv('C:/Users/Ben/OneDrive - std.uestc.edu.cn/桌面/数据挖掘课程数据集/dash-opioid-epidemic/data/nodes.csv')
node_data_select = node_data[["node_id","address","lon","lat"]].values    
node_range = ['1-2','2-3','3-4','4-5','5-10','10-50','over50']

base_dir = os.path.dirname(__file__)
for i in data:
    os.makedirs(os.path.join(base_dir,i["time"].replace(':','.')))
    node_id_temp = []
    for j in range(len(node_range)):
        node_id_temp.append([])
        # os.makedirs( os.path.join(  os.path.join(base_dir,i["time"]) ,  node_range[j]) )
    for j in i["data"]:
        score = i["data"][j]
        if score >=1 and score < 2:
            node_id_temp[0].append(j)
        if score >=2 and score < 3:
            node_id_temp[1].append(j)
        if score >=3 and score < 4:
            node_id_temp[2].append(j)
        if score >=4 and score < 5:
            node_id_temp[3].append(j)
        if score >=5 and score < 10:
            node_id_temp[4].append(j)
        if score >=10 and score < 50:
            node_id_temp[5].append(j)
        if score >=50:
            node_id_temp[6].append(j)
    for j in range(len(node_id_temp)):
        geojson = {}
        geojson["type"] = "FeatureCollection"
        features = []
        for k in node_id_temp[j]:
            temp = {}
            temp["type"] = "Feature"
            temp["properties"] = {}
            temp["geometry"] = {}
            for m in node_data_select:
                # print(m)
                if m[0] == k:
                    # print(1)
                    temp["properties"]["nodeid"] = k
                    temp["properties"]["name"] = m[1]
                    temp["properties"]["range"] = node_range[j]
                    temp["geometry"]["type"] = "Polygon"
                    temp["geometry"]["coordinates"] = [[[m[2]-0.01,m[3]-0.01],[m[2]-0.01,m[3]+0.01],[m[2]+0.01,m[3]+0.01],[m[2]+0.01,m[3]-0.01]]]
            features.append(temp)
        geojson["features"] = features
        jsonData = json.dumps(geojson)
        fileObject = open(os.path.join(  os.path.join(base_dir,i["time"].replace(':','.')) ,  node_range[j] + ".geojson"), 'w', encoding = "utf-8")
        fileObject.write(jsonData)
        fileObject.close()
           





# {
#   "type": "FeatureCollection",
#   "features": [
#     {
#       "type": "Feature",
#       "properties": {
#         "nodeid": "001e0611804d",
#         "name": "ComEd Training Center"
#       },
#       "geometry": {
#         "type": "Point",
#         "coordinates": [
#           -87.659467,
#           41.829806
#         ]
#       }
#     }
#   ]
# }
