# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import base64
import json

from flask import Flask
from flask import request
from airports import Airports

app = Flask(__name__)
airport_util = Airports()


def _base64_decode(encoded_str):
    # Add paddings manually if necessary.
    num_missed_paddings = 4 - len(encoded_str) % 4
    if num_missed_paddings != 4:
        encoded_str += b'=' * num_missed_paddings
    return base64.b64decode(encoded_str).decode('utf-8')

@app.route('/airportName', methods=['GET'])
def airportName():
    print('airportName_airportName_airportName_airportName')
    encoded_info = request.headers.get('X-Endpoint-API-UserInfo', None)
    custom_header = request.headers.get('custom', None)
    print("print custom header")
    print(custom_header)

    if encoded_info:
        info_json = _base64_decode(encoded_info)
        user_info = json.loads(info_json)
        #print(user_info)
        print("print user email")
        print(user_info['email'])
    else:
        print('user info not provided')
    """Given an airport IATA code, return that airport's name."""
    iata_code = request.args.get('iataCode')
    if iata_code is None:
      return 'No IATA code provided.', 400
    maybe_name = airport_util.get_airport_by_iata(iata_code)
    if maybe_name is None:
      return 'IATA code not found : %s' % iata_code, 400
    return maybe_name, 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
