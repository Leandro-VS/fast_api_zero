from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_exercise_deve_retornar_ok_e_leandro():
    client = TestClient(app)  # Arrange

    response = client.get('/exercise')  # Act
    print(response)
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.text == "<html lang='pt-BR'>\
            <head>\
                <title>Exibição de Conteúdo</title>\
            </head>\
            <body>\
                <div>\
                    <p>author: Leandro</p>\
                </div>\
            </body>\
            </html>"  # Assert
