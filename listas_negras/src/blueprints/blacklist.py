from flask import Flask, jsonify, request, Blueprint
from ..commands.create_mail import CreateMail
from ..commands.get_mail import GetMail

blacklist_blueprint = Blueprint('blacklist', __name__)

# 1. Creación de email.
@blacklist_blueprint.route('/blacklists', methods = ['POST'])
def create_list():
    json = request.get_json()
    # fields_request=['username','password','email','dni','fullName','phoneNumber']

    # for field in fields_request:
    #     if field not in json:
    #         json[field]=""
    
    clientIp = request.remote_addr

    token_bearer=request.headers.get('Authorization')
    if token_bearer is None:
        token=""
    else:
       token=token_bearer.replace('Bearer ', '')
    
    result = CreateMail(json['email'], json['app_uuid'], json['blocked_reason'],clientIp ,token).execute()    
    return jsonify(result),201

# 2. Consultar Email.
@blacklist_blueprint.route('/blacklists/<email>', methods = ['GET'])
def get_mail(email):
    token_bearer=request.headers.get('Authorization')
    if token_bearer is None:
        token=""
    else:
       token=token_bearer.replace('Bearer ', '')

    result = GetMail(email,token).execute()    
    return jsonify(result),200