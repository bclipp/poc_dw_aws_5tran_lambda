import requests
import backoff
import utils
import api


def lambda_handler(request, context):
    environment_variables: utils.ConfigVars = utils.get_variables()
    api.census_api(environment_variables["URL"])
    # built response
    # return response
    # example https: // github.com / fivetran / functions / blob / master / redshift / aws_lambda / lambda_function.py
    # docs https://fivetran.com/docs/functions
    return reponse
