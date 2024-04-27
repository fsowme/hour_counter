import collections
import typing
from fileinput import input


class InvalidLine(Exception):
    pass


def parse(line: str) -> typing.Tuple[str, int]:
    try:
        name, hours = line.rsplit(maxsplit=1)
        return name, int(hours)
    except ValueError as error:
        raise InvalidLine() from error


def print_result(result: typing.Mapping[str, list[int]]) -> None:
    for name, hours in result.items():
        printable_hours = ', '.join(map(str, hours))
        print(f'{name}: {printable_hours}; sum: {sum(hours)}')


def count_hours() -> None:
    journal = collections.defaultdict(list)
    with input() as stream:
        for line in stream:
            try:
                name, hours = parse(line)
            except InvalidLine:
                continue
            journal[name].append(hours)
    print_result(journal)


if __name__ == '__main__':
    count_hours()
