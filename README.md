### Description

A PyMongo backend hosted on your local computer with CRUD operations and a REST API.

### How to Use

Install python if not already installed.

Follow the steps below or this link: https://www.mongodb.com/languages/python/pymongo-tutorial

Run the following commands
```
python3 -m venv {project_name}
source {project_name}/bin/activate
```
That didn't work for me but I ran
```
py -m venv {project_name}
cd {project_name}
./Scripts/activate
```

Install required dependencies
`python -m pip install 'fastapi[all]' 'pymongo[srv]' python-decouple`

Create a .env file in the pymongo-fastapi-crud folder with
```
ATLAS_URI={Your Atlas connection string}
DB_NAME={Name of your DB in Atlas}
```

Run the program by using the command
```
py -m uvicorn pymongo-fastapi-crud.main:app --reload
```

If you go to http://127.0.0.1:8000/docs#/ you should see something.