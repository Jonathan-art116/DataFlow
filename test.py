# This program is free software: 
# you can redistribute it and/or modify it under the terms of the GNU General Public License as published 
# by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with this program. 
# If not, see <https://www.gnu.org/licenses/>.
import click

class MyCommand(click.Command):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def invoke(self, ctx):
        # Do something before invoking the command
        click.echo('Running MyCommand...')
        super().invoke(ctx)
        # Do something after invoking the command
        click.echo('MyCommand completed.')

@click.group()
def cli():
    pass

@cli.command(cls=MyCommand)
def hello():
    click.echo('Hello, world!')

@cli.command(cls=MyCommand)
def run():
    click.echo("run")
    a = 1 + 5
    return a

if __name__ == '__main__':
    cli()
