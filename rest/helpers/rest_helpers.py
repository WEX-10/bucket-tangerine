from flask import request, jsonify


def wants_json():
    """Returns True if the client requested a JSON response via query parameter."""
    return request.args.get("json") in ("1", "true", "True")

def fact_to_json(fact):
    """Converts a Fact object to a JSON-serializable dictionary."""
    return {
        "id": getattr(fact, "id", None),
        "fact": fact.fact,
        "category": getattr(fact, "category", None),
        "likes": getattr(fact, "likes", 0),
        "dislikes": getattr(fact, "dislikes", 0)
    }

def error_response(message, status_code=200):
    """Returns a JSON error response with the given message and status code."""
    return jsonify({"error": message}), status_code
