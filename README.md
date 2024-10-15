# DynamoDB JSON Loader

This Python script parses a JSON file and loads each object into a DynamoDB table. The configuration, such as table name and file path, is stored in a `config.yaml` file for easy customization.

## Prerequisites

Before running this script, you must have the following set up:

1. **AWS Credentials**:

   - You must configure your AWS credentials with the necessary access to DynamoDB.
   - If you're using the AWS CLI, run the following command to configure your credentials:
     ```bash
     aws configure
     ```
   - Ensure you have the correct permissions to read and write to the DynamoDB table.

2. **Python Packages**:
   - Install the required Python packages using `pip`:
     ```bash
     pip install boto3 pyyaml
     ```

## Configuration

You need to create a `config.yaml` file to specify the DynamoDB table name and the path to the JSON file.

### Example `config.yaml`:

```yaml
dynamodb:
  table_name: YourTableName

files:
  json_file_path: data.json
```

- dynamodb.table_name: The name of your DynamoDB table.
- files.json_file_path: Path to the JSON file containing the data to be loaded.

## Input JSON Format

The script expects the input JSON file to contain an array of objects. Each object will be inserted into the DynamoDB table. Below is an example of an input object:

```
{
    "_id": "608b22e909fd2116bca43429",
    "mixture": [
        "Iron",
        "Carbon"
    ],
    "alloyName": "Steel",
    "createdAt": "2021-04-29T21:19:37.165Z",
    "updatedAt": "2021-04-29T21:19:37.165Z"
}

```

Each object should have a structure compatible with your DynamoDB table schema.

## Usage

1. Clone the repository or download the script files.
2. Create and modify the config.yaml file as needed.
3. Run the Python script to load data into DynamoDB:

```
python load_to_dynamodb.py
```
