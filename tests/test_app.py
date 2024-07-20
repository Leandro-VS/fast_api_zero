from http import HTTPStatus

from fast_api_zero.schemas import UserPublic


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
            'password': 'test',
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
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
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


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted!'}


# Exercicio
def test_delete_user_error(client, user):
    response = client.delete('/users/-1')

    assert response.status_code == HTTPStatus.NOT_FOUND


##########################################################
# Exercicios
def test_update_user_error(client, user):
    response = client.put(
        '/users/-1',
        json={
            'username': 'testusername2',
            'email': 'test2@test2.com',
            'password': 'novasenha',
            'id': -1,
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_create_user_error_usernameexist(client, user):
    # Enviando o UserSchema
    response = client.post(
        '/users/',
        json={
            'username': 'Teste',
            'password': 'test',
            'email': 'test2@test2.com',
        },
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_user_error_emailexist(client, user):
    # Enviando o UserSchema
    response = client.post(
        '/users/',
        json={
            'username': 'Teste2',
            'password': 'test',
            'email': 'test@test.com',
        },
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
