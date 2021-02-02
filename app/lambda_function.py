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
    json: api.RestReponse = rest_response["json"]
    response: api.LamdaResponse = api.create_response(json)
    return response

    # https://github.com/fivetran/functions/blob/master/fivetran_api/aws_lambda/lambda_api_call.py
    # example https: // github.com / fivetran / functions / blob / master / redshift / aws_lambda / lambda_function.py
    # docs https://fivetran.com/docs/functions
