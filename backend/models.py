from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import List, Optional
from passlib.context import CryptContext
import bcrypt

# Configuration for password hashing
# "bcrypt" is a common, secure hashing algorithm [1].
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True, min_length=4, max_length=50)
    email: str = Field(unique=True, index=True, max_length=255)
    hashed_password: str = Field(nullable=False)
    is_active: bool = Field(default=True)
    is_admin: bool = Field(default=False)

    # Relationship: One User can have many Recipes
    recipes: List["Recipe"] = Relationship(back_populates="owner")

    def verify_password(self, plain_password: str) -> bool:
        """Verifies a password using direct bcrypt library."""
        return bcrypt.checkpw(
            password=plain_password.encode('utf-8'),
            hashed_password=self.hashed_password.encode('utf-8')
        )

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        """Generates a salt and hashes a password directly."""
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

# --- Ingredient Model ---
class Ingredient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    
    # Foreign Key to Recipe
    recipe_id: Optional[int] = Field(default=None, foreign_key="recipe.id")
    
    # Relationship back to Recipe
    recipe: "Recipe" = Relationship(back_populates="ingredients")

# --- Recipe Models ---
class RecipeBase(SQLModel):
    title: str = Field(index=True)
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)

class Recipe(RecipeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # Foreign Key to User (Ownership)
    user_id: int = Field(foreign_key="user.id")
    
    # Relationships
    owner: User = Relationship(back_populates="recipes")
    ingredients: List[Ingredient] = Relationship(
        back_populates="recipe", 
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )

class RecipeCreate(RecipeBase):
    # Used for API input (excludes id and user_id)
    pass