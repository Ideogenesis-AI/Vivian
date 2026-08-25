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


"""Algorithms operating on 2D tensor networks.

Each algorithm lives in its own submodule and is developed and maintained
as an independent unit on top of the shared `vivian.network` core. Planned
members are CTMRG, simple update, full update, and variational
optimization.
"""

__all__: list[str] = []
