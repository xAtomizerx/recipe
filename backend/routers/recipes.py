from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import select
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
    # Change db.session.exec to db.exec
    recipe = db.exec(select(Recipe).where(Recipe.id == recipe_id)).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@router.get('/', response_model=list[RecipeResponse])
def get_recipes(db: db_dependency, user: user_dependency):
    # Change db.session.exec to db.exec
    return db.exec(select(Recipe).where(Recipe.id == user.get('id'))).all()

@router.delete('/')
def delete_recipe(db: db_dependency, user: user_dependency, recipe_id: int):
    # Change db.session.exec to db.exec
    db_recipe = db.exec(select(Recipe).where(Recipe.id == recipe_id)).first()
    if db_recipe:
        db.delete(db_recipe)
        db.commit()
    return {"message": "Deleted"}
