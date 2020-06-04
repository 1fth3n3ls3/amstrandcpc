import unittest
import amstrandcpc.utils as utils


class TestGetVideoMemoryAddress(unittest.TestCase):
    def test_on_address_requested_obtain_hexadecimal_little_endian_string(self):
        self.assertEqual('00 C0', utils.get_video_memory_address(0, 0, 0))

    def test_on_second_row_requested(self):
        self.assertEqual('50 C0', utils.get_video_memory_address(1, 0, 0))  

    def test_on_second_line_requested(self):
        self.assertEqual('00 C8', utils.get_video_memory_address(0, 1, 0))   

    def test_on_second_pos_requested(self):
        self.assertEqual('01 C0', utils.get_video_memory_address(0, 0, 1))   

    def test_on_7_line_25_row_requested(self):
        self.assertEqual('80 FF', utils.get_video_memory_address(24, 7, 0))  

class TestGetHexColor(unittest.TestCase):
    def test_on_rrrr_get_FF(self):
        self.assertEqual('FF', utils.get_hex_color('rrrr'))

    def test_on_bbbb_get_00(self):
        self.assertEqual('00', utils.get_hex_color('bbbb'))

    def test_on_rbbb_get_88(self):
        self.assertEqual('88', utils.get_hex_color('rbbb'))

    def test_on_ybbb_get_88(self):
        self.assertEqual('80', utils.get_hex_color('ybbb'))

class TestSetColor(unittest.TestCase):
    def test_on_color_set_return_value(self):
        address = [0, 0, 0]
        color = 'rbbb'
        self.assertEqual("3E 88 32 00 C0", utils.set_color(address, color))

    def test_on_2_colors_set_return_value(self):
        address = [0, 0, 0]
        color_a = 'rbbb'
        color_b = 'rrrr'
        self.assertEqual("21 88 FF 22 00 C0", utils.set_color(address, color_a, color_b))

class TestHalt(unittest.TestCase):
    def test_on_halt_requested(self):
        self.assertEqual('76 76 76 76 76 76', utils.halt())

    def test_on_halt_requested_for_2_miliseconds(self):
        self.assertEqual('76 76 76 76 76 76 76 76 76 76 76 76', utils.halt(2))


class TestJoinInstructs(unittest.TestCase):
    def test_on_join_instructs_requested(self):
        lst = ["3E 88 32 00 C0", '76 76 76 76 76 76']
        self.assertEqual("3E 88 32 00 C0 76 76 76 76 76 76", utils.join_instructs(*lst))