# Project Name\n\nDescription of the project. Provide a brief overview of what the project is about.\n\n## Prerequisites\n\n- Docker\n- Docker Compose\n\n## Getting Started\n\nFollow these steps to set up and run the project locally.\n\n### 1. Clone the repository\n\n```bash\ngit clone <link>\n```\n\n### 2. Navigate to the project directory\n\n```bash\ncd apiNBP\n```\n\n### 3. Build the database\n\n```bash\ndocker-compose up db --build\n```\n\n### 4. Build the backend\n\n```bash\ndocker-compose up backend --build\n```\n\n### 5. Build the frontend\n\n```bash\ndocker-compose up frontend --build\n```\n\n### 6. Apply database migrations\n\nOpen a new terminal and navigate to the backend container:\n\n```bash\ndocker-compose exec backend bash\n```\n\nIn the bash terminal, run the following command:\n\n```bash\npython manage.py migrate\n```\n\n### 7. Access the application\n\nOpen your browser and navigate to:\n\n```\nhttp://localhost:4200\n```\n\n## Contributing\n\nPlease read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.\n\n## License\n\nThis project is licensed under the MIT License - see the `LICENSE.md` file for details.\n\n## Acknowledgments\n\n- Hat tip to anyone whose code was used\n- Inspiration\n- etc.\n\n---
