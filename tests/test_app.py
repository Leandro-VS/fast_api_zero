from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_create_user(client):
    # Enviando o UserSchema
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )

    # Validar o status code
    assert response.status_code == HTTPStatus.CREATED
    # Validar o UserPublic
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testusername',
                'email': 'test@test.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'testusername2',
            'email': 'test2@test2.com',
            'password': 'novasenha',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'testusername2',
        'email': 'test2@test2.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted!'}


# EXERCICIOS
# def test_exercise_deve_retornar_ok_e_leandro():
#     client = TestClient(app)  # Arrange

#     response = client.get('/exercise')  # Act
#     print(response)
#     assert response.status_code == HTTPStatus.OK  # Assert
#     assert response.text == "<html lang='pt-BR'>\
#             <head>\
#                 <title>Exibição de Conteúdo</title>\
#             </head>\
#             <body>\
#                 <div>\
#                     <p>author: Leandro</p>\
#                 </div>\
#             </body>\
#             </html>"  # Assert
