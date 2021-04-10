import json
from datetime import datetime

from app.blueprints.covid_cases.models.case import Case

TYPE_DATE_MAPPING = {
    "active": "found_active_on",
    "deceased": "deceased_on",
    "recovered": "recovered_on"
}

TYPE_PERIOD_MAPPING = {
    "daily": "$dayOfYear",
    "weekly": "$week",
    "yearly": "$year"
}


def fetch_total_covid_cases_using_filters(filters, case_type, period, start_date, end_date):
    """
    Total (OLD and + NEW) cases between given date range based on the filters.
    :param filters:
    :param case_type:
    :param period:
    :param start_date:
    :param end_date:
    :return:
    """
    field_name = TYPE_DATE_MAPPING.get(case_type, "created_at")
    period_name = TYPE_PERIOD_MAPPING.get(period, "yearly")

    all_filters = {
        field_name:
            {
                "$gte": datetime.strptime(start_date, '%Y-%m-%d'),
                "$lte": datetime.strptime(end_date, '%Y-%m-%d')
            }
    }

    # adding location filters to date filters
    all_filters.update(filters)

    aggregation_pipeline = [
        {
            "$match": all_filters
        },
        {
            "$group": {
                "_id": {period_name: '$' + field_name},
                "cases": {"$sum": 1}
            }
        }
    ]

    cases = list(Case.objects.aggregate(aggregation_pipeline))
    return [{"period_counter": case["_id"], "cases": case["cases"]} for case in cases]


def fetch_covid_cases(filters, case_type, period, start_date, end_date):
    """
    Get all covid cases based on given filters.
    :param filters: location filters
    :param case_type:
    :param period:
    :param start_date:
    :param end_date:
    :return:
    """
    return fetch_total_covid_cases_using_filters(filters, case_type, period, start_date, end_date)


def register_covid_case(case_details):
    """
    Creates a new covid case mongo object and saves in the mongo document.
    :param case_details: request payload for new covid registration
    :return: New covid case mongo object
    """
    new_covid_case = Case.from_json(json.dumps(case_details))
    new_covid_case.save()
    return new_covid_case.to_json_dict()
