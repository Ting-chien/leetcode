import redis
import json
import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, DateTime, String

app = Flask(__name__) 
db = SQLAlchemy(app)

class Redis(object):
    _pool = None

    def __init__(self):
        self._pool = redis.ConnectionPool('localhost', 6379)

    def get_connection(self):
        return redis.StrictRedis(connection_pool=self._pool)

class Teacher(db.Model):

    __tablename__ = 'teacher'
    __table_args__ = ({
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8', 
        'mysql_collate': 'utf8_unicode_ci'
    })

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(128))
    deleted_at = Column(DateTime, default=datetime.datetime.utcnow) 

    def __init__(self, name) -> None:
        self.name = name


@app.route('/admin/teachers', methods=['GET'])
def get_teachers():
    deleted = request.args.get('deleted')
    page = request.args.get('page')
    size = request.args.get('size')

    cache = Redis().get_connection()
    cache_key = '{page}-{size}-{deleted}'.format(page=page, size=size, deleted=deleted)
    result = cache.get(cache_key)

    if result:
        return result
    else:
        offset = size * (page - 1)

        if deleted:
            teachers = Teacher.query.filter(Teacher.deleted_at != None).offset(offset).limit(size).all()
        else:
            teachers = Teacher.query.offset(offset).limit(size).all()

        cache.set(cache_key, json.dumps(teachers))

        return jsonify(teachers)