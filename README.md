# Project Name

Description of the project. Provide a brief overview of what the project is about.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

Follow these steps to set up and run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/RemigiuszZydek/apiNBP.git
```
### 2. Navigate to the project directory
```bash
 cd /apiNBP
```
### 3. Build the database
```bash
docker-compose up db --build
```
### 4. Build the backend
```bash
docker-compose up backend --build
```
### 5. Build the frontend
```bash
docker-compose up frontend --build
```
### 6. Apply database migrations
Open a new terminal and navigate to the backend container:
```bash
docker-compose exec backend bash
```
In the bash terminal, run the following command:
```bash
python manage.py migrate
```
### 7. Access the application
Open your browser and navigate to:
```bash
http://localhost:4200
```
