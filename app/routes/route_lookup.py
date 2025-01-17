from fastapi import APIRouter, Query
from typing import List, Optional
from app.services.route_service import calculate_route

router = APIRouter()

@router.get("/")
async def get_route(
  stops: List[str] = Query(..., description="List of stops in order"),
  filters: Optional[List[str]] = Query(None, description="Filters to exclude certain modes of transportation, e.g., 'no_car', 'no_airplane'")
):
  
  result = calculate_route(stops, filters)

  return result