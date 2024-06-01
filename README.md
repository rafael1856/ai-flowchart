# AI flowchart Generator

link
This program was tested in Linux.
And use [Ollama](https://ollama.com/)


## Features
 
It generates a summary for an interview transcript. 

# Folder structure

    ├── bin
    │   └── setup-conda.sh
    ├── conf
    │   └── conda_config.yaml
    ├── data
    │   ├── main_1717269909_llama3.dot
    │   ├── main_1717269909_llama3.drawio
    │   ├── main_1717270035_mistral.dot
    │   └── main_1717270035_mistral.drawio
    ├── docs
    │   └── Explanation.md
    ├── LICENSE
    ├── logs
    ├── README.md
    ├── src
    │   ├── dot2drawio.py
    │   └── main.py
    └── start.sh


## Quick start
For testing porpuses go to a web site with an interview transcript, download the interview as sample.txt (text file). 

Convert the text file in a json format running:
python src/convert-text-interview-2-json.py sample.txt

It will generate sample.json

Then run the analizer:
./start.sh

The result will be as screen output showing 2 analisis:
1) the result of using the ollama system call
2) the result of using the ollama API call

## Requirements

1) Get ollama working in your system
    link to ollama web site

2) Be sure the models you use for this app are alreay downloaded
        run: 'ollama list' to verify the models available.

3) This app requierd llama2 and llama3 models
   1) You can change the models in the code to see different results
   
Setup conda enviroment running:
source bin/setup-conda.sh

## Upcoming Features

* Allow to pass model via arguments
* Automate downloading interview from a url
* Provide an user interface (flask?)


test: get a summary from a 2 person interviews
    The source files must be in semi-json format:

also could summarize or do other tasks with text files.
The tooling that is used is:

[Ollama](https://ollama.com/)
   
model: llama3

It takes data transcribed from a meeting with format (list of json)
[
  {
    "speaker": "Alice",
    "text": "Good morning everyone, thanks for joining today's meeting."
  },
  {
    "speaker": "Bob",
    "text": "Morning, Alice. What's on the agenda for today?"
  }
]

Use a python program to convert a text interview from 

Then, it is fed to the ollama model to produce a summary. 
'''
It can do analisys changing the prompt
     prompt = """Your goal is to summarize the text that is given to you 
     in roughly 300 words. It is from a meeting between one or more people. 
     Only output the summary without any additional text. 
     Focus on providing a summary in freeform text with a summary of what 
     people said and the action items coming out of it."""
'''

TODO: automatize prompt change ?

TODO: diagram

Install

create enviroment
conda create --name my_enviroment_name -y

activate
conda activate my_enviroment_name

run
pip install -r requierments

run
python main.py