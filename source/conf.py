#
# Copyright 2022 European Centre for Medium-Range Weather Forecasts (ECMWF)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.
#


# Configuration file for the Sphinx documentation builder.

import os
repo_dir = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
print(repo_dir)
print(os.getcwd())

from pathlib import Path
from git import Repo
git_dir = Path(repo_dir) / "git"
shutil.rmtree(git_dir)
git_dir.mkdir(parents=True, exist_ok=True)
Repo.clone_from("https://github.com/ecmwf-projects/polytope-server.git", git_dir.str())

import shutil
doc_dir = Path(repo_dir) / "source_all"
shutil.rmtree(doc_dir)
doc_dir.mkdir(parents=True, exist_ok=True)

import polytope

# -- Project information

project = "Polytope client"
copyright = "2021, ECMWF"
author = "ECMWF"

release = polytope.__version__

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

# -- Options for EPUB output
epub_show_urls = "footnote"

html_extra_path = ["schemas", "static"]


def setup(app):
    app.add_css_file("../my_theme.css")
