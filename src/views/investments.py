from src.helpers import auth
from src.investment import Investment
from flask import request, jsonify
from botocore.exceptions import ClientError
from flask import send_file


@auth.login_required
def available_investments():
    investment_type = request.environ.get("REQUEST_URI").split("/")[-1]
    investment_type = investment_type.capitalize()
    controller = Investment(investment_type)
    output = controller.get_investments_available()
    return jsonify({investment_type: output}), 200


@auth.login_required
def price_investments(investment_name, start_date, end_date):
    try:
        investment_type = request.environ.get("REQUEST_URI").split("/")[2]
        investment_type = investment_type.capitalize()
        investment_name = investment_name.capitalize()
        controller = Investment(investment_type)
        data = controller.get_investment_prices(investment_name, start_date, end_date)
        return jsonify(data), 200
    except ClientError:
        return (
            jsonify(
                {
                    "message": "The first payment date must be previus than today or the end date"
                }
            ),
            400,
        )
    except Exception:
        return (
            jsonify(
                {"message": "The first payment date must has the format dd-mm-yyyy"}
            ),
            400,
        )


@auth.login_required
def export():
    try:
        investment_type = request.environ.get("REQUEST_URI").split("/")[2]
        investment_type = investment_type.capitalize()
        controller = Investment(investment_type)
        file = controller.export_all_investment_prices()
        return send_file(file, attachment_filename="data.csv")
    except:
        return jsonify({"message": "Something went wrong"}), 500
