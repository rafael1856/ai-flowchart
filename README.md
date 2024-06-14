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

Then run the dot flowchart generator:
./start.sh <path to your file>

example: 
./start.sh src/main.py

The result will be two files, one per model in the data folder with format:
name_python_file-epochtimestamp-model_name.dot

    main_1717269909_llama3.dot
    main_1717271662_mistral.dot

# Run from other folders
python path_to_ai-flowchart/src/main.py <your_file_to_dottify>
example:
python ~/dev/projects/ai-flowchart/src/main.py ~/dev/projects/ai-chatsql/docs/Application-Flow.txt


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
* Provide an user interface (flask)
