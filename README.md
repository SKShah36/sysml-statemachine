# sysml
## Installation
First, install the following to run:
- [NodeJS](https://nodejs.org/en/) (v4.x.x recommended)
- [MongoDB](https://www.mongodb.com/)

Second, start mongodb locally by running the `mongod` executable in your mongodb installation (you may need to create a `data` directory or set `--dbpath`).

Then, run `webgme start` from the project root to start . Finally, navigate to `http://localhost:8888` to start using sysml!

## What is SysML?
The Systems Modelling Language (SysML) is a general purpose modelling language used by engineering systems. SysML supports the detailed description, analysis and understanding of complex systems including hardware, software, information, personnel, procedures, in a pictorial representation. It was originally developed by an open source specification project, and includes an open source license for distribution and use. SysML is defined as an extension of a subset of the Unified Modeling Language (UML) using UML's profile mechanism. 

## Why we chose to work with SysML?
These days there are huge works being done on Cyber Physical Systems, which in turn depend on State Machine Diagrams and their transition flows. SysML/UML work extremely well to understand the transition flow between states in a state machine diagram. The clear understanding of these transitions from state to state is absolutely essential to understand proper working of designed cyber physical system without actually implementing it to work which would make use of large amounts of time, equipment, money. So, the SysML library modeled by us in WebGME would be seen as an asset by all computer engineers that work on developing or implementing new Cyber Physical Systems or people who debug the designed Cyber Physical Systems.
 
 
#Project Dependencies:
 
 1. Open the project
 2. Start MongoDB 
 3. Start NPM
 3. Then start the local host server to connect to the server.
 4. Run the python Plugin that we have.
 5. The Step by Step transitions between states in the designed state machine diagrams would be outputted on the screen and resulting in understanding different states transitioned for different input conditions to the state diagram.

## Metamodeling
We defined the Meta Model with different elements that works as different states in a state machine diagram. We considered choice, fork, merge, state bases, compound states, initial state, final state, state machine, transition states. We designed different decorators to be used in the model we developed. These decorators are similar to those that will be used in SysML. The plugin was developed in such a way that it recongizes each state individually and shows transitions between states for various inputs. These various inputs can be different conditions in which the particular machine works. The guard condition can be either true or false. Depends on the condition satisfied, the flow of state machine works out.  The plugin generated is in python. As soon as the plugin is run, individual python files are generated resulting in state machine interpreter. 


