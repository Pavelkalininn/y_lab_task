# Homework 2 task 2

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        for period in self.dates:
            current, finish_date = period
            while current <= finish_date:
                yield current
                current += timedelta(1)


if __name__ == '__main__':
    m = Movie('sw', [
      (datetime(2020, 1, 1), datetime(2020, 1, 7)),
      (datetime(2020, 1, 15), datetime(2020, 2, 7))
    ])

    for d in m.schedule():
        print(d)
