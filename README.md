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
1) conda install ujson
2) conda install tensorflow

### Download RASA
1) pip install rasa

### Train rasa
1) rasa train

### Talk to McBot
1) rasa shell
