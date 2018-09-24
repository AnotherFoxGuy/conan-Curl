from conans import ConanFile, CMake, tools
from conans.tools import os_info, SystemPackageTool

class CurlConan(ConanFile):
    name = "Curl"
    version = "7.61.1"
    url = "https://github.com/AnotherFoxGuy/conan-Curl"
    description = "A command line tool and library for transferring data with URL syntax, supporting HTTP, HTTPS, FTP, FTPS, GOPHER, TFTP, SCP, SFTP, SMB, TELNET, DICT, LDAP, LDAPS, FILE, IMAP, SMTP, POP3, RTSP and RTMP. libcurl offers a myriad of powerful features"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/curl/curl.git", "curl-7_61_1")

    def build(self):
        cmake = CMake(self)
        cmake.definitions['BUILD_TESTING'] = False
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
