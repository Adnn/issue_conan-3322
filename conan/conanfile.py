from conans import ConanFile, CMake, tools

class ScmtestConan(ConanFile):
    name = "scm-test"
    version = "0.0.0"
    description = "Try the SCM conanfile attribute"
    settings = "os", "compiler", "build_type", "arch"

    generators = "cmake", "cmake_paths"

    scm = {
        "type": "git",
        "subfolder": "cloned_repo",
        "url": "auto",
        "revision": "auto"
    }

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="cloned_repo")
        cmake.build()
        cmake.install()

    def package(self):
        # Done by the install step in build()
        pass

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
