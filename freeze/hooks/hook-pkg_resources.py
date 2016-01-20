# Fix issues with new setuptools
# See https://github.com/pyinstaller/pyinstaller/issues/1773


def list_vendored_modules():
    from pkgutil import walk_packages
    import pkg_resources._vendor
    return ["pkg_resources._vendor.{1}".format(*x)
            for x in walk_packages(pkg_resources._vendor.__path__)]

hiddenimports = list_vendored_modules()
