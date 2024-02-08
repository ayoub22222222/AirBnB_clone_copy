#  AirBnB clone 
## **The console**
![Alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240208%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240208T234023Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a5aed6d9e0b34ba7bd44a9f30f09b0517d274d14d1a76de7b3027c703b2cc939)

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

+  `EOF` - exits console
+  `quit` - exits console
+ < emptyline > - overwrites default emptyline method and does nothing
+ `create`- Creates a new instance ofBaseModel, saves it (to the JSON file) and prints the id
+ `destroy `- Deletes an instance based on the class name and id (save the change into the JSON file).
+ `show `- Prints the string representation of an instance based on the class name and id.
+ `all` - Prints all string representation of all instances based or not on the class name.
+ `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

`models/` directory contains classes used for this project:

[base_model.py]() - The BaseModel class from which future classes will be derived

+ `def __init__(self, *args, **kwargs)` - Initialization of the base model
+ `def __str__(self)` - String representation of the BaseModel class
+ `def save(self)` - Updates the attribute updated_at with the current datetime
+ `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

