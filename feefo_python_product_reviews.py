import pandas as pd
import requests
from datetime import datetime, timedelta

# Function to fetch data from the API with pagination
def fetch_reviews(merchant_identifier, days=7):
    reviews = []
    url_template = f"https://api.feefo.com/api/10/reviews/all?page_size=100&merchant_identifier={merchant_identifier}&page={{}}"

    # Calculate the date range for the last 'days' days
    date_threshold = datetime.now() - timedelta(days=days)
    
    page = 1
    while True:
        url = url_template.format(page)
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            # Check if there are reviews
            if 'reviews' not in data:
                break

            # Filter reviews by date
            for review in data['reviews']:
                service = review.get('service', {})
                if 'created_at' in service:
                    review_date = datetime.fromisoformat(service['created_at'][:-1])  # Remove 'Z' for isoformat
                    if review_date >= date_threshold:
                        reviews.append(review)
                    else:
                        # If the review date is older than the threshold, exit the loop
                        break

            # If there are no more pages, exit the loop
            if len(data['reviews']) < 100:  # Less than page size means no more pages
                break

            page += 1  # Go to the next page
        else:
            print(f"Error fetching data: {response.status_code}")
            break

    return reviews

# Function to process the fetched data and create a DataFrame
def process_reviews(reviews):
    reviews_list = []
    
    for review in reviews:
        # Use get to safely access keys
        merchant = review.get('merchant', {})
        customer = review.get('customer', {})
        service = review.get('service', {})
        
        review_data = {
            'merchant_identifier': merchant.get('identifier', 'N/A'),  # Default to 'N/A' if not available
            'customer_name': customer.get('display_name', 'N/A'),  # Default to 'N/A' if not available
            'customer_location': customer.get('display_location', 'N/A'),  # Default to 'N/A' if not available
            'review': service.get('review', 'N/A'),  # Default to 'N/A' if not available
            'service_rating': service.get('rating', {}).get('rating', 'N/A'),  # Default to 'N/A' if not available
            'created_at': service.get('created_at', 'N/A'),  # Default to 'N/A' if not available
            'products_purchased': ', '.join(review.get('products_purchased', [])),
            'url': review.get('url', 'N/A')  # Default to 'N/A' if not available
        }
        reviews_list.append(review_data)

    # Create DataFrame
    df = pd.DataFrame(reviews_list)
    return df

# Main function to execute the script
def main():
    merchant_identifier = 'ct-shirts-uk'  # Your merchant identifier
    reviews = fetch_reviews(merchant_identifier, days=7)

    if reviews:
        df = process_reviews(reviews)
        
        # Print the DataFrame
        print("DataFrame of Reviews from the last 7 days:")
        print(df)

        # Save to CSV
        csv_filename = f"merchant_product_reviews_{merchant_identifier}_last_7_days.csv"
        df.to_csv(csv_filename, index=False)
        print(f"Data exported to {csv_filename}")
    else:
        print("No reviews found for the last 7 days.")

# Run the script
if __name__ == "__main__":
    main()
