class CinemaHall:
    def __init__(self, hall_number: int):
        self.hall_number = hall_number
    
    def movie_session(self, movie_name: str, customers: list, cleaning_staff) -> None:
        for customer in customers:
            customer.watch_movie(movie_name)
