import unittest
from quotes import compare_quotes


class QuoteTests(unittest.TestCase):
    def test_combined_shipping_changes_winner(self):
        quotes = [
            dict(category="board", part_number="A1", supplier="A", unit_price="50", shipping_cost="20",
                 url="https://example.com/a1", compatible=True, in_stock=True),
            dict(category="antenna", part_number="A2", supplier="A", unit_price="10", shipping_cost="20",
                 url="https://example.com/a2", compatible=True, in_stock=True),
            dict(category="board", part_number="B1", supplier="B", unit_price="55", shipping_cost="3",
                 url="https://example.com/b1", compatible=True, in_stock=True),
            dict(category="antenna", part_number="B2", supplier="B", unit_price="12", shipping_cost="3",
                 url="https://example.com/b2", compatible=True, in_stock=True),
        ]
        result = compare_quotes(["board", "antenna"], quotes)
        self.assertEqual(result["total_pre_tax"], "70")
        self.assertEqual([x["part_number"] for x in result["items"]], ["B1", "B2"])

    def test_missing_items_never_invented(self):
        result = compare_quotes(["board","antenna"], [
            dict(category="board", part_number="A", supplier="S", unit_price="50", shipping_cost="5",
                 url="https://example.com/a", compatible=True, in_stock=True)
        ])
        self.assertEqual(result["status"], "missing_offers")
        self.assertEqual(result["missing_categories"], ["antenna"])

    def test_unknown_shipping_fails(self):
        with self.assertRaises(ValueError):
            compare_quotes(["board"], [
                dict(category="board", part_number="A", supplier="S", unit_price=50,
                     url="https://example.com/a", compatible=True, in_stock=True)
            ])


if __name__ == "__main__":
    unittest.main()
