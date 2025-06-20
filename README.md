Hotel Data ETL Pipeline

A modular Python ETL pipeline that fetches hotel listings from a REST API, transforms nested JSON data into a consistent schema, and loads records into MongoDB for efficient querying.

Features

Extract: Parameterized API calls (limit, offset, sort) using requests to retrieve up to 100 hotel records per run.

Transform: Normalizes nested fields, handles missing data gracefully, and constructs clean document structures.

Load: Inserts documents into MongoDB via pymongo, with indexed fields (review_rating, price_minimum) for sub-second query performance.

Reliability: Implements basic logging and retry logic for idempotent, repeatable runs.

Extensible: Packaged as a standalone script ready for orchestration (Airflow/Prefect).

Technologies & Tools

Python 3.x

requests, json, pymongo

MongoDB (local or Atlas)

GitHub (repository & CI)

Project Structure

├── extract.py           # Contains ETL functions and main runner
├── README.md            # Project documentation
└── requirements.txt     # Dependencies list

Prerequisites

Python 3.7+

MongoDB instance (URI in MONGO_URI)

API access (no auth required)

Installation

Clone the repo:

git clone https://github.com/your-username/hotel-etl.git
cd hotel-etl

Install dependencies:

pip install -r requirements.txt

Configure MONGO_URI, DB_NAME and COLLECTION_NAME in extract.py.

Usage

python extract.py

On success, you will see: Inserted X documents into 'hotel_data.hotels'.
