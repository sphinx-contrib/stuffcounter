# -*- coding: utf-8 -*-

# Copyright 2018 Louis Paternault
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this package.  If not, see <http://www.gnu.org/licenses/>.

import unittest


class TestDummy(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(1 + 1, 2)
