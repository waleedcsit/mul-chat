
from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.forms import FormValidationAction




class ValidateForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_save_info_form"

    def validate_grade(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        gradList = ["A", "B", "C", "D", "E", "F"]

        if value in gradList:
            return {"grade": value}
        else:
            dispatcher.utter_message(template="enter_valid_grade")
            return {"grade": None}