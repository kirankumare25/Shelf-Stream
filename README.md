# 🚀 FastAPI Client-Server Workflow Demonstration

This project demonstrates a typical **Client-Server architecture** using two separate FastAPI applications. This approach allows for clear separation of concerns, where one application handles the user interface (Client) and the other manages data processing and API logic (Server).

## 💡 Architecture Overview

| Component | Role | Technology | Port |
| :--- | :--- | :--- | :--- |
| **Client** (`client.py`) | Handles **rendering HTML templates** and user interactions. It sends requests to the Server API. | FastAPI & Jinja Templates | `8080` |
| **Server** (`server.py`) | Handles **API requests**, interacts with the data model (`model.py`), and returns data (e.g., JSON) to the Client. | FastAPI | `5000` |
| **Model** (`model.py`) | Contains the core logic, data manipulation, or placeholder for database interaction. | Python | N/A |

---

## 💻 Getting Started

Follow these steps to set up and run the client and server applications simultaneously.

### Prerequisites

You must have **Python** installed on your system. This project requires FastAPI and the Uvicorn ASGI server to run.

1.  **Install Dependencies:** Install the necessary packages, including FastAPI and Uvicorn.

    ```bash
    pip install fastapi uvicorn "python-multipart[standard]" jinja2
    ```
    *(Note: `jinja2` is often required for rendering HTML templates in FastAPI.)*

### Running the Applications

Since we are running two separate FastAPI applications, we need two separate terminals or command prompts.

#### Step 1: Start the Server Application

In your **first terminal**, navigate to the project directory and start the **Server** application on port **`5000`**.

```bash
uvicorn server:server --port 5000
```

The format is uvicorn <file_name>:<fastapi_instance_name>.

This application handles the backend API requests.


This sounds like a great demonstration of a microservices architecture using FastAPI!

Here is the README.md file you can use, incorporating all the setup and running instructions for your server/client workflow.

Markdown

# 🚀 FastAPI Client-Server Workflow Demonstration

This project demonstrates a typical **Client-Server architecture** using two separate FastAPI applications. This approach allows for clear separation of concerns, where one application handles the user interface (Client) and the other manages data processing and API logic (Server).

## 💡 Architecture Overview

| Component | Role | Technology | Port |
| :--- | :--- | :--- | :--- |
| **Client** (`client.py`) | Handles **rendering HTML templates** and user interactions. It sends requests to the Server API. | FastAPI & Jinja Templates | `8080` |
| **Server** (`server.py`) | Handles **API requests**, interacts with the data model (`model.py`), and returns data (e.g., JSON) to the Client. | FastAPI | `5000` |
| **Model** (`model.py`) | Contains the core logic, data manipulation, or placeholder for database interaction. | Python | N/A |

---

## 💻 Getting Started

Follow these steps to set up and run the client and server applications simultaneously.

### Prerequisites

You must have **Python** installed on your system. This project requires FastAPI and the Uvicorn ASGI server to run.

1.  **Install Dependencies:** Install the necessary packages, including FastAPI and Uvicorn.

    ```bash
    pip install fastapi uvicorn "python-multipart[standard]" jinja2
    ```
    *(Note: `jinja2` is often required for rendering HTML templates in FastAPI.)*

### Running the Applications

Since we are running two separate FastAPI applications, we need two separate terminals or command prompts.

#### Step 1: Start the Server Application

In your **first terminal**, navigate to the project directory and start the **Server** application on port **`5000`**.

```bash
uvicorn server:server --port 5000
```
The format is uvicorn <file_name>:<fastapi_instance_name>.

This application handles the backend API requests.

#### Step 2: Start the Client Application
In your second terminal, navigate to the project directory and start the Client application on port 8080.

```bash

uvicorn client:app --port 8080
```
This application handles the frontend templates and makes requests to the backend server running on port 5000


#### Accessing the Application
Once both terminals show that the applications are running, you can access the frontend Client application in your web browser at:

```bash
[http://127.0.0.1:8080](http://127.0.0.1:8080)
```
The Client will then automatically communicate with the Server running on port 5000 to fetch data.
