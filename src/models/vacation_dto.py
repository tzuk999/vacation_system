from dataclasses import dataclass
from datetime import date

@dataclass
class VacationDTO:
    id: int
    country_id: int
    description: str
    start_date: date
    end_date: date
    price: float
    image_file_name: str