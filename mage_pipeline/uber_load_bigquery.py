from google.cloud import bigquery
import pandas as pd
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_exporter
def export_data_to_bigquery(data, **kwargs) -> None:
    """
    Export data to BigQuery
    """
    # Configuration
    project_id = kwargs['PROJECT_ID']  # Pass this as a runtime variable
    dataset_id = 'uber_data_dataset'
    
    # Initialize BigQuery client
    client = bigquery.Client(project=project_id)
    
    # Create dataset if it doesn't exist
    dataset_ref = client.dataset(dataset_id)
    try:
        client.get_dataset(dataset_ref)
        print(f"Dataset {dataset_id} already exists")
    except Exception:
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = "US"  # Set your preferred location
        client.create_dataset(dataset)
        print(f"Created dataset {dataset_id}")
    
    # Define table schemas
    schemas = {
        'datetime_dim': [
            bigquery.SchemaField("datetime_id", "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("pick_hour", "INTEGER"),
            bigquery.SchemaField("pick_day", "INTEGER"),
            bigquery.SchemaField("pick_month", "INTEGER"),
            bigquery.SchemaField("pick_year", "INTEGER"),
            bigquery.SchemaField("pick_weekday", "INTEGER"),
            bigquery.SchemaField("drop_hour", "INTEGER"),
            bigquery.SchemaField("drop_day", "INTEGER"),
            bigquery.SchemaField("drop_month", "INTEGER"),
            bigquery.SchemaField("drop_year", "INTEGER"),
            bigquery.SchemaField("drop_weekday", "INTEGER")
        ],
        'passenger_count_dim': [
            bigquery.SchemaField("passenger_count_id", "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("passenger_count", "INTEGER")
        ],
        'trip_distance_dim': [
            bigquery.SchemaField("trip_distance_id", "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("trip_distance", "FLOAT")
        ],
        'rate_code_dim': [
            bigquery.SchemaField("rate_code_id", "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("RatecodeID", "INTEGER"),
            bigquery.SchemaField("rate_code_name", "STRING")
        ],
        'pickup_location_dim': [
            bigquery.SchemaField("pickup_location_id", "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("pickup_latitude", "FLOAT"),
            bigquery.SchemaField("pickup_longitude", "FLOAT")
        ],
        'dropoff_location_dim': [
            bigquery.SchemaField("dropoff_location_id", "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("dropoff_latitude", "FLOAT"),
            bigquery.SchemaField("dropoff_longitude", "FLOAT")
        ],
        'payment_type_dim': [
            bigquery.SchemaField("payment_type_id", "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("payment_type", "INTEGER"),
            bigquery.SchemaField("payment_type_name", "STRING")
        ],
        'fact_table': [
            bigquery.SchemaField("VendorID", "INTEGER"),
            bigquery.SchemaField("datetime_id", "INTEGER"),
            bigquery.SchemaField("passenger_count_id", "INTEGER"),
            bigquery.SchemaField("trip_distance_id", "INTEGER"),
            bigquery.SchemaField("rate_code_id", "INTEGER"),
            bigquery.SchemaField("store_and_fwd_flag", "STRING"),
            bigquery.SchemaField("pickup_location_id", "INTEGER"),
            bigquery.SchemaField("dropoff_location_id", "INTEGER"),
            bigquery.SchemaField("payment_type_id", "INTEGER"),
            bigquery.SchemaField("fare_amount", "FLOAT"),
            bigquery.SchemaField("extra", "FLOAT"),
            bigquery.SchemaField("mta_tax", "FLOAT"),
            bigquery.SchemaField("tip_amount", "FLOAT"),
            bigquery.SchemaField("tolls_amount", "FLOAT"),
            bigquery.SchemaField("improvement_surcharge", "FLOAT"),
            bigquery.SchemaField("total_amount", "FLOAT")
        ]
    }
    
    # Load each table to BigQuery
    for table_name, df in data.items():
        table_ref = dataset_ref.table(table_name)
        job_config = bigquery.LoadJobConfig(
            schema=schemas[table_name],
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
        )
        
        job = client.load_table_from_dataframe(
            df, table_ref, job_config=job_config
        )
        job.result()  # Wait for job to complete
        print(f"Loaded {table_name} with {df.shape[0]} rows")


@test
def test_output(output, *args) -> None:
    """
    Test the output of the block.
    """
    # This is a data exporter, so we don't test the output
    pass