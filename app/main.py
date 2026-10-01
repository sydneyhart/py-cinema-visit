from app.customer import Customer
from app.cleaner import Cleaner
from app.cinema_hall import CinemaHall
from app.cinema_bar import CinemaBar


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customer_instances = [
        Customer(
            name=customer["name"],
            food=customer["food"],
        )
        for customer in customers
    ]

    cleaning_staff = Cleaner(name=cleaner)
    hall = CinemaHall(hall_number=hall_number)

    for customer in customer_instances:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer,
        )

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff,
    )
