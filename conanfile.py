from conans import AutoToolsBuildEnvironment, tools, ConanFile


class GnutlsConan(ConanFile):
    name = "GnuTLS"
    version = "3.5.0"
    license = "LGPLv2.1+"
    url = "https://www.gnutls.org/"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "pkg_config"

    # def system_requirements(self):
    #     try:
    #         installer = conans.tools.SystemPackageTool()
    #         installer.update()
    #         installer.install('autoconf')
    #         installer.install('automake')
    #         installer.install('libtool')
    #         installer.install('make')
    #         installer.install('pkg-config')
    #     except:
    #         self.output.warn('Unable to bootstrap required build tools.  If they are already installed, you can ignore this warning.')

    def source(self):
        self.run("wget https://www.gnupg.org/ftp/gcrypt/gnutls/v3.5/gnutls-3.5.0.tar.xz")
        self.run("tar xf ./gnutls-3.5.0.tar.xz")

    def build(self):
        with tools.chdir("gnutls-3.5.0"):
            self.run('autoreconf')
            env_build = AutoToolsBuildEnvironment(self)
            env_build.configure(args=['--without-p11-kit', "--without-p11-kit", "--enable-shared", "--enable-static", "--with-included-libtasn1", "--disable-tools", "--without-idn" "--with-included-unistring"])
            env_build.make()

    def package(self):
        self.copy("*.so", dst="lib", src="gnutls-3.5.0/lib/.libs/", keep_path=False)
        self.copy("*.h", dst="include/gnutls", keep_path=False, src="./lib/includes/gnutls/")
        self.copy("*.h", dst="include/gnutls", keep_path=False, src="gnutls-3.5.0/lib/includes/gnutls/")
        self.copy("*.pc", keep_path=False, src="gnutls-3.5.0/lib/")

    def package_info(self):
        self.cpp_info.libs = ["gnutls"]


