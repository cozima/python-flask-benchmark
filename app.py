from boto3.dynamodb.conditions import Attr
from decimal import Decimal
from flask import Flask, request

import boto3
import msgpack
import os
import uuid

app = Flask(__name__)

dynamodb = boto3.resource(
    'dynamodb',
    region_name='eu-west-1'
)

@app.route('/measurements/<id>', methods=['GET'])
def find_by_id(id):

    table = dynamodb.Table("measurements_test")
    res = table.get_item(
        Key = {"id": id}
    )
    item = res.get('Item')
    if item is None:
        raise Exception()
    else:
        return msgpack.packb(item, default=default), 200

def default(obj):
    if isinstance(obj, Decimal):
        return float(str(obj))
    return obj

@app.route('/measurements', methods=['POST'])
def create():

    data = msgpack.unpackb(request.data, raw=False)

    vertices = [[Decimal(str(i)) for i in j] for j in data['vertices']]
    faces = data['faces']
    rings = [[[Decimal(str(i)) for i in j] for j in k] for k in data['rings']]

    measurement_data = {
        'id': str(uuid.uuid1()),
        'vertices': vertices,
        'faces': faces,
        'rings': rings
    }

    table = dynamodb.Table("measurements_test")
    arg = dict(Item=measurement_data)
    arg.update(ConditionExpression=Attr("id").not_exists())
    res = table.put_item(**arg)

    if res is None:
        raise Exception()
    else:
        return '', 201
        
if __name__ == '__main__':
    app.run()