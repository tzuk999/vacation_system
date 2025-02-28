from dataclasses import dataclass
from datetime import date

@dataclass
class Vacation:
    id: int
    country_id: int
    description: str
    start_date: date
    end_date: date
    price: float
    image_filename: str