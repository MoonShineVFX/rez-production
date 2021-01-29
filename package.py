
name = "production"

version = "1.1-m1"

description = "Production suite tool provider"

requires = []

build_command = False

suite_root = "T:/rez-studio/sweet/show"
# Profile pkg (in memory) name prefix, for differing with regular packages
mem_pkg_prefix = "_m_show_"


def commands():
    env = globals()["env"]
    ephemerals = globals()["ephemerals"]

    show_eph = ephemerals.get("show")
    if show_eph:
        show_name = show_eph[len(".show-"):]
        suite_path = "{this.suite_root}/%s/bin" % show_name

        env.PATH.prepend(suite_path)

    env.PRODUCTION_SUITE_ROOT = "{this.suite_root}"


@late()
def _data():
    import os
    this = globals()["this"]

    show_name = this.name
    if show_name.startswith(this.mem_pkg_prefix):
        show_name = show_name[len(this.mem_pkg_prefix):]

    parts = show_name.split("_")
    if parts[0].isdigit():
        parts = parts[1:]
    pretty_name = " ".join(parts)

    return {
        "icon": "%s/%s/icon.png" % (this.suite_root, show_name),
        "label": pretty_name,
        "category": os.path.basename(this.suite_root),
    }
