from run_command import run_command
import os
def build_no_dependencies(build_type:str):
    cwd= os.getcwd()
    os.chdir("..")
    run_command(["cmake","-B",f"Build/NoDependencies/{build_type}","-S",".",f"-DCMAKE_BUILD_TYPE={build_type}",
                 "-G","Visual Studio 17 2022","-A","x64",f"-DCMAKE_INSTALL_PREFIX=Packages/{build_type}",
                 "-D","GLSLANG_ENABLE_INSTALL=ON"])
    run_command(["cmake","--build",f"Build/NoDependencies/{build_type}","--config",build_type])
    run_command(["cmake","--install",f"Build/NoDependencies/{build_type}","--config",build_type])
    os.chdir(cwd)
def build_libpng(build_type:str):
    cwd= os.getcwd()
    os.chdir("..")
    run_command(["cmake","-B",f"Build/libpng/{build_type}","-S","libpng",f"-DCMAKE_BUILD_TYPE={build_type}",
                 "-G","Visual Studio 17 2022","-A","x64",f"-DCMAKE_INSTALL_PREFIX=Packages/{build_type}",
                 "-D","CMAKE_POSITION_INDEPENDENT_CODE=ON",
                 "-D","PNG_TESTS=OFF",
                 "-D","PNG_STATIC=ON",
                 "-D","CMAKE_PREFIX_PATH="+os.path.abspath(f"Packages/{build_type}")])
    run_command(["cmake","--build",f"Build/libpng/{build_type}","--config",build_type])
    run_command(["cmake","--install",f"Build/libpng/{build_type}","--config",build_type])
    os.chdir(cwd)
os.system("chcp 65001>nul")
build_no_dependencies("Debug")
build_libpng("Debug")
