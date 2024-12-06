# Spy Cat Agency API

## Overview
The Spy Cat Agency API is a Django-based CRUD application designed for managing spy cats, their missions, and assigned targets. It provides endpoints to manage cats, create and update missions, and validate breeds through TheCatAPI.

---

## Features
- Manage Spy Cats:
  - Create, read, update, and delete spy cats.
  - Validate cat breeds via TheCatAPI.
- Manage Missions:
  - Create missions with associated targets.
  - Update and delete missions (with restrictions).
  - Automatically mark missions as complete when all targets are completed.
- Manage Targets:
  - Update notes for targets.
  - Mark targets as complete (and freeze notes when done).

---

## Installation and Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- SQLite (pre-configured, no additional setup required)

### Steps to Run
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/spy-cat-agency.git
   cd spy-cat-agency
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and go to `http://127.0.0.1:8000/api/`.

---

## API Endpoints

### Spy Cats
- **GET** `/api/spycats/` - Retrieve all spy cats.
- **GET** `/api/spycats/{id}/` - Retrieve a specific spy cat.
- **POST** `/api/spycats/` - Create a new spy cat.
  - **Body**:
    ```json
    {
        "name": "Shadow",
        "years_of_experience": 5,
        "breed": "Abyssinian",
        "salary": "5000.00"
    }
    ```
- **PUT** `/api/spycats/{id}/` - Update an existing spy cat.
- **DELETE** `/api/spycats/{id}/` - Delete a spy cat.

### Missions
- **GET** `/api/missions/` - Retrieve all missions.
- **GET** `/api/missions/{id}/` - Retrieve a specific mission.
- **POST** `/api/missions/` - Create a new mission.
  - **Body**:
    ```json
    {
        "cat": 1,
        "complete": false,
        "targets": [
            { "name": "Target A", "country": "USA", "notes": "Observe movements.", "complete": false },
            { "name": "Target B", "country": "UK", "notes": "Collect data.", "complete": false }
        ]
    }
    ```
- **PUT** `/api/missions/{id}/` - Update an existing mission.
- **DELETE** `/api/missions/{id}/` - Delete a mission (if not assigned to a cat).

### Targets
- **GET** `/api/targets/` - Retrieve all targets.
- **GET** `/api/targets/{id}/` - Retrieve a specific target.
- **PATCH** `/api/targets/{id}/` - Update notes or mark as complete.
  - **Body**:
    ```json
    { "notes": "Updated notes." }
    ```

---

## TheCatAPI Integration
- The application fetches a list of valid cat breeds from TheCatAPI (`https://api.thecatapi.com/v1/breeds`) to validate breeds during spy cat creation or updates.
- If the breed is invalid, the API returns a validation error.

---

## Notes
- Missions cannot be deleted if assigned to a cat.
- Notes for targets cannot be updated if the target or its mission is completed.
- The database uses SQLite by default, but it can be configured to use PostgreSQL or MySQL if needed.

