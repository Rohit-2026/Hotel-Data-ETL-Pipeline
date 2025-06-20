# Hotel Data ETL Pipeline

A modular Python ETL pipeline that fetches hotel listings from a REST API, transforms nested JSON data into a consistent schema, and loads records into MongoDB for efficient querying.

## Features
- **Extract**: Parameterized API calls (`limit`, `offset`, `sort`) using `requests` to retrieve up to 100 hotel records per run.
- **Transform**: Normalizes nested fields, handles missing data gracefully, and constructs clean document structures.
- **Load**: Inserts documents into MongoDB via `pymongo`, with indexed fields (`review_rating`, `price_minimum`) for sub-second query performance.
- **Reliability**: Implements basic logging and retry logic for idempotent, repeatable runs.
- **Extensible**: Packaged as a standalone script ready for orchestration (Airflow/Prefect).

## Technologies & Tools
- Python 3.x
- `requests`, `json`, `pymongo`
- MongoDB (local or Atlas)
- GitHub (repository & CI)

## Project Structure
├── extract.py # Contains ETL functions and main runner
├── README.md # Project documentation
└── requirements.txt # Dependencies list

markdown
Copy
Edit

## Prerequisites
- Python 3.7+
- MongoDB instance (URI in `MONGO_URI`)
- API access (no auth required)

## Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/hotel-etl.git
   cd hotel-etl
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Configure MONGO_URI, DB_NAME and COLLECTION_NAME in extract.py.

Usage
bash
Copy
Edit
python extract.py
On success, you will see:

csharp
Copy
Edit
Inserted X documents into 'hotel_data.hotels'
Resume Snippet
pgsql
Copy
Edit
Hotel Data ETL Pipeline
• Built parameterized Python ETL (requests, JSON) ingesting ~100 hotel listings per run from a REST API
• Designed transform logic to normalize nested fields and gracefully handle missing data
• Loaded cleansed records into MongoDB via PyMongo with indexed review_rating and price_minimum
• Implemented idempotent runs with basic logging and retry logic for pipeline reliability
• Packaged as a standalone script ready for orchestration (Airflow/Prefect)
Future Improvements
Integrate with Airflow DAG for scheduled runs

Add unit tests (pytest) for transform logic

Extend load to support CSV/SQL sinks

Enhance logging (structured logs, monitoring)
