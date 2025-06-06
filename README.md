# PROG8850Week1Installation
install mysql, python

```bash
ansible-playbook up.yml
```

To use mysql:

```bash
mysql -u root -h 127.0.0.1 -p
```

To run github actions like (notice that the environment variables default for the local case):

```yaml
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Install MySQL client
        run: sudo apt-get update && sudo apt-get install -y mysql-client

      - name: Deploy to Database
        env:
          DB_HOST: ${{ secrets.DB_HOST || '127.0.0.1' }} 
          DB_USER: ${{ secrets.DB_ADMIN_USER || 'root' }}
          DB_PASSWORD: ${{ secrets.DB_PASSWORD  || 'Secret5555'}}
          DB_NAME: ${{ secrets.DB_NAME || 'mysql' }}
        run: mysql -h $DB_HOST -u $DB_USER -p$DB_PASSWORD $DB_NAME < schema_changes.sql
```

locally:

first try

```bash
bin/act
```

then if that doesn't work 

```bash
bin/act -P ubuntu-latest=-self-hosted
```

to run in the codespace.

To shut down:

```bash
ansible-playbook down.yml
```

This is a reproducible mysql setup

# PROG8850 MySQL Automation Project

This project provides a reproducible MySQL environment with automated schema management using Python and GitHub Actions.

## Features

- Automated MySQL setup using Ansible and Docker (for Codespaces or local Linux)
- SQL schema management via `schema_changes.sql`
- Python script (`run_sql_script.py`) to execute SQL scripts using `mysql-connector-python`
- GitHub Actions workflow to test schema changes on every push to `main`

---

## Prerequisites

- [Python 3.8+](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)
- [MySQL Server](https://dev.mysql.com/downloads/mysql/) (for local testing)
- [Ansible](https://docs.ansible.com/) (for provisioning)
- [Docker](https://www.docker.com/) (optional, for Codespaces or containerized MySQL)
- [act](https://github.com/nektos/act) (optional, to run GitHub Actions locally)

---

## Setup

### 1. Provision MySQL and Python

Run the Ansible playbook to set up MySQL and Python:

```bash
ansible-playbook up.yml
```

### 2. Connect to MySQL

```bash
mysql -u root -h 127.0.0.1 -p
```

---

## Running the SQL Script

### Using Python

Install dependencies:

```bash
pip install mysql-connector-python
```

Run the script:

```bash
python run_sql_script.py
```

This will execute all commands in `schema_changes.sql` and commit changes to the database.

---

## GitHub Actions Workflow

A workflow is provided in `.github/workflows/mysql_action.yml`:

- **Triggers:** On every push to the `main` branch
- **What it does:**
  - Sets up a MySQL service in a container
  - Installs Python and dependencies
  - Runs `run_sql_script.py` to apply schema changes

**To check workflow status:**
1. Push your changes to `main`.
2. Go to the "Actions" tab in your GitHub repository.
3. Click on the latest workflow run to see logs and results.

---

## Running GitHub Actions Locally

You can use [`act`](https://github.com/nektos/act) to simulate GitHub Actions:

```bash
bin/act
```

If you encounter issues, try:

```bash
bin/act -P ubuntu-latest=-self-hosted
```

---

## Shutting Down

To tear down the environment:

```bash
ansible-playbook down.yml
```

---

## Project Structure

```
.
├── README.md
├── schema_changes.sql         # SQL schema changes
├── run_sql_script.py         # Python script to execute SQL
├── up.yml / down.yml         # Ansible playbooks
└── .github/
    └── workflows/
        └── mysql_action.yml  # GitHub Actions workflow
```

---

## Notes

- The workflow and scripts use the following MySQL credentials by default:
  - **Host:** 127.0.0.1
  - **User:** root
  - **Password:** Secret5555
  - **Database:** test

- You can change these in the workflow file or Python script as needed.

---

## License

MIT License

---

## Author

Akintunde
