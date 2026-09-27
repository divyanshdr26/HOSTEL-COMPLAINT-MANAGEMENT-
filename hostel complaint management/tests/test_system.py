import unittest
from database import load_complaints
from validators import valid_category, valid_status


class TestHostelComplaintSystem(unittest.TestCase):
    def test_categories(self):
        categories = {
            "1": "Electrical",
            "2": "Water",
            "3": "Food",
            "4": "Wi-Fi",
            "5": "Cleaning",
            "6": "Furniture",
        }
        self.assertTrue(valid_category("1", categories))
        self.assertFalse(valid_category("9", categories))

    def test_status(self):
        self.assertTrue(valid_status("Pending"))
        self.assertTrue(valid_status("Resolved"))
        self.assertFalse(valid_status("Unknown"))

    def test_sample_data(self):
        complaints = load_complaints()
        self.assertGreaterEqual(len(complaints), 6)


if __name__ == "__main__":
    unittest.main()
