import requests
import pandas as pd
import json
from datetime import datetime
import time

def _get_merchant_reviews(merchant_identifier, since_period='week', max_retries=3):
    all_reviews = []
    page = 1

    while True:
        try:
            # Construct the URL for the current page (no displayFeedbackType parameter)
            response = requests.get(
                f"https://api.feefo.com/api/10/reviews/all?page_size=100&merchant_identifier={merchant_identifier}&since_period={since_period}&page={page}",
                timeout=10
            )
            
            # Check if the request was successful
            if response.status_code == 200:
                results = json.loads(response.text)
                
                # Extract reviews from the current page
                reviews = results.get('reviews', [])
                all_reviews.extend(reviews)

                # Check if we have more pages
                total_pages = _count_pages(results)
                if page >= total_pages:
                    break
                
                page += 1
            
            elif response.status_code == 504:
                print("Server timeout, retrying...")
                max_retries -= 1
                if max_retries <= 0:
                    print("Max retries reached. Exiting.")
                    break
                time.sleep(2)  # wait before retrying
            else:
                print(f"Failed to retrieve reviews: {response.status_code}, {response.text}")
                break

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break

    # Debugging print to check total reviews fetched
    print(f"Total Reviews Fetched: {len(all_reviews)}")
    
    return all_reviews

def get_merchant_reviews(merchant_identifier, since_period='week'):
    reviews = _get_merchant_reviews(merchant_identifier, since_period)
    
    if not reviews:
        print("No reviews found.")
        return pd.DataFrame()

    # Create a list to hold rows
    rows = []
    
    for review in reviews:
        row = {
            'merchant_identifier': review.get('merchant', {}).get('identifier'),
            'customer': review.get('customer', {}).get('display_name', {}),
            'created_at': review.get('service', {}).get('created_at', {}),
            'review': review.get('service', {}).get('review', {}),
            'service_rating': review.get('service', {}).get('rating', {}).get('rating', None)
        }
        rows.append(row)

    # Create the DataFrame after collecting rows
    df = pd.DataFrame(rows)

    # Handle missing service_rating values before converting to int
    df['service_rating'] = pd.to_numeric(df['service_rating'], errors='coerce').fillna(0).astype(int)

    df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
    df['type'] = "Service Reviews"

    # Create unique ID to identify rows
    df['id'] = df["customer"].astype(str) + df['created_at'].astype(str) + df['service_rating'].astype(str) + df['review'].astype(str)

    # Drop duplicates based on the unique ID
    df = df.drop_duplicates(subset='id', keep='last')

    # Print final DataFrame to check results
    print(df)
    
    # Export the DataFrame to a CSV file
    csv_filename = f"merchant_reviews_{merchant_identifier}_{since_period}.csv"
    df.to_csv(csv_filename, index=False)
    print(f"Data exported to {csv_filename}")
    
    return df

# Call the function to fetch reviews and export to CSV
get_merchant_reviews('ct-shirts-uk', 'week')
