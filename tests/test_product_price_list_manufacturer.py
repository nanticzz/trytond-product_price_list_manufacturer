# This file is part of the product_price_list_manufacturer module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class ProductPriceListManufacturerTestCase(ModuleTestCase):
    'Test Product Price List Manufacturer module'
    module = 'product_price_list_manufacturer'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ProductPriceListManufacturerTestCase))
    return suite