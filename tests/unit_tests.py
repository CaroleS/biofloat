#!/usr/bin/env python

import os
import sys
import unittest
parentDir = os.path.join(os.path.dirname(__file__), "../")
sys.path.insert(0, parentDir)

from oxyfloat import OxyFloat

class DataTest(unittest.TestCase):
    def setUp(self):
        self.of = OxyFloat(verbosity=0)

    def test_get_oxyfloats(self):
        self.oga_floats = self.of.get_oxy_floats()
        self.assertNotEqual(len(self.oga_floats), 0)

    def _get_dac_urls(self):
        # Testing with a float that has data
        oga_floats = ['1900650']
        for dac_url in self.of.get_dac_urls(oga_floats):
            self.dac_url = dac_url
            self.assertTrue(self.dac_url.startswith('http'))
            break

    def _get_profile_opendap_urls(self):
        for profile_url in self.of.get_profile_opendap_urls(self.dac_url):
            self.profile_url = profile_url
            break

    def _profile_to_dataframe(self):
        d = self.of._profile_to_dataframe(self.profile_url)
        self.assertNotEqual(len(d), 0)

    def test_read_profile_data(self):
        # Methods need to be called in order
        self._get_dac_urls()
        self._get_profile_opendap_urls()
        self._profile_to_dataframe()


if __name__ == '__main__':
    unittest.main()
