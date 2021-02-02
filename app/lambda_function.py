"""

"""
import utils
import api


def lambda_handler(request, context):
    """

    :param request:
    :param context:
    :return:
    """
    environment_variables: utils.ConfigVars = utils.get_variables()
    rest_response: dict = api.app_api(environment_variables["URL"])
    json: dict = rest_response["json"]
    response: dict = api.create_response(json)
    return response


    # example https: // github.com / fivetran / functions / blob / master / redshift / aws_lambda / lambda_function.py
    # docs https://fivetran.com/docs/functions
