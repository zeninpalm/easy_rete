import unittest
from unittest.mock import MagicMock
from easy_inference.algorithms.rete.network import Network

class ReteTests(unittest.TestCase):

    def test_creation_with_rules(self):
        mocked_rules = MagicMock()
        network = Network(rules = mocked_rules)
        self.assertEqual(network.rules, mocked_rules)

if __name__ == "__main__":
    unittest.main()

