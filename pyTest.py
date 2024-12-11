'''
Testing the smart contract
'''
import pytest
import pytest_asyncio
from web3 import (EthereumTesterProvider, Web3)
from web3.eth import (AsyncEth,)
from web3.providers.eth_tester.main import (AsyncEthereumTesterProvider)


@pytest.fixture
def tester_provider():
    return EthereumTesterProvider()