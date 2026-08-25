# Copyright (C) 2026 Changkai Zhang.
#
# This file is part of Vivian project.
#
# Vivian is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# Vivian is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Vivian. If not, see <https://www.gnu.org/licenses/>.


"""Smoke tests for the Vivian package and its tensor backend."""

from __future__ import annotations

import vivian


def test_version_is_exposed() -> None:
    """The installed distribution version is readable as `vivian.__version__`."""
    assert isinstance(vivian.__version__, str)
    assert vivian.__version__


def test_subpackages_are_importable() -> None:
    """Every subpackage named in `__all__` is reachable as an attribute."""
    for name in vivian.__all__:
        assert hasattr(vivian, name)


def test_backend_is_available() -> None:
    """Nicole and Yuzuha, which power the tensor backend, are installed."""
    import nicole
    import yuzuha

    assert nicole is not None
    assert yuzuha is not None
