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

class ValidateOrderForm(FormValidationAction):

    validation_events = []

    def name(self) -> Text:
        return "validate_order_form"

    def invalid_item(
        self,
        slot_name: Any,
        slot_value: Any,
        dispatcher: CollectingDispatcher):

        print('we dont have')
        dispatcher.utter_message(template="utter_wrong_item", incorrect_item=slot_value)
        self.validation_events.append(SlotSet(slot_name, None))

    def validate_1_main_entree(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        print("Running is valid")
        print("1_main_entree")
        if not isinstance(slot_value, str):
            seperator = " "
            slot_value = seperator.join(slot_value)

        print(slot_value)


        if slot_value.lower() in self.main_entree_db():
            self.validation_events.append(SlotSet("1_main_entree", slot_value))
            return {"1_main_entree": slot_value}
        else:
            self.invalid_item("1_main_entree", slot_value, dispatcher)
            return {"1_main_entree": None}


    def validate_2_side(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        print("Running is valid")
        print("2_side")

        if not isinstance(slot_value, str):
            seperator = " "
            slot_value = seperator.join(slot_value)

        print(slot_value)

        if slot_value.lower() in self.side_db():
            self.validation_events.append(SlotSet("2_side", slot_value))
            return {"2_side": slot_value}
        else:
            self.invalid_item("2_side", slot_value, dispatcher)
            return {"2_side": None}

    def validate_3_size(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:


        if not isinstance(slot_value, str):
            seperator = " "
            slot_value = seperator.join(slot_value)

        print("Running is valid")
        print("3_size")
        print(slot_value)

        if slot_value.lower() in self.size_db():
            self.validation_events.append(SlotSet("3_size", slot_value))
            return {"3_size": slot_value}
        else:
            self.invalid_item("3_size", slot_value, dispatcher)
            return {"3_size": None}

    def validate_4_drink(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        print("Running is valid")
        print("4_drink")

        if not isinstance(slot_value, str):
            seperator = " "
            slot_value = seperator.join(slot_value)

        print(slot_value)

        if slot_value.lower() in self.drink_db():
            self.validation_events.append(SlotSet("4_drink", slot_value))
            return {"4_drink": slot_value}
        else:
            self.invalid_item("4_drink", slot_value, dispatcher)
            return {"4_drink": None}

    def validate_5_dessert(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        print("Running is valid")
        print("5_dessert")

        if not isinstance(slot_value, str):
            seperator = " "
            slot_value = seperator.join(slot_value)

        print(slot_value)

        if slot_value.lower() in self.dessert_db():
            self.validation_events.append(SlotSet("5_dessert", slot_value))
            return {"5_dessert": slot_value}
        else:
            self.invalid_item("5_dessert", slot_value, dispatcher)
            return {"5_dessert": None}

    @staticmethod
    def main_entree_db() -> List[Text]:
        return [
            "hamburger",
            "a number one",
            "burger",
            "cheeseburger",
            "cheese burger",
            "chicken nuggets", 
            "crispy chicken sandwich",
            "spicy crispy chicken sandwich",
            "deluxe crispy chicken sandwich",
            "6 piece chicken mcnuggets", 
            "4 piece chicken mcnuggets",
            "mcchicken",
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

    def extract_2_side(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict
    ) -> Dict[Text, Any]:

        missing_slots = (
            slot_name
            for slot_name in self.slots_mapped_in_domain(domain)
            if tracker.slots.get(slot_name) is None
        )

        if next(missing_slots, None) == "2_side":

            if tracker.get_intent_of_latest_message() == "deny":
                return {"2_side":"nothing", "3_size":"nothing"}

            elif tracker.get_intent_of_latest_message() == "affirm":
                dispatcher.utter_message(text="What side would you like?")
                return {"2_side": None}

        elif tracker.get_intent_of_latest_message() == "side":
            size_ordered = next(tracker.get_latest_entity_values("size"), None)
            if size_ordered != None:
                return {"2_side":tracker.latest_message.get("text"), "3_size":size_ordered}
            else:
                return {"2_side": tracker.latest_message.get("text")}

    def extract_5_dessert(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict
    ) -> Dict[Text, Any]:

        missing_slots = (
            slot_name
            for slot_name in self.slots_mapped_in_domain(domain)
            if tracker.slots.get(slot_name) is None
        )

        if next(missing_slots, None) == "5_dessert":

            if tracker.get_intent_of_latest_message() == "deny":
                return {"5_dessert":"nothing"}

            elif tracker.get_intent_of_latest_message() == "affirm":
                dispatcher.utter_message(text="What dessert would you like?")
                return {"5_dessert": None}
                
        elif tracker.get_intent_of_latest_message() == "dessert":
            return {"5_dessert":tracker.latest_message.get("text")}


class FinalOrder(Action):
    def name(self) -> Text:
        return "action_final_order"

    async def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        main_entree = tracker.get_slot("1_main_entree")
        side = tracker.get_slot("2_side")
        size = tracker.get_slot("3_size")
        drink = tracker.get_slot("4_drink")
        dessert = tracker.get_slot("5_dessert")

        message = ""
        if main_entree != "nothing": message = message + "\n" + main_entree
        if size != "nothing": message = message + "\n" + size
        if side != "nothing": message = message + " " + side
        if drink != "nothing": message = message + "\n" + drink
        if dessert != "nothing": message = message + "\n" + dessert

        if message == "":
            dispatcher.utter_message(text="You didn't order anything. :(")
        else:
            dispatcher.utter_message(text="For your order, I have:" + message)
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 

