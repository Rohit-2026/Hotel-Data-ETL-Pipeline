import requests
import csv
import json
LOCATION_KEY = 'g662323'  # Replace with your actual location key if needed
LIMIT = 100  # Number of hotels to retrieve (max 100)
OFFSET = 0   # Adjust offset if needed
SORT_BY = 'best_value'  # Options: best_value, popularity, distance
# API Endpoint
BASE_URL = 'https://data.xotelo.com/api/list'
params = {
    'location_key': LOCATION_KEY,
    'limit': LIMIT,
    'offset': OFFSET,
    'sort': SORT_BY
}
try:
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    if data.get('error'):
        raise Exception(f"API Error: {data['error']}")
    hotels = data.get('result', {}).get('list', [])
    if not hotels:
        print("No hotel data found.")
    else:
        # Define CSV file name
        csv_file = 'hotels_list_N.csv'
        header = [
            'name','key','accommodation_type','url','review_rating','review_count','price_maximum','price_minimum','geo_latitude','geo_longitude','highlighted_amenities'
        ]
        # Write hotel details to CSV
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for hotel in hotels:
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
                writer.writerow(row)
        print(f"Data successfully written to {csv_file}")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except ValueError as e:
    print(f"JSON decode error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")






