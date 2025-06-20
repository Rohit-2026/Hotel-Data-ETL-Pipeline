import requests
import csv
import json

LOCATION_KEY = 'g662323'
LIMIT = 100
OFFSET = 0
SORT_BY = 'best_value'
BASE_URL = 'https://data.xotelo.com/api/list'
CSV_FILE = 'hotels_list_N.csv'
HEADER = [
    'name','key','accommodation_type','url',
    'review_rating','review_count',
    'price_maximum','price_minimum',
    'geo_latitude','geo_longitude',
    'highlighted_amenities'
]


def extract(params):
    """
    Extract data from the API
    """
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get('result', {}).get('list', [])


def transform(raw_hotels):
    """
    Transform raw JSON into a list of rows for CSV or DB
    """
    transformed = []
    for hotel in raw_hotels:
        row = [
            hotel.get('name', 'N/A'),
            hotel.get('key', 'N/A'),
            hotel.get('accommodation_type', 'N/A'),
            hotel.get('url', 'N/A'),
            hotel.get('review_summary', {}).get('rating', 'N/A'),
            hotel.get('review_summary', {}).get('count', 'N/A'),
            hotel.get('price_ranges', {}).get('maximum', 'N/A') if hotel.get('price_ranges') else 'N/A',
            hotel.get('price_ranges', {}).get('minimum', 'N/A') if hotel.get('price_ranges') else 'N/A',
            hotel.get('geo', {}).get('latitude', 'N/A'),
            hotel.get('geo', {}).get('longitude', 'N/A'),
            ", ".join([amenity.get('name', '') for amenity in hotel.get('highlighted_amenities', [])])
        ]
        transformed.append(row)
    return transformed


def load(rows, csv_file, header):
    """
    Load the transformed data into a CSV file
    """
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)


def main():
    params = {
        'location_key': LOCATION_KEY,
        'limit': LIMIT,
        'offset': OFFSET,
        'sort': SORT_BY
    }
    raw_data = extract(params)
    if not raw_data:
        print("No hotel data found.")
        return

    rows = transform(raw_data)
    load(rows, CSV_FILE, HEADER)
    print(f"Data successfully written to {CSV_FILE}")


if __name__ == '__main__':
    main()
