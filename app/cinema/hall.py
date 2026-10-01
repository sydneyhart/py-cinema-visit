hall = CinemaHall(hall_number=5)
movie_name = "Madagascar"
customers = [
    Customer(name="Bob", food="Coca-cola"),
    Customer(name="Alex", food="popcorn")
]
cleaning_staff = Cleaner(name="Anna")

hall.movie_session(movie_name=movie_name, customers=customers, cleaning_staff=cleaning_staff)
