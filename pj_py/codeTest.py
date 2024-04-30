# @app.post("/getMongo/")
# async def get_mongo(data:dict): #{"BId": "0007"}
#     try:
#         response = requests.get("http://192.168.1.64:3000/getMongo")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Failed to fetch data: {str(e)}")

#     data = response.json()  # 전달 받은 데이터를 JSON 형태로 변환
#     print(data)
#     pathlist = data.get("path_list", [])
#     print(pathlist)

#     for data_item in pathlist:
#         idtype = data_item.get('SearchId')
#         if idtype == 'BId':
#             mycolbus.insert_one(data_item)
#         elif idtype == 'SId':
#             mycolsub.insert_one(data_item)

#     result = mycolbus.find_one({"BId": "0007"}, {"_id":0})
#     return result