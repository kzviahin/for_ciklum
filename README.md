ELEVATOR MANAGEMENT SYSTEM

This is small model of elevator management system. System works just in scope of calling lifts from floor to floor.
You can interact with a system pressing buttons on different floors. 

Elevator class responsible for using elevator object itself, move it, stop etc.

Button class responsible for button object and it's behaviour. So it has state of button and some methods to interact with it.

ElevatorsSystem class is a management system itself. In class constructor initialized two lists with elevators and buttons.
Also in this class represent mechanism of choosing elevator and adding stops to it's list

Test was written with using pytest

Use --smoke to run only two of them