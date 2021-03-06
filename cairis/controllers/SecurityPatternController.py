#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

import sys
if (sys.version_info > (3,)):
  import http.client
  from http.client import BAD_REQUEST, CONFLICT, NOT_FOUND, OK
else:
  import httplib
  from httplib import BAD_REQUEST, CONFLICT, NOT_FOUND, OK

from flask import session, request, make_response
from flask_restful import Resource
from cairis.daemon.CairisHTTPError import ARMHTTPError, ObjectNotFoundHTTPError
from cairis.data.SecurityPatternDAO import SecurityPatternDAO
from cairis.tools.JsonConverter import json_serialize
from cairis.tools.MessageDefinitions import SecurityPatternMessage
from cairis.tools.SessionValidator import get_session_id, get_model_generator

__author__ = 'Shamal Faily'


class SecurityPatternsAPI(Resource):

  def get(self):
    session_id = get_session_id(session, request)
    dao = SecurityPatternDAO(session_id)
    sps = dao.get_security_patterns()
    dao.close()
    resp = make_response(json_serialize(sps, session_id=session_id), OK)
    resp.contenttype = 'application/json'
    return resp

  def post(self):
    session_id = get_session_id(session, request)
    dao = SecurityPatternDAO(session_id)
    new_sp = dao.from_json(request)
    dao.add_security_pattern(new_sp)
    dao.close()
    resp_dict = {'message': new_sp['theName'] + ' created'}
    resp = make_response(json_serialize(resp_dict), OK)
    resp.contenttype = 'application/json'
    return resp


class SecurityPatternByNameAPI(Resource):

  def get(self,name):
    session_id = get_session_id(session, request)
    dao = SecurityPatternDAO(session_id)
    sp = dao.get_security_pattern(name)
    dao.close()
    resp = make_response(json_serialize(sp, session_id=session_id), OK)
    resp.contenttype = 'application/json'
    return resp


  def put(self,name):
    session_id = get_session_id(session, request)
    dao = SecurityPatternDAO(session_id)
    upd_sp = dao.from_json(request)
    dao.update_security_pattern(upd_sp,name)
    dao.close()
    resp_dict = {'message': upd_sp['theName'] + ' updated'}
    resp = make_response(json_serialize(resp_dict), OK)
    resp.contenttype = 'application/json'
    return resp


  def delete(self,name):
    session_id = get_session_id(session, request)
    dao = SecurityPatternDAO(session_id)
    dao.delete_security_pattern(name)
    dao.close()

    resp_dict = {'message': name + ' deleted'}
    resp = make_response(json_serialize(resp_dict), OK)
    resp.headers['Content-type'] = 'application/json'
    return resp

class SituateSecurityPatternAPI(Resource):

  def post(self,security_pattern_name,environment_name):
    session_id = get_session_id(session, request)
    dao = SecurityPatternDAO(session_id)
    dao.situate_security_pattern(security_pattern_name,environment_name)
    dao.close()
    resp_dict = {'message': security_pattern_name + ' situated'}
    resp = make_response(json_serialize(resp_dict), OK)
    resp.contenttype = 'application/json'
    return resp
