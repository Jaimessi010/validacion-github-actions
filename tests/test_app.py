from app import app


def test_inicio():
    cliente = app.test_client()

    respuesta = cliente.get("/")

    assert respuesta.status_code == 200

    datos = respuesta.get_json()

    assert datos["estado"] == "funcionando"


def test_tareas():
    cliente = app.test_client()

    respuesta = cliente.get("/tareas")

    assert respuesta.status_code == 200

    datos = respuesta.get_json()

    assert len(datos) == 3


def test_health():
    cliente = app.test_client()

    respuesta = cliente.get("/health")

    assert respuesta.status_code == 200

    datos = respuesta.get_json()

    assert datos["status"] == "OK"