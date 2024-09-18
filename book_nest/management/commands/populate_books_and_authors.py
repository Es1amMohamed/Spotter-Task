from django.core.management.base import BaseCommand
from datetime import date
from book_nest.models import Auther, Book


class Command(BaseCommand):
    help = "Populate database with authors and books data"

    def handle(self, *args, **kwargs):
        # Authors
        author1 = Auther.objects.create(
            name="Stephen King",
            biography="Stephen King is a prolific American author of horror, supernatural fiction, suspense, and fantasy novels.",
            birth_date=date(1947, 9, 21),
            nationality="American",
            website="https://stephenking.com",
            awards="Bram Stoker Award, World Fantasy Award",
        )

        author2 = Auther.objects.create(
            name="J.K. Rowling",
            biography="J.K. Rowling is a British author, best known for the Harry Potter series.",
            birth_date=date(1965, 7, 31),
            nationality="British",
            website="https://www.jkrowling.com",
            awards="Hugo Award, British Book Awards",
        )

        author3 = Auther.objects.create(
            name="Isaac Asimov",
            biography="Isaac Asimov was a Russian-American author and professor of biochemistry, best known for his science fiction works.",
            birth_date=date(1920, 1, 2),
            nationality="American",
            website="",
            awards="Hugo Award, Nebula Award",
        )

        author4 = Auther.objects.create(
            name="Agatha Christie",
            biography="Agatha Christie was an English writer known for her 66 detective novels and 14 short story collections.",
            birth_date=date(1890, 9, 15),
            nationality="British",
            website="",
            awards="Edgar Award",
        )

        author5 = Auther.objects.create(
            name="George Orwell",
            biography="George Orwell was an English novelist, essayist, and critic, famous for his works on political issues.",
            birth_date=date(1903, 6, 25),
            nationality="British",
            website="",
            awards="Prometheus Hall of Fame Award",
        )
        # Create books for each author

        # Stephen King books
        Book.objects.create(
            title="The Shining",
            auther=author1,
            description="A horror novel about a haunted hotel.",
            category="HOR",
            language="English",
            pages=447,
            published_date=date(1977, 1, 28),
        )

        Book.objects.create(
            title="It",
            auther=author1,
            description="A story about seven children terrorized by a being called It.",
            category="HOR",
            language="English",
            pages=1138,
            published_date=date(1986, 9, 15),
        )

        Book.objects.create(
            title="Misery",
            auther=author1,
            description="A psychological horror novel about a famous author and his deranged fan.",
            category="HOR",
            language="English",
            pages=320,
            published_date=date(1987, 6, 8),
        )

        Book.objects.create(
            title="Carrie",
            auther=author1,
            description="A supernatural horror novel about a bullied girl with telekinetic powers.",
            category="HOR",
            language="English",
            pages=199,
            published_date=date(1974, 4, 5),
        )

        # J.K. Rowling books
        Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            auther=author2,
            description="The first book in the Harry Potter series.",
            category="FAN",
            language="English",
            pages=223,
            published_date=date(1997, 6, 26),
        )

        Book.objects.create(
            title="Harry Potter and the Chamber of Secrets",
            auther=author2,
            description="The second book in the Harry Potter series.",
            category="FAN",
            language="English",
            pages=251,
            published_date=date(1998, 7, 2),
        )

        Book.objects.create(
            title="Harry Potter and the Prisoner of Azkaban",
            auther=author2,
            description="The third book in the Harry Potter series.",
            category="FAN",
            language="English",
            pages=317,
            published_date=date(1999, 7, 8),
        )

        Book.objects.create(
            title="Harry Potter and the Goblet of Fire",
            auther=author2,
            description="The fourth book in the Harry Potter series.",
            category="FAN",
            language="English",
            pages=636,
            published_date=date(2000, 7, 8),
        )

        # Isaac Asimov books
        Book.objects.create(
            title="Foundation",
            auther=author3,
            description="A science fiction novel about the collapse of a galactic empire.",
            category="SF",
            language="English",
            pages=244,
            published_date=date(1951, 5, 1),
        )

        Book.objects.create(
            title="Foundation and Empire",
            auther=author3,
            description="The second novel in the Foundation series.",
            category="SF",
            language="English",
            pages=227,
            published_date=date(1952, 10, 1),
        )

        Book.objects.create(
            title="Second Foundation",
            auther=author3,
            description="The third novel in the Foundation series.",
            category="SF",
            language="English",
            pages=210,
            published_date=date(1953, 11, 1),
        )

        Book.objects.create(
            title="I, Robot",
            auther=author3,
            description="A collection of short stories about robots and the Three Laws of Robotics.",
            category="SF",
            language="English",
            pages=253,
            published_date=date(1950, 12, 2),
        )

        # Agatha Christie books
        Book.objects.create(
            title="Murder on the Orient Express",
            auther=author4,
            description="A detective novel featuring Hercule Poirot.",
            category="FIC",
            language="English",
            pages=256,
            published_date=date(1934, 1, 1),
        )

        Book.objects.create(
            title="The Murder of Roger Ackroyd",
            auther=author4,
            description="A detective novel featuring Hercule Poirot.",
            category="FIC",
            language="English",
            pages=312,
            published_date=date(1926, 6, 1),
        )

        Book.objects.create(
            title="And Then There Were None",
            auther=author4,
            description="A mystery novel considered one of the best-selling books of all time.",
            category="FIC",
            language="English",
            pages=272,
            published_date=date(1939, 11, 6),
        )

        Book.objects.create(
            title="Death on the Nile",
            auther=author4,
            description="A detective novel featuring Hercule Poirot.",
            category="FIC",
            language="English",
            pages=288,
            published_date=date(1937, 11, 1),
        )

        # George Orwell books
        Book.objects.create(
            title="1984",
            auther=author5,
            description="A dystopian novel about a totalitarian regime.",
            category="FIC",
            language="English",
            pages=328,
            published_date=date(1949, 6, 8),
        )

        Book.objects.create(
            title="Animal Farm",
            auther=author5,
            description="A satirical novella about the dangers of totalitarianism.",
            category="FIC",
            language="English",
            pages=112,
            published_date=date(1945, 8, 17),
        )

        Book.objects.create(
            title="Homage to Catalonia",
            auther=author5,
            description="A personal account of George Orwell's experiences during the Spanish Civil War.",
            category="HIS",
            language="English",
            pages=232,
            published_date=date(1938, 4, 25),
        )

        Book.objects.create(
            title="The Road to Wigan Pier",
            auther=author5,
            description="A political book documenting the harsh living conditions of working-class Britons.",
            category="FIC",
            language="English",
            pages=224,
            published_date=date(1937, 3, 8),
        )

        self.stdout.write(
            self.style.SUCCESS("Database populated with authors and books")
        )
