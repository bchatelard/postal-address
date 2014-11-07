# -*- coding: utf-8 -*-

from __future__ import (unicode_literals, print_function, absolute_import,
                        division)

import unittest

from address import Address, territory_codes


class TestAddress(unittest.TestCase):

    def test_default_values(self):
        address = Address()
        self.assertEquals(address.line1, None)
        self.assertEquals(address.line2, None)
        self.assertEquals(address.zip_code, None)
        self.assertEquals(address.city, None)
        self.assertEquals(address.country_code, None)
        self.assertEquals(address.subdivision_code, None)

    def test_dict_access(self):
        address = Address()
        self.assertEquals(Address._components, address.keys())
        self.assertEquals(set([None]), set(address.values()))
        self.assertEquals(
            dict.fromkeys(Address._components),
            dict(address.items()))
        for key in address.keys():
            self.assertIsNone(address[key])

    def test_blank_string_normalization(self):
        address = Address(
            line1='',
            line2='',
            zip_code='',
            city='',
            country_code='',
            subdivision_code='')
        self.assertEquals(address.line1, None)
        self.assertEquals(address.line2, None)
        self.assertEquals(address.zip_code, None)
        self.assertEquals(address.city, None)
        self.assertEquals(address.country_code, None)
        self.assertEquals(address.subdivision_code, None)

    def test_territory_codes(self):
        self.assertIn('FR', territory_codes())
        self.assertIn('FR-59', territory_codes())
        self.assertNotIn('FRE', territory_codes())