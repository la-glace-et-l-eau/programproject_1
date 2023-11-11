from conan import ConanFile


class Recipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps", "VirtualRunEnv", "NMakeToolchain", "NMakeDeps", "MSBuildDeps", "MSBuildToolchain"

    def layout(self):
        self.folders.generators = "conan"

    def requirements(self):
        self.requires("fmt/10.1.1")

    def build_requirements(self):
        self.test_requires("catch2/3.4.0")
