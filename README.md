# Django Todo Checklist App

A simple Todo checklist application built with Python and Django, using `uv` for dependency management.

## Features
- Create, edit, and delete Todo items.
- Assign due dates with a date picker.
- Mark items as resolved/unresolved.
- Responsive design.

## Setup

### Prerequisites
- Python 3.14+
- `uv` package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd antigravity-django-todo-checklist-hw1
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Apply migrations:**
   ```bash
   uv run python manage.py migrate
   ```

## Usage

1. **Start the development server:**
   ```bash
   uv run python manage.py runserver
   ```

2. **Access the application:**
   Open your browser and navigate to `http://127.0.0.1:8000/`.

## Testing & Verification

### Automated Tests
Run the test suite to verify functionality:
```bash
uv run python manage.py test todo_app
```

### Manual Verification
1. **Create Todo**: Click "Add New Todo", fill in the title, description, and select a due date. Click "Save".
2. **Edit Todo**: Click "Edit" on an existing item, modify details, and save.
3. **Resolve**: Click "Resolve" to toggle the completion status.
4. **Delete**: Click "Delete", then confirm the deletion.
