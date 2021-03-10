# McBot
McDonalds Drive through Chat Bot 

# Chatbot Platform: RASA

## How to install:

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

### Train rasa
1) rasa train

### Talk to McBot
1) rasa shell

## Sample conversation 1:
> User: Hi
> McBot Response: Greets and asks for main entree
> User: I'd like a burger
> McBot Response: Asks for side order
> User: I'd like french fries
> McBot Repsonse: Asks for size of side
> User: I'd like a small
> McBot Response: Asks for drink order
> User: I'd like a sprite
> McBot Response: Asks for dessert
> User: I'd like a McFlurry
> McBot Response: Repeats order back to user
> 
