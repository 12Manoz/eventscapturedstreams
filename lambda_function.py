from email import message
import logging
import os
from crhelper import CfnResource
from DynamoDAO import DynamoDb
from SQSQueue import Queue

logger = logging.getLogger(__name__)


helper = CfnResource(
)

db = DynamoDb(table_name="tbff2002_prod_autm_rvis_test")


def handler(event, context):
    helper(event, context)


@helper.update
@helper.create
def create(event, context):
    logger.info("Resource Created")
    ResourceProperties = event["ResourceProperties"]
    logger.info(event)
    logger.info('First phase we will get all the products second phase we will get all the porducts id')
    logger.info("All products are stored in the config partitions")
    logger.info("all products in config partitions begin with products hash value")
    try:
        response = db.query_table_key_and_range_key_begins_with(
        partition_key='cod_chav_patc', partition_key_value="config", range_key="cod_chav_filg", range_key_value="products#")
        products = response["Items"]
        logger.info("We have received products and now we will send to the sqs")
        process_products(products)
        return "processsing Done"
    except Exception as error :
        logger.error("Exception occured")
        logger.error(error)
        return "Exception occured"
    finally:
        return "finally block completed"


# @helper.update
# def udpate(event,context):
#     create(event,context)
#     return "Update completed"


@helper.delete
def delete(event,context):
    return "DeleteStackComplete"


def process_products(products):
    queue_name = os.environ.get("sqsqueuename")
    logger.info(f"queuename: {queue_name}")
    queue = Queue(queue_name)

    for product in products:
        if "cod_chav_filg" in product:
            product_id = product["cod_chav_filg"].split("#")[1]
            message = product_id
            queue.send_message(message)
    logger.info("Message send to SQS completed")
    return


def get_account_details(productid):
    product_details=[]
    response = db.query_table_key_and_range_key_begins_with_secondary_index(
        'cod_chav_patc', 'config', 'cod_chav_filg_locl', f'env#{product_id}#', 'xff20022')
    product_env_details = response['Items']
    product_details.append([{"product_id": product_id, "account": item["cod_chav_filg"].split("#")[
                           1], "environemnt": item["cod_chav_filg_locl"].split(f"env#{product_id}#")[1]} for item in product_env_details])
    return product_details