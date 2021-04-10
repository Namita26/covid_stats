import logging
from flask import Blueprint, jsonify
from mongoengine.errors import DoesNotExist, ValidationError, InvalidQueryError, LookUpError, NotUniqueError, \
    FieldDoesNotExist

errors = Blueprint('errors', __name__)
logger = logging.getLogger('covid_stats')


def return_error(status, e_type, message):
    status_code = status
    response = {
        'success': False,
        'error': {
            'type': e_type,
            'message': message
        }
    }
    return jsonify(response), status_code


@errors.app_errorhandler(NotUniqueError)
def handle_incorrect_id(e):
    logger.debug(e)
    return return_error(400, "NOT_UNIQUE_ERROR", "The case already exists in our system.")


@errors.app_errorhandler(ValidationError)
def handle_incorrect_id(e):
    logger.debug(e)
    return return_error(400, "VALIDATION_FAILED", e.message)


@errors.app_errorhandler(FieldDoesNotExist)
def handle_incorrect_id(e):
    logger.debug(e)
    return return_error(400, "FIELD_DOES_NOT_EXIST", "Invalid Json")



@errors.app_errorhandler(DoesNotExist)
def handle_does_not_exist(e):
    logger.debug(e)
    return return_error(404, "DOES_NOT_EXIST", "The object does not exist.")


@errors.app_errorhandler(LookUpError)
def handle_look_up_error(e):
    logger.debug(e)
    return return_error(400, "FIELD_NOT_EXIST", e.message)


@errors.app_errorhandler(InvalidQueryError)
def handle_lookup_error(e):
    logger.debug(e)
    return return_error(400, "INVALID_QUERY_ERROR", "Not a valid object provided")


@errors.app_errorhandler(Exception)
def handle_unexpected_error(e):
    logger.exception(e)
    return return_error(500, "UNEXPECTED_EXCEPTION", 'An unexpected error has occurred.')
