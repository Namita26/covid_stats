import logging

from flask import request, Blueprint

from .service import fetch_covid_cases, register_covid_case

from app.utils.request_response_utils import make_json_response, get_filters

covid_cases_blueprint = Blueprint("covid_cases_api", __name__)


ALLOWED_FILTERS = {
    "area": "location__area",
    "state": "location__state",
    "country": "location__country",
    "continent": "location__continent"
}


@covid_cases_blueprint.route("", methods=["POST"])
def add():
    case_details_payload = request.get_json()
    new_covid_case = register_covid_case(case_details_payload)
    return make_json_response(new_covid_case, 201, {})


@covid_cases_blueprint.route("", methods=["GET"])
def cases():
    """
    Get covid cases based on the filters
    """

    filters = get_filters(request, ALLOWED_FILTERS)

    case_type = request.args.get("type")
    period = request.args.get('period', default='daily')
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    return make_json_response(fetch_covid_cases(filters, case_type, period, start_date, end_date), 200, {})
