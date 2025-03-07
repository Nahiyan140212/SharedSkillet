import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource("dynamodb")
recipes_table = dynamodb.Table("SharedSkilletRecipes")
orders_table = dynamodb.Table("SharedSkilletOrders")

def save_recipe(recipe: dict):
    recipe_id = str(hash(str(recipe)))
    recipes_table.put_item(Item={
        "id": recipe_id,
        "title": recipe["title"],
        "ingredients": recipe["ingredients"],
        "instructions": recipe["instructions"],
        "public_url": recipe["public_url"]
    })
    return recipe_id

def get_recipes(recipe_ids: list):
    return [recipes_table.get_item(Key={"id": str(id)}).get("Item") for id in recipe_ids if recipes_table.get_item(Key={"id": str(id)}).get("Item")]

def save_order(order: dict, payment_intent: str):
    order_id = str(hash(str(order)))
    orders_table.put_item(Item={
        "order_id": order_id,
        "chef_id": order["chef_id"],
        "items": order["items"],
        "amount": order["amount"],
        "payment_intent": payment_intent,
        "status": "pending"
    })
    return order_id