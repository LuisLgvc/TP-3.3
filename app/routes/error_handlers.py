from flask import Blueprint
from ..models.exceptions import CustomException, FilmNotFound, InvalidDataError

errors = Blueprint("errors", __name__)

@errors.app_errorhandler(CustomException)
def handle_custom_exception(error):
    return error.get_response(), error.status_code

@errors.app_errorhandler(FilmNotFound)
def handle_film_not_found(error):
    return error.get_response(), error.status_code

@errors.app_errorhandler(InvalidDataError)
def handle_indalid_data_error(error):
    return error.get_response(), error.status_code