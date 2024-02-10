#  AirBnB clone 
## **The console**
![alt text](<hbnb proejct.PNG>)

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
4. Run hbnb (non-interactively) :  echo "`<command>`"| ./console.py 

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

Classes inherited from Base Model:

+ **amenity.py**
+ **city.py**
+ **place.py**
+ **review.py**
+ **state.py**
+ **user.py**

`/models/engine` directory contains File Storage class that handles JASON serialization and deserialization :

**file_storage.py** - serializes instances to a JSON file & deserializes back to instances

+ `def all(self)` - returns the dictionary __objects
+ `def new(self, obj)` - sets in __objects the obj with key .id
+ `def save(self)` - serializes __objects to the JSON file (path: __file_path)
 + `def reload(self)` - deserializes the JSON file to __objects

