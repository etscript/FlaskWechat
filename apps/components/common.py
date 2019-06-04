from flask import jsonify

def returnData(code, msg, data):
    returnjsondict = {
        "code": code,
        "msg": str(msg),
        "data": data
    }
    return jsonify(returnjsondict)