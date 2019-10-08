from conans import ConanFile, CMake, tools
import os
import shutil
import json

class HnswlibConan(ConanFile):
    #TODO wrap with Conan build tools to extract version from source
    name = "hnswlib"
    branch = "master"
    license = "MIT"
    author = "B. van Lew b.van_lew@lumc.nl"
    # The url for the conan recipe
    url = "https://github.com/nmslib/hnswlib" 
    description = "Header-only C++/python library for fast approximate nearest neighbors."
    topics = ("hdps", "plugin", "image data", "loading")
    # No settings/options are necessary, this is header only
    exports_sources = "hnswlib/*"
    no_copy_source = True
            
    def source(self):
        self.run("git clone {0}.git".format(self.url))

    def package(self):
        self.copy("*.h")

