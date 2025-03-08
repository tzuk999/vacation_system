from dal.vacations_dao import VacationsDAO
from models.vacation_dto import VacationDTO
from datetime import date

class VacationService:
    def __init__(self, connection_params, schema_name):
        self.vacations_dao = VacationsDAO(connection_params, "vacations", schema_name)



    def get_all_vacations(self):
        try:
            return self.vacations_dao.getAllVacations()
        except Exception as e:
            raise Exception("Database error") from e



    def add_vacation(self, country_id: int, description: str, start_date: date, end_date: date, price: float, image_file_name: str):
        if price < 0 or price > 10000:
            raise ValueError("Price must be between 0 and 10,000")
        
        if end_date < start_date:
            raise ValueError("End date cannot be before start date")
        
        vacation_data = {
            "country_id": country_id,
            "description": description,
            "start_date": start_date,
            "end_date": end_date,
            "price": price,
            "image_file_name": image_file_name
        }
        
        try:
            new_vacation_data = self.vacations_dao.add_row(vacation_data)
            if new_vacation_data:
                new_vacation = VacationDTO(new_vacation_data["id"], new_vacation_data["country_id"], new_vacation_data["descriptiom"], new_vacation_data["start_date"],
                                            new_vacation_data["end_date"], new_vacation_data["price"], new_vacation_data["image_file_name"])
                print(f"vacation {new_vacation.id} updated")
                return new_vacation
        except Exception as e:
            raise Exception("Database error") from e



    def update_vacation(self, vacation_id: int, country_id: int, description: str, start_date: date, end_date: date, price: float, image_file_name: str):
        if price < 0 or price > 10000:
            raise ValueError("Price must be between 0 and 10,000")
        
        if end_date < start_date:
            raise ValueError("End date cannot be before start date")
        
        if image_file_name:
            vacation_data = {
                "country_id": country_id,
                "description": description,
                "start_date": start_date,
                "end_date": end_date,
                "price": price,
                "image_file_name": image_file_name
            }
        else:
            vacation_data = {
                "country_id": country_id,
                "description": description,
                "start_date": start_date,
                "end_date": end_date,
                "price": price
            }
        
        try:
            self.vacations_dao.update_by_id(vacation_id, vacation_data)
            print(f"vacation {vacation_id} updated")
        except Exception as e:
            raise Exception("Database error") from e



    def delete_vacation(self, vacation_id: int):
        try:
            self.vacations_dao.delete_by_id(vacation_id)
            print(f'vacation- {vacation_id} deleted')
        except Exception as e:
            raise Exception("Database error") from e
