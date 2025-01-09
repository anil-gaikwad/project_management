# Multi-Tenant Company and Employee Management System

This project is a multi-tenant backend API for managing companies and their employees, as well as projects. It includes features for admin management, employee management, project management, real-time communication, and a front-end UI. The backend is built using FastAPI and MongoDB.

## Requirements

- Python 3.9+
- Docker
- Docker Compose
- MongoDB

## Features

- **Overall Admin Management**
  - Add and remove companies
- **Employee Management**
  - Admin of the company can invite, add, and remove employees
  - Employees can edit their own profile and update their details
- **Project Management**
  - Employees can create, edit, and delete projects
  - Employees can post comments on the project, and other users should get updates and respond in real-time

## Setup

### Backend

1. **Install Python dependencies:**
    ```sh
    cd backend
    pip install -r requirements.txt
    ```

2. **Start FastAPI server:**
    ```sh
    uvicorn app.main:app --reload
    ```

### Docker

1. **Build and start the containers:**
    ```sh
    docker-compose up --build
    ```

2. **Access the application:**
    - Backend: http://localhost:3000 (default FastAPI port)


## Deployment

### Docker

1. **Build and start the containers in detached mode:**
    ```sh
    docker-compose up --build -d
    ```

2. **Stop the containers:**
    ```sh
    docker-compose down
    ```

## Project Structure

### Backend

- `app/`: FastAPI application directory
  - `main.py`: Entry point for the FastAPI application
  - `models/`: Pydantic models and database schemas
  - `routes/`: API route definitions
  - `usecase/`: Business logic
  - `services/`: services
  - `utils/`: Utility functions and helpers

