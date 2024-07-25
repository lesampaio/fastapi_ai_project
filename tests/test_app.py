from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_project.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (Organização)
    # Act (Ação-Executar bloco de código que precisa ser testado)
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK  # Assert (Afirmação)
    assert response.json() == {'message': 'Olá, mundo!'}  # Assert (Afirmação)
