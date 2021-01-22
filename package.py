
name = "production"

version = "1.0-m1"

description = "Show production tool provider"

requires = [
    "house-1.2+",
]

build_command = False


def commands():
    env = globals()["env"]
    ephemerals = globals()["ephemerals"]

    show_eph = ephemerals.get("show")
    if show_eph:
        show_name = show_eph[len(".show-"):]
    else:
        show_name = "site-default"

    suite_path = "$SWEET_SHOW_ROOT/%s/bin" % show_name
    env.PATH.prepend(suite_path)
