# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import

try:
    from .generated.commands import *  # noqa: F403
except ImportError:
    pass

try:
    from .generated.commands import *  # noqa: F403
except ImportError:
    pass
