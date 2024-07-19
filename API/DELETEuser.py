import requests
import json

#base url
base_url="https://reqres.in/api"

#auth token
auth_token="token ....token value"

#post request
def delete_request(user_id):
    url=base_url + f"/users/{user_id}"
    print("delete url: ",url)
    headers={"Authorization":auth_token}
    response=requests.delete(url,headers=headers)
    assert response.status_code==204
    print(".......Delete/user is deleted successfully.........")

delete_request(3)