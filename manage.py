import os
import click


@click.group()
def manage():
    pass


@click.command()
def newproblem():
    from template import new_problem
    new_problem.main()


manage.add_command(newproblem)


if __name__ == "__main__":
    manage()