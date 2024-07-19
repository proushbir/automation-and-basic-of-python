import requests
import json
import random
import string

#base url
base_url="https://reqres.in/api"

#auth token
auth_token="token ....token value"

def generate_random_email():
    domain="test.com"
    email_length=8
    random_string=''.join(random.choice(string.ascii_lowercase)for _ in range(email_length))
    email=random_string + "@" + domain
    return email

def generate_random_phone():
    phone_number="98" + ''.join(random.choices(string.digits,k=8))
    return phone_number

#post request
def put_request(user_id):
    url=base_url + f"/users/{user_id}"
    print("put url: ",url)
    headers={"Authorization":auth_token}
    data={
        "name":"Proush",
        "email":generate_random_email(),
        "phone_number":generate_random_phone(),
        "job":"QA learner"
    }

    response=requests.put(url,json=data,headers=headers)
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json put response data:",json_str)
    assert response.status_code==200
    print(".......Put/user is updated successfully.........")

put_request(553)