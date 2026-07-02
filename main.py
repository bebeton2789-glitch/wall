import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def alexa_skill():
    # Recibe el JSON que Alexa envía
    data = request.get_json()

    # Detecta el tipo de request
    request_type = data["request"]["type"]

    if request_type == "LaunchRequest":
        # Cuando el usuario abre la skill
        response_text = "¡Hola Anthony! Tu skill ya está conectado a Railway."
    elif request_type == "IntentRequest":
        # Cuando el usuario dice algo que activa un intent
        intent_name = data["request"]["intent"]["name"]
        if intent_name == "PreguntarIAIntent":
            # Aquí puedes procesar la pregunta del usuario
            user_question = data["request"]["intent"]["slots"]["texto"]["value"]
            response_text = f"Recibí tu pregunta: {user_question}"
        else:
            response_text = "Lo siento, no entendí tu petición."
    else:
        response_text = "No sé cómo manejar esta solicitud."

    # Devuelve la respuesta en formato Alexa
    response = {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": response_text
            },
            "shouldEndSession": False
        }
    }
    return jsonify(response)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
