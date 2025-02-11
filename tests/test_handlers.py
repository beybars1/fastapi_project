import json


async def test_create_user(client, get_user_from_database):
    new_user = {
        "name": "Johnggg",
        "surname": "Doe",
        "email": "test@gmail.com",
        "password": "string"
        }
    response = client.post("/user/", data=json.dumps(new_user))
    data_from_response = response.json()
    print(data_from_response)
    assert response.status_code == 200
    assert data_from_response["name"] == new_user["name"]
    assert data_from_response["surname"] == new_user["surname"]
    assert data_from_response["email"] == new_user["email"]
    assert data_from_response["is_active"] == True
    users_from_db = await get_user_from_database(data_from_response["user_id"])
    assert len(users_from_db) == 1
    users_from_db = dict(users_from_db[0])
    assert users_from_db["name"] == new_user["name"]
    assert users_from_db["surname"] == new_user["surname"]
    assert users_from_db["email"] == new_user["email"]
    assert users_from_db["is_active"] == True
    assert str(users_from_db["user_id"]) == data_from_response["user_id"]
    