from conans import ConanFile, AutoToolsBuildEnvironment, tools


class GnutlsConan(ConanFile):
    name = "GnuTLS"
    version = "3.5.0"
    license = "LGPLv2.1+"
    url = "https://www.gnutls.org/"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"

    def source(self):
        self.run("wget https://www.gnupg.org/ftp/gcrypt/gnutls/v3.5/gnutls-3.5.0.tar.xz")
        self.run("tar xf ./gnutls-3.5.0.tar.xz")

    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        env_build.configure(configure_dir='gnutls-3.5.0', args=['--without-p11-kit'])
        env_build.make()

    def package(self):
        self.copy("*.so", dst="lib", src="./lib/.libs/", keep_path=False)
        self.copy("*.h", dst="include/gnutls", keep_path=False, src="./lib/includes/gnutls/")
        self.copy("*.h", dst="include/gnutls", keep_path=False, src="gnutls-3.5.0/lib/includes/gnutls/")

    def package_info(self):
        self.cpp_info.libs = ["gnutls"]

