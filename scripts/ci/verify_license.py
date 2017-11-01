# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

import os
import sys

from util import get_repo_root

REPO_ROOT = get_repo_root()
SRC_DIR = os.path.join(REPO_ROOT, 'src')

LICENSE_HEADER = """# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
"""


def main():
    env_path = os.path.join(REPO_ROOT, 'env')

    files_without_header = []
    for current_dir, _, files in os.walk(get_repo_root()):
        if current_dir.startswith(env_path):
            continue
        file_itr = (os.path.join(current_dir, p) for p in files if p.endswith('.py'))
        for python_file in file_itr:
            with open(python_file, 'r') as f:
                file_text = f.read()
                if file_text and LICENSE_HEADER not in file_text:
                    files_without_header.append(os.path.join(current_dir, python_file))

    if files_without_header:
        print("Error: The following files don't have the required license headers: \n{}".format(
            '\n'.join(files_without_header)), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
