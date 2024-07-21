import json
import requests

#base url
base_url="https://reqres.in/api"

#authorization
auth_token="token ...auth_token"

def get_request(user_id):
    url=base_url + f"/users/{user_id}"
    print(f"Get the url: {url}")
    headers={"Authorization": auth_token}
    response=requests.get(url,headers=headers)
    assert response.status_code==200
    json_data=response.json()
    json_str=json.dumps(json_data,indent=2)
    print("Get json data per user: ",json_str)

get_request(3)