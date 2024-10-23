# Feefo Python Reviews

## Overview
This repository contains Python scripts for fetching, processing, and exporting customer service and product reviews from the Feefo API. The scripts are designed to handle pagination, filter reviews from the last 7 days, and provide businesses with insights into customer feedback.

## Features
- **Service Reviews**
  - Fetches customer service reviews from the Feefo API.
  - Handles pagination to retrieve all available reviews.
  - Filters reviews from the last 7 days.
  - Exports results to a CSV file for easy analysis.
  - Processes data into a Pandas DataFrame for further manipulation.

|   merchant_identifier | customer_name       | customer_location | review                                               | service_rating | created_at                | products_purchased                               | url                                                 |
|-----------------------|---------------------|--------------------|-----------------------------------------------------|----------------|---------------------------|--------------------------------------------------|-----------------------------------------------------|
| ct-shirts-uk         | Mr Malkit Kaur      | Southall, London   | I bought 5 shirts, Nice fitting, good material...  | 5              | 2024-10-23 15:39:50 UTC   | SF Indigo Blue & Red Button-Down Collar Shirt... | https://www.feefo.com/en_GB/reviews/...            |
| ct-shirts-uk         | Ms Sarah Johnson     | Manchester         | Very helpful young lady that had to put up with... | 5              | 2024-10-23 16:08:05 UTC   | SF White Cutaway Collar Non-Iron Twill Shirt...  | https://www.feefo.com/en_GB/reviews/...            |
| ct-shirts-uk         | Mr James Smith      | Birmingham         | Excellent service and great quality shirts.        | 5              | 2024-10-23 15:29:46 UTC   | CF White Non-Iron Poplin Shirt                   | https://www.feefo.com/en_GB/reviews/...            |


- **Product Reviews**
  - Fetches product reviews from the Feefo API.
  - Handles pagination to retrieve all available reviews.
  - Filters reviews from the last 7 days.
  - Exports results to a CSV file for easy analysis.
  - Processes data into a Pandas DataFrame for further manipulation.

|   merchant_identifier | customer_name       | customer_location | review                              | product_title                                         | product_sku  | service_rating | created_at                | url                                                 |
|-----------------------|---------------------|--------------------|-------------------------------------|------------------------------------------------------|--------------|----------------|---------------------------|-----------------------------------------------------|
| ct-shirts-uk         | Ms Linda Brown      | London             | Lovely shirt                        | CF White Non-Iron Poplin Shirt                        | FON0004WHT   | 5              | 2024-10-23 15:30:31 UTC   | https://www.feefo.com/en_GB/reviews/...            |
| ct-shirts-uk         | Mr John Doe         | Liverpool          | Great fit and quality               | CF Cobalt Blue Button-Down Collar Non-Iron Stripe... | FOB0678COB   | 4              | 2024-10-23 15:35:12 UTC   | https://www.feefo.com/en_GB/reviews/...            |
| ct-shirts-uk         | Ms Alice Green      | Bristol            | Excellent service                   | SF Indigo Blue & Red Button-Down Collar Shirt        | FON0005IND   | 5              | 2024-10-23 15:40:50 UTC   | https://www.feefo.com/en_GB/reviews/...            |


## Requirements
- Python 3.x
- `requests` library
- `pandas` library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/feefo-python-reviews.git
