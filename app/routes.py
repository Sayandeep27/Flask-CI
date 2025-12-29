from flask import Blueprint, jsonify

main_bp = Blueprint("main", __name__)


# Simple health check endpoint


@main_bp.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})


@main_bp.route("/add/<int:a>/<int:b>", methods=["GET"])
def add(a, b):
    return jsonify({"result": a + b})
