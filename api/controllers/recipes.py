# controllers/recipes.py
from sqlalchemy.orm import Session
from ..models import models, schemas

def create(db: Session, recipe: schemas.RecipeCreate):
    db_recipe = models.Recipe(
        sandwich_id=recipe.sandwich_id,
        resource_id=recipe.resource_id,
        amount=recipe.amount
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def read_all(db: Session):
    return db.query(models.Recipe).all()

def read_one(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def update(db: Session, recipe: schemas.RecipeUpdate, recipe_id: int):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if db_recipe is None:
        return None
    for var, value in vars(recipe).items():
        if value is not None:
            setattr(db_recipe, var, value)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def delete(db: Session, recipe_id: int):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if db_recipe is None:
        return None
    db.delete(db_recipe)
    db.commit()
    return db_recipe