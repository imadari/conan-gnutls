import os

from conans import ConanFile, CMake, tools


class GnutlsTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        if not tools.cross_building(self.settings):
            #os.chdir("bin")
            with tools.chdir("bin"):
                self.run("./example")
