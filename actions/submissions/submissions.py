from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.forms import FormValidationAction

import requests
from rasa_sdk.types import DomainDict


def getFieldPackage():
    query = {'method': 'askFee', 'prg_name': 'BSCS'}
    response = requests.get('https://lab.mul.edu.pk/api/model/api.php', params=query)
    print(response.json())

    response_as_dict = response.json()

    total = response_as_dict['DATA'][0]['total_pkg']
    print(total)

    return total


class SubmitForm(Action):

    def name(self) -> Text:
        return "action_submit_save_info_form"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        total = getFieldPackage()
        dispatcher.utter_message("Total amount = %s" % total)
        return []
