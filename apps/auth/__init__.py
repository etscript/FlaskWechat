__author__ = 'Ran'

from flask import Blueprint
auth = Blueprint('auth', __name__)
from ..auth import urls