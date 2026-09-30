from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def inicio():
    return jsonify({
        "aplicacion": "Sistema de Gestión de Tareas",
        "estado": "funcionando",
        "version": "1.0"
    })


@app.route("/tareas")
def tareas():
    lista_tareas = [
        {
            "id": 1,
            "titulo": "Configurar GitHub Actions",
            "completada": True
        },
        {
            "id": 2,
            "titulo": "Construir imagen Docker",
            "completada": True
        },
        {
            "id": 3,
            "titulo": "Ejecutar Docker Bake",
            "completada": False
        }
    ]

    return jsonify(lista_tareas)


@app.route("/health")
def health():
    return jsonify({
        "status": "OK"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )