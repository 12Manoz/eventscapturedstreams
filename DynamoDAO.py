from urllib import response
import boto3
from boto3.dynamodb.conditions import Key


class DynamoDb:
    def __init__(self, table_name) -> None:
        self.__table = boto3.resource('dynamodb').Table(table_name)
        self.__client = boto3.client('dynamodb')
        self.__table_name = table_name

    def query_table_key_and_range_key_begins_with(self, partition_key, partition_key_value, range_key, range_key_value):
        filtering_exp = Key(partition_key).eq(partition_key_value) & Key(
            range_key).begins_with(range_key_value)
        return self.__table.query(KeyConditionExpression=filtering_exp)

    def query_table_key_and_range_key_begins_with_secondary_index(self, partition_key, partition_key_value, range_key, range_key_value, sec_index):
        filtering_exp = Key(partition_key).eq(partition_key_value) & Key(
            range_key).begins_with(range_key_value)
        return self.__table.query(IndexName=sec_index, KeyConditionExpression=filtering_exp)
