import unittest

from duckfine import DuckFine


class DuckFineTests(unittest.TestCase):
    def test_initializes_member_and_zero_balance(self):
        duckfine = DuckFine("member-123")

        self.assertEqual(duckfine.member_id, "member-123")
        self.assertEqual(duckfine.total_owed, 0.0)

    def test_forgives_first_two_late_days(self):
        duckfine = DuckFine("member-123")

        fee = duckfine.charge(2)

        self.assertEqual(fee, 0.0)

    def test_charges_daily_fee_after_grace_period(self):
        duckfine = DuckFine("member-123")

        fee = duckfine.charge(5)

        self.assertEqual(fee, 1.50)

    def test_doubles_fee_for_deluxe_duck(self):
        duckfine = DuckFine("member-123")

        fee = duckfine.charge(5, deluxe=True)

        self.assertEqual(fee, 3.00)

    def test_caps_a_single_fee_at_maximum(self):
        duckfine = DuckFine("member-123")

        fee = duckfine.charge(20)

        self.assertEqual(fee, 5.00)

    def test_adds_each_fee_to_total_owed(self):
        duckfine = DuckFine("member-123")

        duckfine.charge(3)
        duckfine.charge(4)

        self.assertEqual(duckfine.total_owed, 1.50)

    def test_rejects_negative_days_without_charging(self):
        duckfine = DuckFine("member-123")

        with self.assertRaises(ValueError):
            duckfine.charge(-1)

        self.assertEqual(duckfine.total_owed, 0.0)


if __name__ == "__main__":
    unittest.main()
