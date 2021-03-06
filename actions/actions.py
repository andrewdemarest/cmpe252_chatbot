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

class ValidateSlots(Action):
    def name(self) -> Text:
        print("Custom action called...")
        return "validate_order_form"

    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
            ) -> List[EventType]:
        print("Running")
        extracted_slots: Dict[Text, Any] = tracker.slots_to_validate()
        print(extracted_slots)
        validation_events = []
        for slot_name, slot_value in extracted_slots.items():
            #Checks if slot is valid:
            if self.is_valid(slot_name, slot_value):
                validation_events.append(SlotSet(slot_name, slot_value))
            else:
                print('we dont have')
                dispatcher.utter_message(template="utter_wrong_item", incorrect_item = slot_value)
                validation_events.append(SlotSet(slot_name, None))

        return validation_events


    def is_valid(self, slot_name, slot_value: Any) -> bool:
        print("Running is valid")
        print(slot_name)
        print(slot_value)
        if slot_name.lower() == '1_main_entree':
            if slot_value.lower() in self.main_entree_db():
                return True
            else:
                return False
        elif slot_name.lower() == '2_side':
            if slot_value.lower() in self.side_db():
                return True
            else:
                return False
        elif slot_name.lower() == '3_size':
            if slot_value.lower() in self.size_db():
                return True
            else:
                return False
        elif slot_name.lower() == '4_drink':
            if slot_value.lower() in self.drink_db():
                return True
            else:
                return False
        elif slot_name.lower() == '5_dessert':
            if slot_value.lower() in self.dessert_db():
                return True
            else:
                return False
        else:        
            return False


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
            "nothing",
            ]

    @staticmethod
    def side_db() -> List[Text]:
        return [
            "fries",
            "french fries",
            "nothing",
            ]
    @staticmethod
    def size_db() -> List[Text]:
        return [
            "large",
            "small",
            "medium",
            "nothing",
            ]

    @staticmethod
    def drink_db() -> List[Text]:
        return [
            "coke",
            "sprite",
            "diet coke",
            "pepsi",
            "diet pepsi",
            "mountain dew",
            "lemonade", 
            "orange juice",
            "coffee",
            "nothing",
            ]
    @staticmethod
    def dessert_db() -> List[Text]:
        return [
            "vanilla shake",
            "chocolate shake",
            "mcflurry",
            "kiddie cone",
            "strawberry shake",
            "nothing",
            ]

 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 

