from google.cloud import bigquery

schema = {
    'dim_customer': [
        bigquery.SchemaField('id', 'BIGNUMERIC', 'REQUIRED', None, None, (), None),
        bigquery.SchemaField('sex', 'STRING', 'NULLABLE', None, None, (), None),
        bigquery.SchemaField('age_group', 'STRING', 'NULLABLE', None, None, (), None)
    ],
    'dim_date': [
        bigquery.SchemaField('date', 'DATE', 'REQUIRED', None, None, (), None),
        bigquery.SchemaField('month', 'STRING', 'REQUIRED', None, None, (), None),
        bigquery.SchemaField('year', 'INTEGER', 'REQUIRED', None, None, (), None),
        bigquery.SchemaField('quarter_number', 'STRING', 'REQUIRED', None, None, (), None),
        bigquery.SchemaField('day_of_week', 'STRING', 'NULLABLE', None, None, (), None)
    ],
    'dim_manager': [
        bigquery.SchemaField('id', 'BIGNUMERIC', 'REQUIRED', None, None, (), None),
        bigquery.SchemaField('traiding_point', 'STRING', 'REQUIRED', None, None, (), None),
        bigquery.SchemaField('city', 'STRING', 'NULLABLE', None, None, (), None),
        bigquery.SchemaField('sex', 'STRING', 'NULLABLE', None, None, (), None),
        bigquery.SchemaField('age_group', 'STRING', 'NULLABLE', None, None, (), None)
    ],
    'dim_order': [
        bigquery.SchemaField('id', 'BIGNUMERIC', 'REQUIRED', None, None, (), None),
        bigquery.SchemaField('vendor', 'STRING', 'NULLABLE', None, None, (), None),
        bigquery.SchemaField('type', 'STRING', 'REQUIRED', None, None, (), None),
        bigquery.SchemaField('gem', 'STRING', 'NULLABLE', None, None, (), None),
        bigquery.SchemaField('metal', 'STRING', 'NULLABLE', None, None, (), None),
        bigquery.SchemaField('assay', 'INTEGER', 'NULLABLE', None, None, (), None),
        bigquery.SchemaField('color', 'STRING', 'NULLABLE', None, None, (), None),
        bigquery.SchemaField('weight', 'FLOAT', 'NULLABLE', None, None, (), None),
        bigquery.SchemaField('vendor_size', 'STRING', 'NULLABLE', None, None, (), None)
    ],
    'fact_delivered_order': [
        bigquery.SchemaField('date', 'DATE', 'REQUIRED', None, 'dimension', (), None),
        bigquery.SchemaField('order_id', 'BIGNUMERIC', 'REQUIRED', None, 'dimension', (), None),
        bigquery.SchemaField('customer_id', 'BIGNUMERIC', 'REQUIRED', None, 'dimension', (), None),
        bigquery.SchemaField('manager_id', 'BIGNUMERIC', 'REQUIRED', None, 'dimension', (), None),
        bigquery.SchemaField('accurancy_weight', 'FLOAT', 'NULLABLE', None, 'metric', (), None),
        bigquery.SchemaField('cost', 'FLOAT', 'REQUIRED', None, 'metric', (), None),
        bigquery.SchemaField('profit', 'FLOAT', 'REQUIRED', None, 'metric', (), None),
        bigquery.SchemaField('production_duration', 'INTEGER', 'NULLABLE', None, 'metric', (), None)
    ],
    'fact_payment': [
        bigquery.SchemaField('date', 'DATE', 'REQUIRED', None, 'dimension', (), None),
        bigquery.SchemaField('order_id', 'BIGNUMERIC', 'REQUIRED', None, 'dimension', (), None),
        bigquery.SchemaField('customer_id', 'BIGNUMERIC', 'REQUIRED', None, 'dimension', (), None),
        bigquery.SchemaField('manager_id', 'BIGNUMERIC', 'REQUIRED', None, 'dimension', (), None),
        bigquery.SchemaField('amount', 'FLOAT', 'NULLABLE', None, 'metric', (), None),
        bigquery.SchemaField('pay_left', 'FLOAT', 'NULLABLE', None, 'metric', (), None)
    ]
}
