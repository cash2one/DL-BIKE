# coding: utf-8

import uuid
import hmac
import ujson
import hashlib
import redis

class SessionData(dict):

    def __init__(self, session_id, hmac_key):
        self.session_id = session_id
        self.hmac_key = hmac_key

class Session(SessionData):

    def __init__(self, session_manager, request_handler, subsession):
        if not isinstance(subsession, (int)) or subsession <= 0:
            raise Exception("subsession format wrong")
        self.session_manager = session_manager
        self.request_handler = request_handler
        try:
            current_session = session_manager.get(subsession, request_handler)
        except InvalidSessionException:
            current_session = session_manager.get(subsession)
        for key, data in current_session.iteritems():
            self[key] = data
        self.session_id = current_session.session_id
        self.hmac_key = current_session.hmac_key
        self.subsession = subsession

    def save(self):
        self.session_manager.set(self.request_handler, self)

class SessionManager(object):

    def __init__(self, secret, store_options, session_timeout):
        self.secret = secret
        self.session_timeout = session_timeout
        try:
            self.pool = redis.ConnectionPool(host=store_options['redis_host'],
                port=store_options['redis_port'], password=store_options['redis_pass'])
            self.redis = redis.StrictRedis(connection_pool=self.pool)
        except Exception as e:
            print e

    def _fetch(self, session_id):
        try:
            session_data = raw_data = self.redis.get(session_id)
            if raw_data != None:
                self.redis.setex(session_id, self.session_timeout, raw_data)
                session_data = ujson.loads(raw_data)
            if type(session_data) == type({}):
                return session_data
            else:
                return {}
        except IOError:
            return {}

    def get(self, subsession, request_handler = None):
        if (request_handler == None):
            session_id = None
            hmac_key = None
        else:
            session_id = request_handler.get_secure_cookie("session_id")
            hmac_key = request_handler.get_secure_cookie("verification")
        if session_id == None:
            session_exists = False
            session_id = self._generate_id()
            hmac_key = self._generate_hmac(session_id)
        else:
            session_exists = True
        check_hmac = self._generate_hmac(session_id)
        if hmac_key != check_hmac:
            raise InvalidSessionException()
        session = SessionData(session_id, hmac_key)
        if session_exists:
            session_data = self._fetch(session_id+ "_" + str(subsession))
            for key, data in session_data.iteritems():
                session[key] = data
        return session

    def set(self, request_handler, session):
        request_handler.set_secure_cookie("session_id", session.session_id)
        request_handler.set_secure_cookie("verification", session.hmac_key)
        session_data = ujson.dumps(dict(session.items()))
        self.redis.setex(session.session_id+"_"+str(session.subsession), self.session_timeout, session_data)

    def _generate_id(self):
        new_id = hashlib.sha256(self.secret + str(uuid.uuid4()))
        return new_id.hexdigest()

    def _generate_hmac(self, session_id):
        return hmac.new(session_id, self.secret, hashlib.sha256).hexdigest()

    def close(self):
        self.redis.close()

class InvalidSessionException(Exception):
    pass
