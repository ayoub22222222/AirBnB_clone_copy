#  AirBnB clone 
## **The console**
![Alt text](<hbnb proejct-1.PNG>)

# Description :file_folder:

 


HBnB is a complete web application, integrating database storage, a back-end API, and front-end interface in a clone of AirBnB.

This team project is part of the [ALX](https://www.alxafrica.com/)
 Software Engineering program.
It represents the first step towards building a full web application.

This first step consists of:

a custom command-line interface for data management, and the base classes for the storage of this data.

# Environment 

Our project is built and tested on Ubuntu 20.04 LTS using python3 (version 3.8.5)

# Installation 
1.  Clone this repository:  **<mark> git clone "https://github.com/ayoub22222222/AirBnB_clone"</mark>**
2. Access AirBnb directory: **<mark> cd AirBnB_clone </mark>**
3. Run hbnb (interactively):  **<mark> ./console </mark>** and enter command
4. Run hbnb (non-interactively) : **<mark> echo "<command>"| ./console.py </mark>**

# File descriptions

[console.py]() - the console contains the entry point of the command interpreter. List of commands this console current supports:

+  **EOF** - exits console
+  **quit** - exits console
+ < **emptyline** > - overwrites default emptyline method and does nothing
+ **create** - Creates a new instance ofBaseModel, saves it (to the JSON file) and prints the id
+ **destroy** - Deletes an instance based on the class name and id (save the change into the JSON file).
+ **show** - Prints the string representation of an instance based on the class name and id.
+ **all** - Prints all string representation of all instances based or not on the class name.
+ **update** - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).


