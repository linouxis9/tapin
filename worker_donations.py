from pprint import pprint
import sys
import json
from bitshares import BitShares
from bitshares.account import Account
from bitshares.blockchain import Blockchain
import logging
log = logging.getLogger(__name__)

from_account = "faucet"
amount = 10000
asset = "TEST"

bitshares = BitShares(
    "wss://node.testnet.bitshares.eu",
    keys=[""],
    nobroadcast=False
)


def run(begin=None, end=None):

    blockchain = Blockchain(
        mode="head",
        bitshares_instance=bitshares
    )

    for op in blockchain.stream(
        start=6110829
    ):
        blockid = op.get("block_num")
        timestamp = op.get("timestamp")

        if not blockid % 100:
            print("Blockid: %d (%s)" % (blockid, timestamp), flush=True)

        try:
            pprint(bitshares.transfer(
                op["op"][1]["name"],
                amount, asset,
                account=from_account
            ))
        except Exception as e:
            log.error(str(e))
            pass


if __name__ == '__main__':
    run()