# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Text, List, Any, Dict
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet, EventType

#I'm not sure if this still runs...
#However, it's intent was to use a custom action to ask for the next slot
#This is supposed to go run actions utter_ask_main_entree and utter_ask_drink
#However, I say not sure if it still runs, because I don't know...
class Test(Action):
    def name(self) -> Text:
        return "order_form_not_matching_on_purpose" #<- needs to match form name in domain.yml
    
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["main_entree", "drink"]
        print('Running slot thing')

        
        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                #Slot not filled yet, request the user to fill the slot next
                return [SlotSet("requested_slot", slot_name)]

        #All slots are filled now...
        return [SlotSet("requested_slot", None)]
#This is supposed to be ran once the form is activated
#It's a validation run...
class ValidateMainEntreeForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_main_entree_form"



    @staticmethod
    def main_entree_db() -> List[Text]:
        return [
          "hamburger",
          "a number one",
          "burger",
          "cheeseburger",
          "Chicken Nuggets", 
          "crispy chicken sandwich",
          "spicy crispy chicken sandwich",
          "deluxe crispy chicken sandwich",
          "6 piece chicken mcnuggets", 
          "4 piece chicken mcnuggets",
          "McChicken", 
          "filet-o-fish",
          "mcchicken",
          
          ]

    def validate_main_entree(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text,Any],
            ) -> Dict[Text, Any]:

        print('Validating main entree...')
        print(value)
        if value.lower() in self.main_entree_db():
            print('Good news it exists')
            return {"main_entree":value}
        else:
            print('Bad news it does not exist')
            dispatcher.utter_message(template="utter_wrong_menu_item", incorrect_item = value)
            return {"main_entree":None}
        

class ValidateDrinkForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_drink_form"

    @staticmethod
    def drink_db() -> List[Text]:
        return [
         "coke",
         "orange juice",
         "lemonade", 
         "sprite", 
         "coffee",
         ]

    def validate_drink(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
            ) -> Dict[Text, Any]:
        print('Validating drink order...')
        print(value)
        if value.lower() in self.drink_db():
            print('Good news it exists')
            return {"drink":value}
        else:
            print('Bad news it does not exist')
            dispatcher.utter_Message(tempate="utter_wrong_menu_item", incorrect_item = value)
            return {"drink":None}
 
class ActionSubmit(Action):
     def name(self) -> Text:
         return "action_submit"

     def run(
         self,
         dispatcher,
         tracker: Tracker,
         domain: "DomainDict"
         ) -> List[Dict[Text, Any]]:
         dispatcher.utter_message(template="utter_order", Main_entree=tracker.get_slot("main_entree"), Drink=tracker.get_slot("drink"))
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 

