from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Depends, status, HTTPException
from models import Recipe
from deps import db_dependency, user_dependency

router = APIRouter(
    prefix='/recipe',
    tags=['recipe']
)
class RecipeBase(BaseModel):
    title: str
    description: Optional[str] = None
    ingredients: list[str] = []

class RecipeCreate(RecipeBase):
    # schema for creating a recipe (without ID)
    pass

class RecipeResponse(RecipeBase):
    # schema for returning a recipe (includes ID)
    id: int

    class ConfigDict:
        from_attributes = True

@router.get('/{recipe_id}', response_model=RecipeResponse)
def get_recipe(db: db_dependency, user: user_dependency, recipe_id: int):
    # Ensure a recipe is found or return 404
    recipe = db.session.exec(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@router.get('/', response_model=list[RecipeResponse])
def get_recipes(db: db_dependency, user: user_dependency):
    # Only return recipes belonging to the current user for security
    return db.session.exec(Recipe).filter(Recipe.user_id == user.get('id')).all()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=RecipeResponse)
def create_recipe(db: db_dependency, user: user_dependency, recipe: RecipeCreate):
    # unpacking all of the data from the recipe object
    db_recipe = Recipe(**recipe.model_dump(), user_id=user.get('id'))
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

@router.delete('/')
def delete_recipe(db: db_dependency, user: user_dependency, recipe_id: int):
    db_recipe = db.session.exec(Recipe).filter(Recipe.id == recipe_id).first()
    if db_recipe:
        db.session.delete(db_recipe)
        db.session.commit()
    return db_recipe
