# kaggle-etl

Use loan data from a kaggle project and develop a highly automated ETL.  This project is meant to be a significant improvement over the data challenge version.

## Flow
Download loan data.
Upload to S3 bucket.
Parse loan data to dynamically generate database tables to store the data


## Scraper / Automate the download from Kaggle
- credentials page uses javascript and XSRF protection, so we need to read the page to get the token first
- selenium can be used to handle the javascript interpretation
- pycurl can then retrieve the cookies
- beautiful soup can be used for parsing, but might not be needed.
- download the data directly and/or send it to the S3 bucket directly

## Parse Zipped Loan Data for Metadata
- store metadata from the lcdictionary.
- use metadata from the zipped loan data to create tables dynamically.
