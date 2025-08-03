from fastapi import Path
from ms_core import BaseCRUDRouter

from app import ModelCRUD, Schema
from app.schemas import Create

router = BaseCRUDRouter(
    ModelCRUD, Schema, Create, prefix="/template", tags=["template"]
)


@router.get("/extra/{item_id}")
async def get_by_id(item_id: int = Path()) -> Schema | None:
    return await ModelCRUD.get_by_id(item_id)
