from flask import Blueprint, request, jsonify
from app.utils.rut_helper import validate_and_format_rut
from app.utils.api_caller import call_api

rut_blueprint = Blueprint("rut", __name__)


@rut_blueprint.route("/", methods=["GET"])
def index():
    try:
        rut = request.args.get("rut")
        if not rut:
            return jsonify(error="RUT not provided"), 400

        is_valid, formatted_rut = validate_and_format_rut(rut)
        if not is_valid:
            return jsonify(error="Invalid RUT"), 400

        json_data = call_api(formatted_rut)
        print(json_data)
        return jsonify(Rut=formatted_rut, Valid=is_valid, Data=json_data)
    except Exception as e:
        return jsonify(error=f"An error occurred: {str(e)}"), 500
