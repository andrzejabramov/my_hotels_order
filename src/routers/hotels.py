from fastapi import APIRouter, Query

from schemas.hotels import HotelsAdd
from sqlalchemy.orm import defer

router = APIRouter(prefix='/hotels', tags=['Отели'])


@router.get(
    "",
    summary="Получение списка отелей с применением фильтра",
    description="Либо получаем все отели, если не устанавливаем параметры, либо отдельно взятые",
            )
async def get_hotels(
    title: str | None = Query(None, description='название отеля'),
    location: str | None = Query(None, description='адрес отеля'),
) -> dict:
    return {'hotels': title, 'location': location}

@router.post("")
async def add_hotel() -> dict:
    pass