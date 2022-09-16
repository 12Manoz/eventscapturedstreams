from DynamoDAO import DynamoDb
import logging
logger = logging.getLogger(__name__)

db = DynamoDb(table_name="tbff2002_prod_autm_rvis_test")


def handler(event, context):
    logger.info(event)
    print(event)
    response = db.query_table_key_and_range_key_begins_with(
        partition_key='cod_chav_patc', partition_key_value="config", range_key="cod_chav_filg", range_key_value="products#")
    products = response["Items"]
    logger.info("We have received products and now we will send to the sqs")
    print(products)
