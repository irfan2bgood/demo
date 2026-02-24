import boto3
import pandas as pd
from io import StringIO

# Assume df already exists (your flight dataset)

bucket_name = "your-bucket-name"
s3_key = "flight-data/synthetic_flight_data.csv"

# Convert dataframe to CSV in memory
csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)

# Create S3 client
s3 = boto3.client("s3")

# Upload
s3.put_object(
    Bucket=bucket_name,
    Key=s3_key,
    Body=csv_buffer.getvalue()
)

print(f"Uploaded to s3://{bucket_name}/{s3_key}")