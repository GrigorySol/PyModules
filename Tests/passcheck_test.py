import unittest
from Utilites import passcheck


class TestRequestAPIData(unittest.TestCase):

    def setUp(self) -> None:
        self.hash_part = "CBFDA"
        self.wrong_hash_part = "123"

    def test_right_hash(self):
        code = passcheck.request_api_data(self.hash_part).status_code
        self.assertEqual(code, 200)

    def test_wrong_hash(self):
        with self.assertRaises(RuntimeError):
            passcheck.request_api_data(self.wrong_hash_part)


class TestGetHashesForPassword(unittest.TestCase):

    def setUp(self) -> None:
        self.password = "any_password"
        self.wrong_password = 123
        self.pass_hash = "2ead4d954c5b8e825427042a3ef33c7a2d9"
        self.hashes = "2E84FCA2828F32791EFA5DA0C667887030C:5\n" \
                      "2EAD4D954C5B8E825427042A3EF33C7A2D9:3\n" \
                      "2F1788588A1639B278E331DCDFDE42A6357:1"

    def test_right_password_type(self):
        data = passcheck.get_hashes_for_password(self.password)
        self.assertIsInstance(data[0], str)

    def test_wrong_password_type(self):
        with self.assertRaises(AttributeError):
            passcheck.get_hashes_for_password(self.wrong_password)


class TestComparePasswordHash(unittest.TestCase):

    def setUp(self) -> None:
        self.check_hash = "2ead4d954c5b8e825427042a3ef33c7a2d9"
        self.hashes = "2E84FCA2828F32791EFA5DA0C667887030C:5\n" \
                      "2EAD4D954C5B8E825427042A3EF33C7A2D9:3\n" \
                      "2F1788588A1639B278E331DCDFDE42A6357:1"

    def test_right_hash_part(self):
        amount = passcheck.compare_password_hash(self.hashes, self.check_hash)
        self.assertEqual(amount, "3")

    def test_unknown_hash_part(self):
        unknown_hash = "sdfsd234234sdf"
        amount = passcheck.compare_password_hash(self.hashes, unknown_hash)
        self.assertEqual(amount, 0)


class TestCheckPassword(unittest.TestCase):

    def setUp(self) -> None:
        self.passwords = ["123", "abc"]

    def test_right_passwords(self):
        for amount in passcheck.check_password(self.passwords):
            self.assertIsInstance(amount, str)
