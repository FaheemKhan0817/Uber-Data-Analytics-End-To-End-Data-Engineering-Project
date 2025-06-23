import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Transform Uber data into dimensional model
    """
    # Define mappings
    RATE_CODE_MAPPING = {
        1: "Standard rate",
        2: "JFK",
        3: "Newark",
        4: "Nassau or Westchester",
        5: "Negotiated fare",
        6: "Group ride"
    }

    PAYMENT_TYPE_MAPPING = {
        1: "Credit card",
        2: "Cash",
        3: "No charge",
        4: "Dispute",
        5: "Unknown",
        6: "Voided trip"
    }

    # Convert datetime fields
    data['tpep_pickup_datetime'] = pd.to_datetime(data['tpep_pickup_datetime'])
    data['tpep_dropoff_datetime'] = pd.to_datetime(data['tpep_dropoff_datetime'])
    
    # Create datetime dimension
    datetime_dim = data[['tpep_pickup_datetime', 'tpep_dropoff_datetime']].copy()
    datetime_dim['datetime_id'] = datetime_dim.index + 1
    datetime_dim['pick_hour'] = datetime_dim['tpep_pickup_datetime'].dt.hour
    datetime_dim['pick_day'] = datetime_dim['tpep_pickup_datetime'].dt.day
    datetime_dim['pick_month'] = datetime_dim['tpep_pickup_datetime'].dt.month
    datetime_dim['pick_year'] = datetime_dim['tpep_pickup_datetime'].dt.year
    datetime_dim['pick_weekday'] = datetime_dim['tpep_pickup_datetime'].dt.weekday
    datetime_dim['drop_hour'] = datetime_dim['tpep_dropoff_datetime'].dt.hour
    datetime_dim['drop_day'] = datetime_dim['tpep_dropoff_datetime'].dt.day
    datetime_dim['drop_month'] = datetime_dim['tpep_dropoff_datetime'].dt.month
    datetime_dim['drop_year'] = datetime_dim['tpep_dropoff_datetime'].dt.year
    datetime_dim['drop_weekday'] = datetime_dim['tpep_dropoff_datetime'].dt.weekday
    datetime_dim = datetime_dim.drop(['tpep_pickup_datetime', 'tpep_dropoff_datetime'], axis=1)
    
    # Create other dimensions
    passenger_count_dim = data[['passenger_count']].copy()
    passenger_count_dim['passenger_count_id'] = passenger_count_dim.index + 1
    
    trip_distance_dim = data[['trip_distance']].copy()
    trip_distance_dim['trip_distance_id'] = trip_distance_dim.index + 1
    
    rate_code_dim = data[['RatecodeID']].copy()
    rate_code_dim['rate_code_id'] = rate_code_dim.index + 1
    rate_code_dim['rate_code_name'] = rate_code_dim['RatecodeID'].map(RATE_CODE_MAPPING)
    
    pickup_location_dim = data[['pickup_latitude', 'pickup_longitude']].copy()
    pickup_location_dim['pickup_location_id'] = pickup_location_dim.index + 1
    
    dropoff_location_dim = data[['dropoff_latitude', 'dropoff_longitude']].copy()
    dropoff_location_dim['dropoff_location_id'] = dropoff_location_dim.index + 1
    
    payment_type_dim = data[['payment_type']].copy()
    payment_type_dim['payment_type_id'] = payment_type_dim.index + 1
    payment_type_dim['payment_type_name'] = payment_type_dim['payment_type'].map(PAYMENT_TYPE_MAPPING)
    
    # Create fact table
    fact_table = data[['VendorID', 'store_and_fwd_flag', 'fare_amount', 'extra', 
                      'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge', 'total_amount']].copy()
    fact_table['datetime_id'] = datetime_dim['datetime_id']
    fact_table['passenger_count_id'] = passenger_count_dim['passenger_count_id']
    fact_table['trip_distance_id'] = trip_distance_dim['trip_distance_id']
    fact_table['rate_code_id'] = rate_code_dim['rate_code_id']
    fact_table['pickup_location_id'] = pickup_location_dim['pickup_location_id']
    fact_table['dropoff_location_id'] = dropoff_location_dim['dropoff_location_id']
    fact_table['payment_type_id'] = payment_type_dim['payment_type_id']
    
    return {
        'datetime_dim': datetime_dim,
        'passenger_count_dim': passenger_count_dim,
        'trip_distance_dim': trip_distance_dim,
        'rate_code_dim': rate_code_dim,
        'pickup_location_dim': pickup_location_dim,
        'dropoff_location_dim': dropoff_location_dim,
        'payment_type_dim': payment_type_dim,
        'fact_table': fact_table
    }


@test
def test_output(output, *args) -> None:
    """
    Test the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert isinstance(output, dict), 'Output is not a dictionary of DataFrames'
    assert len(output) == 8, 'Output should contain 8 DataFrames'
    for df in output.values():
        assert not df.empty, 'DataFrame in output is empty'