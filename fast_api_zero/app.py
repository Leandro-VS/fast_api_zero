from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_api_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/exercise', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_exercise():
    return "<html lang='pt-BR'>\
            <head>\
                <title>Exibição de Conteúdo</title>\
            </head>\
            <body>\
                <div>\
                    <p>author: Leandro</p>\
                </div>\
            </body>\
            </html>"
