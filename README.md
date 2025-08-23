# SQL-Based Incident Analysis with GenAI Reporting

Automates root cause analysis on a MySQL incident database and generates AI-powered summaries using OpenAI. Containerized with Docker and scheduled via cron for automated daily reporting.

## Key Features
- Detects recurring error patterns in production incidents
- Generates human-readable summaries and recommendations
- Fully containerized for consistent deployment
- Scheduled cron job for automated execution

## Tech Stack
- **Python**: Data fetching, processing, and API integration
- **MySQL**: Incident database
- **Docker**: Containerization
- **OpenAI API**: AI-generated summaries
- **Pandas**: Data handling

## Quick Start
git clone https://github.com/VeeraReddyRavuri/SQL-GenAI-Incident-Analysis.git
cd SQL-GenAI-Incident-Analysis
docker build -t incident-analysis .
docker run --rm --network="host" incident-analysis

