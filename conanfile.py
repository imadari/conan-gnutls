from conans import ConanFile, AutoToolsBuildEnvironment, tools


class GnutlsConan(ConanFile):
    name = "GnuTLS"
    version = "3.5.0"
    license = "LGPLv2.1+"
    url = "<Package recipe repository url here, for issues about the package>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"

    def source(self):
        self.run("wget https://www.gnupg.org/ftp/gcrypt/gnutls/v3.5/gnutls-3.5.0.tar.xz")
        self.run("tar xf ./gnutls-3.5.0.tar.xz")

    def build(self):
        #with tools.chdir('gnutls-3.5.0'):
        env_build = AutoToolsBuildEnvironment(self)
        env_build.configure(configure_dir='gnutls-3.5.0', args=['--without-p11-kit'])
            #env_build.configure(args=['--without-p11-kit'])
        env_build.make()

    def package(self):
        #self.copy("*.h", dst="include", src="gnutls-3.5.0", keep_path=True)
        #self.copy("*gnutls*.lib", dst="lib", keep_path=False)
        #self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", src="./lib/.libs/", keep_path=False)
        self.copy("*.h", dst="include/gnutls", keep_path=False, src="./lib/includes/gnutls/")
        #self.copy("compat.h", dst="include/gnutls", keep_path=False, src="./lib/includes/gnutls/")
        self.copy("*.h", dst="include/gnutls", keep_path=False, src="gnutls-3.5.0/lib/includes/gnutls/")
        #self.copy("*.dylib", dst="lib", keep_path=False)
        #self.copy("*.a", dst="lib", keep_path=False)

        # With keep dir:
        # /home/istvan/.conan/data/GnuTLS/3.5.0/gnutls/testing/package/27cb7fbffba1a5268eda91c4da54b0254d48c3b1/include/lib/includes/gnutls/gnutls.h
        # /home/istvan/.conan/data/GnuTLS/3.5.0/gnutls/testing/build/27cb7fbffba1a5268eda91c4da54b0254d48c3b1/lib/includes/gnutls/gnutls.h

        # /home/istvan/.conan/data/GnuTLS/3.5.0/gnutls/testing/package/27cb7fbffba1a5268eda91c4da54b0254d48c3b1/include/gnutls.h
        # /home/istvan/.conan/data/GnuTLS/3.5.0/gnutls/testing/build/27cb7fbffba1a5268eda91c4da54b0254d48c3b1/lib/includes/gnutls/gnutls.h



    def package_info(self):
        self.cpp_info.libs = ["gnutls"]

