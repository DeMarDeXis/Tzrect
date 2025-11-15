from flask import request, jsonify

from internal.service.msg_sender import MessageService

def init_router(app):
    service = MessageService()

    @app.route("/", methods=["GET"])
    def send_msg():
        name = request.args.get("name", "Recruto")
        msg = request.args.get("message", "Давай дружить!")
        result = service.format_message(name, msg)
        return jsonify({"message": result})
