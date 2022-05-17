import boto3

def insert_item():
    table = boto3.resource(
        "dynamodb", region_name="us-east-1").Table("tbff2002_prod_autm_rvis")
    table.put_item(
        Item={
            "cod_chav_patc": "sandboxsre32",
            "cod_chav_filg": "PRRCON39#dev#LATEST",
            "cod_chav_filg_locl": "LATEST#REL#PRRCON39#dev",
            "complaint": False,
            "entity": "Product",
            "pillar": "REL"
        })
    print("inserted successfully")


if __name__ == "__main__":
    insert_item()
