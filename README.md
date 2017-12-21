Blockchain
==========

Created following [this article](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46)

How to
======

Create a virtualenv with Python 3.6,

    mktmpenv -p`which python3.6`

install requirements,

    pip install -r requirements.txt

launch a node on port 5000,

    python api.py

or specify a custom port.

    python api.py 5001

Now you can interact with your blockchains via HTTP.

    curl localhost:5000/mine
    curl localhost:5000/chain
    curl -H 'content-type: application/json' --data '{"nodes": ["http://localhost:5001", "http://localhost:5002"]}' localhost:5000/nodes/register
    curl localhost:5000/nodes/resolve
    curl -H 'content-type: application/json' --data '{"sender": "b71ba9de0fc94efd925bcfe33eeeef59", "recipient": "another-address", "amount": 5}' localhost:5000/transactions/new
