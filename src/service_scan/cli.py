#!/usr/bin/env python

import asyncio
import click
from core import main


@click.command()
@click.option('--net', help='Enter network to scan', default='192.168.2.0/24', )
@click.option('--port', help='Enter the port from the service', default='3389', type=click.IntRange(1, 65536))
def start(net, port):
    click.echo(f"Scanning network {net} for services on port {port}")
    print(asyncio.run(main(network=net, port=port)))


if __name__ == '__main__':
    start()
