# McBot
McDonalds Drive through Chat Bot 

# Chatbot Platform: RASA

## How to install:
* RASA's official installation documentation:
https://rasa.com/docs/rasa/installation/

* abridged walk through below

### Pre-requisite: 
1) Download Anaconda

### Set-up RASA environment
* Note: example name of Rasa environment: rasaMcD
1) Open Anaconda Prompt
1) Download and Navigate to this git directory
2) conda create --name rasaMcD python==3.8.5
3) conda activate rasaMcD

### Download RASA dependencies
#### Main
1) conda install ujson
2) conda install tensorflow

#### Optional
* Dependent on OS/Python version
1) pip install typing_extensions

### Download RASA
1) pip install rasa

### Download RASA X 
* optional chatbot GUI
1) pip install rasa-x --extra-index-url https://pypi.rasa.com/simple

### Train rasa
1) rasa train

### Start up Action Server
1) Open separate terminal
2) rasa run actions

### Talk to McBot
* 2 options:
1) rasa shell
2) rasa x

## Sample conversation 1:
- User: Hi
- McBot Response: Greets and asks for main entree
- User: I'd like a burger
- McBot Response: Asks for side order
- User: I'd like french fries
- McBot Repsonse: Asks for size of side
- User: I'd like a small
- McBot Response: Asks for drink order
- User: I'd like a sprite
- McBot Response: Asks for dessert
- User: I'd like a McFlurry
- McBot Response: Repeats order back to user
## Sample conversation 2:
- User: What time are you open?
- McBot Response: Responds with store hours.
- User: Are you open on holidays?
- McBot Response: Responds with holiday schedule.
- User: What are your holiday hours?
- McBot Response: Responds with the holiday hours.
## Sample conversation 3 (for the talkative customer):
- User: Hi how are you?
- McBot: Livin' the dream!
- User: What's new with you?
- McBot: Surviving
- User: What's your name
- McBot: My name is McBot
- User: Cool how's the weather?
- McBot: The weather is sure something.
- User: You are awesome!
- McBot: You are too kind.
## Other notes:
- McBot responds to query about the menu on a per item basis. e.g. what main entrees do you have?.
- McBot responds to basic chitchat. Especially compliments, or if the manager needs to be seen.
- McBot does check if what you're ordering is actually on the menu. For instance McBot does not serve a guac burger.

