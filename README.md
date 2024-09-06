# Simple Note-Taking API

This is a RESTful API for a simple note-taking application built with Django.

## Features
- Create notes
- Fetch notes by ID
- Query notes by title substring
- Update notes

## Installation

1. Clone the repository:
```bash
   git clone https://github.com/your-username/your-repo-name.git
 ```
2. Navigate to the project directory:
```bash
cd your-repo-name
```
3. Create and activate a virtual environment:
```bash
    python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
4. Install the required packages:
```bash
pip install -r requirements.txt
```
5. Run migrations:
```bash
python manage.py migrate
```
6. Start the development server:
```bash
python manage.py runserver
```
## Usage
- POST /notes: Create a new note
- GET /notes?title=<substring>: Query notes by title
- GET /notes/<id>/: Fetch a note by ID
- PUT /notes/<id>/: Update a note by ID
- PATCH /notes/<id>/: Partially update a note by ID

