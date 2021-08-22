import ipaddress
import asyncio


async def tcp_syn(ip='192.168.2.1', port=3389):
    try:
        reader, writer = await asyncio.open_connection(
            host=str(ip), port=int(port))
        return ip
    except:
        return False


async def main(network, port):
    ip_list = ipaddress.ip_network(network)
    tasks = [asyncio.create_task(tcp_syn(ip, port), name=f"{ip}-{port}") for ip in ip_list.hosts()]

    try:
        for coro in asyncio.as_completed(tasks, timeout=3):
            await coro
    except:
        pass

    return [i.result() for i in tasks if i.done() and bool(i.result())]


if __name__ == '__main__':
    print(asyncio.run(main(network='192.168.2.0/24', port=3389)))
