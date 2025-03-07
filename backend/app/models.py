from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.security import OAuth2PasswordBearer
from .models import Recipe, MealPlan, OrderRequest
from .ai import generate_recipe, image_to_recipe, generate_meal_plan
from .database import save_recipe, get_recipes, save_order
from .payments import process_payment
from mangum import Mangum
import boto3
import os

app = FastAPI(title="SharedSkillet API")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
cognito = boto3.client("cognito-idp")

# Health check
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# AI Recipe Generation (Bedrock)
@app.post("/api/recipes/generate")
async def create_recipe(ingredients: str, token: str = oauth2_scheme):
    try:
        # Validate token with Cognito (simplified)
        payload = cognito.get_user(AccessToken=token)
        recipe = generate_recipe(ingredients)
        save_recipe(recipe)
        return recipe
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

# Image-to-Recipe (Rekognition)
@app.post("/api/recipes/image")
async def analyze_image(file: UploadFile = File(...), token: str = oauth2_scheme):
    try:
        cognito.get_user(AccessToken=token)
        image_content = await file.read()
        recipe = image_to_recipe(image_content)
        save_recipe(recipe)
        return recipe
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

# Personalized Meal Planning (Bedrock)
@app.post("/api/meal-plan")
async def get_meal_plan(preferences: MealPlan, token: str = oauth2_scheme):
    try:
        cognito.get_user(AccessToken=token)
        meal_plan = generate_meal_plan(preferences.dict())
        return meal_plan
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

# Grocery List Generator
@app.get("/api/grocery-list")
async def get_grocery_list(recipe_ids: str, token: str = oauth2_scheme):
    try:
        cognito.get_user(AccessToken=token)
        ids = [int(id) for id in recipe_ids.split(",")]
        recipes = get_recipes(ids)
        ingredients = [item for recipe in recipes for item in recipe.get("ingredients", [])]
        return {"ingredients": list(set(ingredients))}
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

# Order Placement
@app.post("/api/orders")
async def place_order(order: OrderRequest, token: str = oauth2_scheme):
    try:
        cognito.get_user(AccessToken=token)
        payment_intent = process_payment(order.amount, order.token)
        order_id = save_order(order.dict(), payment_intent)
        return {"order_id": order_id, "payment_intent": payment_intent}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Lambda handler
handler = Mangum(app)