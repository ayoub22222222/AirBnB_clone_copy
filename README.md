#  AirBnB clone 
## **The console**
![hbnb proejct](https://github.com/Zinebb12/Own_tests/assets/141257110/c31ad1cd-ab29-4554-a81f-a1c04ecb2c67)

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
2.  Access AirBnb directory:  cd `AirBnB_clone` 
3.  Run hbnb (interactively):  **<mark> `./console `</mark>** and enter command
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

 `/tests` directory contains all unit test cases for this project : 


  * **/test_models/test_base_model.py**- Contains the TestBaseModel and TestBaseModelDocs classes TestBaseModelDocs class

* **/test_models/test_amenity.py** - Contains the TestAmenityDocs class 
* **/test_models/test_city.py** - Contains the TestCityDocs class 
* **/test_models/test_file_storage.py** - Contains the TestFileStorageDocs class 
* **/test_models/test_place.py** - Contains the TestPlaceDoc class


# Execustion 
### In interactive mode
```python
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit

```

###  In non-interactive mode

```python
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

# Authors
[Mohammed Ayoub ESSBAI](https://github.com/ayoub22222222) 

[Zineb ZID ](https://github.com/Zinebb12)

# Licence 

No copyright protection . 
