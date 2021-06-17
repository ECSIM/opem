# -*- coding: utf-8 -*-
"""Version-check script."""
import os
import sys
import codecs
Failed = 0
VERSION = "1.3"

VERSION_1 = VERSION.split(".")[0]
VERSION_2 = str(int(float(VERSION) * 10 - int(VERSION_1) * 10))
VERSION_3 = str(int(float(VERSION) * 100 - int(VERSION_1)
                    * 100 - int(VERSION_2) * 10))
VERSION_4 = "0"

SETUP_ITEMS = [
    "version='{0}'",
    'https://github.com/ecsim/opem/tarball/v{0}']
INSTALL_ITEMS = [
    "[Version {0}](https://github.com/ecsim/opem/archive/v{0}.zip)",
    "Run `OPEM-{0}.exe`",
    "[Exe-Version {0}](https://github.com/ECSIM/opem/releases/download/v{0}/OPEM-{0}.exe)",
    "[DMG-Version {0}](https://github.com/ECSIM/opem/releases/download/v{0}/OPEM-{0}.dmg)"]
CHANGELOG_ITEMS = [
    "## [{0}]",
    "https://github.com/ECSIM/opem/compare/v{0}...develop",
    "[{0}]:"]
DOCUMENT_ITEMS = [
    "### Version {0}"]

HTML_ITEMS = ["Version {0}"]
PARAMS_ITEMS = ["Version = {0}"]
RC_ITEMS = [
    "filevers=({0}, {1}, {2}, {3})",
    "prodvers=({0}, {1}, {2}, {3})",
    "(u'FileVersion', u'{0}.{1}.{2}.{3}'),",
    "(u'ProductVersion', u'{0}, {1}, {2}, {3}')"]
TEST_ITEMS = ["New Version ({0}) Is Available!"]
FILES = {
    "setup.py": SETUP_ITEMS, "INSTALL.md": INSTALL_ITEMS, "CHANGELOG.md": CHANGELOG_ITEMS, os.path.join(
        "Documents", "Amphlett.ipynb"): DOCUMENT_ITEMS, os.path.join(
            "Documents", "Chamberline_Kim.ipynb"): DOCUMENT_ITEMS, os.path.join(
                "Documents", "Larminie_Dicks.ipynb"): DOCUMENT_ITEMS, os.path.join(
                    "Documents", "Padulles_Amphlett.ipynb"): DOCUMENT_ITEMS, os.path.join(
                        "Documents", "Padulles_Hauer.ipynb"): DOCUMENT_ITEMS, os.path.join(
                            "Documents", "Padulles1.ipynb"): DOCUMENT_ITEMS, os.path.join(
                                "Documents", "Padulles2.ipynb"): DOCUMENT_ITEMS, os.path.join(
                                    "otherfile", "test.html"): HTML_ITEMS, os.path.join(
                                        "opem", "Params.py"): PARAMS_ITEMS, os.path.join(
                                            "opem", "Test", "test_Functions.py"): TEST_ITEMS}

TEST_NUMBER = len(FILES.keys()) + 1


def print_result(failed=False):
    """
    Print final result.

    :param failed: failed flag
    :type failed: bool
    :return: None
    """
    message = "Version tag tests "
    if not failed:
        print("\n" + message + "passed!")
    else:
        print("\n" + message + "failed!")
    print("Passed : " + str(TEST_NUMBER - Failed) + "/" + str(TEST_NUMBER))


if __name__ == "__main__":
    for file_name in FILES.keys():
        try:
            file_content = codecs.open(
                file_name, "r", "utf-8", 'ignore').read()
            for test_item in FILES[file_name]:
                if file_content.find(test_item.format(VERSION)) == -1:
                    print("Incorrect version tag in " + file_name)
                    Failed += 1
                    break
        except Exception as e:
            Failed += 1
            print("Error in " + file_name + "\n" + "Message : " + str(e))
    try:
        file_content = codecs.open(
            os.path.join(
                "otherfile",
                "Version.rc"),
            "r",
            "utf-8",
            'ignore').read()
        for test_item in RC_ITEMS:
            if file_content.find(
                test_item.format(
                    VERSION_1,
                    VERSION_2,
                    VERSION_3,
                    VERSION_4)) == -1:
                print("Incorrect version tag in " + "Version.rc")
                Failed += 1
                break
    except Exception as e:
        Failed += 1
        print("Error in Version.rc" + "\n" + "Message : " + str(e))
    if Failed == 0:
        print_result(False)
        sys.exit(0)
    else:
        print_result(True)
        sys.exit(1)
