from flask import jsonify, Blueprint
from utils import all_information

api_blueprint = Blueprint('api_blueprint', __name__)

@api_blueprint.route("/api/posts")
def inf_json():
    info = all_information()
    return jsonify(info)