import click

from src.myfunc import square_integer


@click.command()
@click.argument('number', type=int)
def main(number):
    """Calculate the square of a number."""
    result = square_integer(number)
    print(f'The square of {number} is {result}')

if __name__ == '__main__':
    main()
