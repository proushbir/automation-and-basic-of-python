import requests
import json

#base url
base_url="https://reqres.in/api"

#authorization
auth_token="token ...auth_token"

#post request
def post_request(user_names):
    url=base_url + "/users/"
    print("Post url: ", url)
    headers={"Authorization":auth_token}
    user_ids=[]

    for name in user_names:
        data={
            "name":name,
            "job":"QA learner"
        }
        response=requests.post(url,json=data,headers=headers)
        json_data=response.json()
        json_str=json.dumps(json_data,indent=4)
        print("Json data post response: ", name, ":", json_str)
        user_id=json_data.get("id")
        if user_id:
            user_ids.append(user_id)
        assert response.status_code==201
        assert "name" in json_data
        print(".........Post/user is created successfully.",name,"........")

    return user_ids

#user name example:
user_names=["Proush","Rupak","Saroj","Surakshya","Ushav","Nikita","Sapana"]

for _ in range(0,10):
    user_ids=post_request(user_names)
    print("Created user Id:",user_ids)