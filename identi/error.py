#!/usr/bin/python
#
# Copyright (C) 2012 Sibi <sibi@psibi.in>
#
# This file is part of Identity.
#
# Identity is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Identity is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Identity.  If not, see <http://www.gnu.org/licenses/>.
#
#
# Author:   Sibi <sibi@psibi.in>

class IdentiError(AttributeError):
    """Generic Error class for Identier"""
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)
