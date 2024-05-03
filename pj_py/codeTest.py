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

    # fetch("http://192.168.1.64:3000/getMongo")
    # .then(response => response.json())
    # .then(json => console.log(json))
    # .catch(err => console.log(err))

    # if SearchId == 'BId':
    #     result = mycolbus.find_one({"BId": data['BId']}, {"_id": 0})  # 예시에서는 'BId' 값으로 검색하는 예를 제시하였으나,
    # elif SearchId == 'SId':
    #     result = mycolsub.find_one({"SId": data['SId']}, {"_id": 0})  # 'SId'에 대한 조회 예시

    # @app.get("/select")
# async def Select():
#     try: response = requests.get("http://192.168.1.64:3000/getMongo")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Failed to fetch data: {str(e)}")
    
#     return data