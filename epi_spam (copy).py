from data_utils import awsutils, generalutils, apiutils, epi_utils

user = 'epiUser'
password = 'epiPassword'


class EpiSpam(object):

    def __init__(self):
        self.ssm_base = awsutils.SSMBase()
        self.epi_user = self.ssm_base.get_ssm_parameter(user)
        self.epi_password = self.ssm_base.get_ssm_parameter(password)
        self.api_key = epi_utils.create_api_key_string(self.epi_user, self.epi_password)
    
    def post_spam_reason(self, clientId, recipientListId, recipientId, spam, spam_grund):
        #components of the request:
        link = f"https://api.campaign.episerver.net/rest/{clientId}/recipients/{recipientListId}/{recipientId}"

        headers = {'accept': 'application/json',
                        'Authorization': f'BASIC {self.api_key}',
                        'Content-Type': 'application/x-www-form-urlencoded'
                        }
        body = {
            "mode": "set",
            "data": f"&data.Spam Grund={spam_grund}&data.Spam={spam}&"
        }

        # This is executing the request
        return apiutils.handle_post_request(url=link, body=body, headers=headers)
