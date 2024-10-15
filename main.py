import json
import boto3
import yaml

# Load configuration from config.yaml
def load_config(config_file):
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)

# Initialize DynamoDB and table using configuration
def load_dynamodb_table(config):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(config['dynamodb']['table_name'])
    return table

# Insert data into DynamoDB
def insert_data_to_dynamodb(table, json_data):
    for item in json_data:
        response = table.put_item(Item=item)
        print(f"Inserted item: {item} - Status: {response['ResponseMetadata']['HTTPStatusCode']}")

if __name__ == "__main__":
    # Load configuration from config.yaml
    config = load_config('config.yaml')
    
    # Load DynamoDB table
    table = load_dynamodb_table(config)
    
    # Read JSON file
    with open(config['files']['json_file_path']) as json_file:
        data = json.load(json_file)  # Load JSON data
    
    # Insert the parsed data into DynamoDB
    insert_data_to_dynamodb(table, data)
