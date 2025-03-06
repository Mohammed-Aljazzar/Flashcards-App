# Flashcards App

![Python](https://img.shields.io/badge/Python-3.13-blue) ![Django](https://img.shields.io/badge/Django-5.1.6-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

A simple web-based flashcard application built with Django to help users study and review topics using a spaced repetition system (inspired by the Leitner system). Users can create, update, and review flashcards organized into numbered boxes, with the ability to move cards between boxes based on whether they answer correctly.

## Features
- Create flashcards with questions, answers, and box numbers (1 to 5).
- View all flashcards or filter by box number.
- Check a random card from a specific box and move it based on whether the answer was correct.
- Update existing flashcards.
- Track card creation dates and organize them by box and recency.
- Simple navigation with links to each box showing the number of cards.

## Tech Stack
- **Backend**: Python 3.13, Django 5.1.6
- **Database**: SQLite (default, can be configured for others)
- **Frontend**: Django templates (HTML)
- **Dependencies**: Managed via `pip` in a virtual environment

## Installation

### Prerequisites
- Python 3.13 installed ([Download Python](https://www.python.org/downloads/))
- Git installed ([Download Git](https://git-scm.com/downloads))

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/flashcards-app.git
   cd flashcards-app
   ```
2. **Set Up a Virtual Environment**
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```
3. **Install Dependencies**
  ```bash
  pip install django==5.1.6
  ```
4. **Apply Migrations**
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
5. **Run the Development Server**
  ```bash
  python manage.py runserver
  ```
  Open your browser and go to http://127.0.0.1:8000/.








