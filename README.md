# sysml
## Installation
First, install the following to run:
- [NodeJS](https://nodejs.org/en/) (v4.x.x recommended)
- [MongoDB](https://www.mongodb.com/)
- [Git](https://git-scm.com/)
- [Python 3](https://www.python.org/)
- For more information [click here](https://webgme.readthedocs.io/en/latest/getting_started/dependencies.html)
- In order to create your own repository [Follow steps](https://webgme.readthedocs.io/en/latest/getting_started/creating_a_repository.html)

Second, start mongodb locally by running the `mongod` executable in your mongodb installation (you may need to create a `data` directory or set `--dbpath`).

Then, run `webgme start` from the project root to start . Finally, navigate to `http://localhost:8888` to start using sysml!

## What is SysML?
The Systems Modeling Language (SysML) is a general purpose modeling language used by engineering systems. SysML supports the detailed description, analysis and understanding of complex systems including hardware, software, information, personnel, procedures, in a pictorial representation. It was originally developed by an open source specification project, and includes an open source license for distribution and use. SysML is defined as an extension of a subset of the Unified Modeling Language (UML) using UML's profile mechanism. 

## Why we chose to work with SysML?
These days there are huge works being done on Cyber Physical Systems, which in turn depend on State Machine Diagrams and their transition flows. SysML/UML work extremely well to understand the transition flow between states in a state machine diagram. The clear understanding of these transitions from state to state is absolutely essential to understand proper working of designed cyber physical system without actually implementing it to work which would make use of large amounts of time, equipment, money. So, the SysML library modeled by us in WebGME would be seen as an asset by all computer engineers that work on developing or implementing new Cyber Physical Systems or people who debug the designed Cyber Physical Systems.
 
## Metamodel
The metamodel is defined by meta-rules for a state machine conforming to the SysML specifications. The current model definition includes support for various state elements including common statebases such as initial, state and final and pseudo states such as fork, merge and choice.

## How to run
If you are building your deployment from scratch, having installed the dependencies mentioned above, follow the steps:
1. Navigate to http://localhost:<port_number>. By default, it is 8088 so you can type in http://localhost:8888 in the address bar, if you haven't configured any changes.
2. If you want to see how a new project is created, Go to Create New. Otherwise, our deployment already has SysML_StateMachine as the project. If you choose to launch it, then skip step 3.
3. Import the .webgmex file that is provided with the project.
4. You have your state machine metamodel ready.
### Building a state machine
5. In order to check out the Examples, in the Visualizer pane on the left, navigate to Composition selector.
6. Double click Examples. There is a Airport check-in state machine example.
7. In order to create another example, inside the 'Examples' drag a StateMachine object from Decorated Part list, on your left.
8. You can rename the example to your choice by double-clicking on it.
9. Now navigate inside the <New_Example>. 
10. You will find state machine elements from the same Decorated Part list on your left. Drag and drop elements. Make connections by dragging arrows from the elements.

### Running Python plugin
11. This project already has a plugin that generates a code for a state machine interpreter, depending on the state machine. In order to run the plugin, navigate to inside of your state machine.
12. On the top left side, click on the 'play' button. It will list out all the plugins that can be currently executed for a state machine. Currently, it is Python Plugin. Click on it.
13.1. Make sure, if you are using your own deployment and the webgmex file for this project then you have config.plugin.allowServerExecution = true; line added to config/config.default.js from the root of your repository.
13.2. Run the plugin. This should generate an artifact by <Example_name>.py
14. Open the file. This is the state machine interpreter in Python. Run the file. You will see various states being traversed depending upon the guard and trigger conditions set.

To checkout the plugin code from the root of your repository, navigate to src/plugins/PythonPlugin/PythonPlugin. Open __init__.py


