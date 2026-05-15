# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using the FastAPI framework, including defining request models, creating endpoints, and validating input data.

## 📝 Tasks

### 🛠️ Create a FastAPI application

#### Description
Create the main FastAPI app and add a root endpoint plus an initial `/items/` endpoint that returns example data.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance
- Add a root (`/`) GET endpoint that returns a welcome message
- Add a `/items/` GET endpoint that returns a list of example items
- Use JSON output for all endpoint responses

### 🛠️ Add data validation with Pydantic

#### Description
Define a Pydantic model for item data and add a POST endpoint that accepts new items.

#### Requirements
Completed program should:

- Define an `Item` model using `pydantic.BaseModel`
- Accept POST requests at `/items/` with JSON body matching the `Item` model
- Return the created item in the response
- Validate required fields and data types automatically

### 🛠️ Build a complete CRUD workflow

#### Description
Extend the API with read, update, and delete operations for item data.

#### Requirements
Completed program should:

- Add a GET endpoint at `/items/{item_id}` to return a specific item
- Add a PUT endpoint at `/items/{item_id}` to update an item using the `Item` model
- Add a DELETE endpoint at `/items/{item_id}` to remove an item
- Use appropriate path parameters and return meaningful JSON responses
