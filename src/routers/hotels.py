from fastapi import APIRouter, Query, Body
import asyncio

from src.schemas.hotels import HotelsAdd
from src.database import call_stored_proc


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
async def add_hotel(
    hotel_data: HotelsAdd = Body(
        openapi_examples={
            "1": {
                "summary": "Сочи",
                "value": {
                    "title": "Resourt 5 stars",
                    "location": "Сочи, ул.Приморская, 10",
                },
            },
            "2": {
                "summary": "Дубай",
                "value": {
                    "title": "Arabian beach",
                    "location": "Дубай, ул.Шейха, 3",
                },
            }
        }
    ),
    db_object = 'SELECT sch_hotels.f_add_hotels($1)',
):
    hotel = await call_stored_proc(db_object, hotel_data.model_dump_json())
    return {"data": hotel}