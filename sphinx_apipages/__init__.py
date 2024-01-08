r"""Extension that generates API pages using autosummary.

It reads RST files from ``apipages_src_dir``
that specify the modules, classes, and functions
to be included in the API documentation.

It then creates sub-pages for those
inside ``apipages_dst_dir``
and builds the documentation afterwards,
ignoting all files inside ``apipages_src_dir``.

"""
import filecmp
import os
import shutil
import typing

import sphinx

import audeer


__version__ = "0.1.0"
package_dir = os.path.abspath(os.path.dirname(__file__))


# ===== MAIN FUNCTION SPHINX EXTENSION ====================================
def setup(app: sphinx.application.Sphinx):
    r"""Modelcard Sphinx extension."""
    # Add config values
    app.add_config_value("apipages_src_dir", "docs/api-src", False)
    app.add_config_value("apipages_dst_dir", "docs/api", False)

    # Extend templates_path for autosummary templates
    templates_path = audeer.path(package_dir, "templates")
    if hasattr(app.config, "templates_path"):
        app.config.templates_path.append(templates_path)
    else:
        app.config.templates_path = templates_path

    # Connect builder
    app.connect("builder-inited", builder_inited)

    return {"version": __version__, "parallel_read_safe": True}


# ===== SPHINX EXTENSION FUNCTIONS ========================================
#
# All functions defined here
# are added to the extension
# via app.connect()
# in setup()
#
def builder_inited(app: sphinx.application.Sphinx):
    r"""Emitted when the builder object has been created.

    It is available as ``app.builder``.

    """
    # Read config values
    src_dir = app.config.apipages_src_dir
    dst_dir = app.config.apipages_dst_dir

    # Copy API (sub-)module RST files to dst folder
    if os.path.exists(src_dir):
        audeer.mkdir(dst_dir)
        api_src_files = audeer.list_file_names(src_dir)
        api_dst_files = [
            audeer.path(dst_dir, os.path.basename(src_file))
            for src_file in api_src_files
        ]
        for src_file, dst_file in zip(api_src_files, api_dst_files):
            if (
                not os.path.exists(dst_file)  # new file
                or not filecmp.cmp(src_file, dst_file)  # changed file
            ):
                shutil.copyfile(src_file, dst_file)  # Find model cards