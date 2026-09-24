from run_command import run_command
import os
import platform
import shutil
import subprocess


def physical_core_count():
    system = platform.system()
    if system == "Windows":
        output = subprocess.check_output(
            ["powershell", "-NoProfile", "-Command",
             "(Get-CimInstance Win32_Processor | Measure-Object NumberOfCores -Sum).Sum"],
            text=True,
        )
        return int(output.strip())
    if system == "Darwin":
        return int(subprocess.check_output(["sysctl", "-n", "hw.physicalcpu"], text=True).strip())
    if system == "Linux":
        output = subprocess.check_output(["lscpu", "-p=SOCKET,CORE"], text=True)
        return len({line for line in output.splitlines() if line and not line.startswith("#")})
    raise RuntimeError(f"Cannot determine physical CPU cores on {system}")


PARALLEL_JOBS = str(physical_core_count())



def build_no_dependencies(build_type:str):
    cwd= os.getcwd()
    os.chdir("..")
    run_command(["cmake","-B",f"Build/NoDependencies/{build_type}","-S","Repos",f"-DCMAKE_BUILD_TYPE={build_type}",
                 f"-DCMAKE_INSTALL_PREFIX=Packages/{build_type}",
                 "-D","GLSLANG_ENABLE_INSTALL=ON"])
    run_command(["cmake","--build",f"Build/NoDependencies/{build_type}","--config",build_type,"--parallel",PARALLEL_JOBS])
    run_command(["cmake","--install",f"Build/NoDependencies/{build_type}","--config",build_type])
    os.chdir(cwd)
def build_libpng(build_type:str):
    cwd= os.getcwd()
    os.chdir("..")
    run_command(["cmake","-B",f"Build/libpng/{build_type}","-S","Repos/libpng",f"-DCMAKE_BUILD_TYPE={build_type}",
                 f"-DCMAKE_INSTALL_PREFIX=Packages/{build_type}",
                 "-D","CMAKE_POSITION_INDEPENDENT_CODE=ON",
                 "-D","PNG_TOOLS=OFF",
                 "-D","PNG_TESTS=OFF",
                 "-D","PNG_STATIC=ON",
                 "-D","PNG_SHARED=OFF",
                 "-D","CMAKE_PREFIX_PATH="+os.path.abspath(f"Packages/{build_type}"),
                 "-D","PNG_LIBCONF_HEADER="+os.path.abspath("Repos/libpng/pnglibconf.h.prebuilt")
                 ])
            
    run_command(["cmake","--build",f"Build/libpng/{build_type}","--config",build_type,"--parallel",PARALLEL_JOBS])
    run_command(["cmake","--install",f"Build/libpng/{build_type}","--config",build_type])
    os.chdir(cwd)
def build_lib(name:str,build_type:str,source_dir:str,options:list[str]):
    cwd=os.getcwd()
    os.chdir("..")

    command=["cmake","-B",f"Build/{name}/{build_type}","-S",source_dir,f"-DCMAKE_BUILD_TYPE={build_type}"]
    for option in options:
        command.append(option)
    run_command(command)
    run_command(["cmake","--build",f"Build/{name}/{build_type}","--config",build_type,"--parallel",PARALLEL_JOBS])
    run_command(["cmake","--install",f"Build/{name}/{build_type}","--config",build_type])
    os.chdir(cwd)

def build_msdfgen(build_type:str):
    options=[
        "-DMSDFGEN_CORE_ONLY=ON",
        "-DMSDFGEN_USE_VCPKG=OFF",
        "-DCMAKE_BUILD_TYPE=Debug",
        f"-DCMAKE_INSTALL_PREFIX=Packages/{build_type}",
        "-DMSDFGEN_INSTALL=ON",
        "-DMSDFGEN_USE_SKIA=OFF",
        "-DMSDFGEN_DYNAMIC_RUNTIME=ON",
    ]
    build_lib("msdfgen",build_type,"Repos/msdfgen",options)
def build_zlib(build_type:str):
    options=[
        f"-DCMAKE_BUILD_TYPE={build_type}",
        f"-DCMAKE_INSTALL_PREFIX=Packages/{build_type}",
        "-DZLIB_ENABLE_TESTS=OFF",
        "-DZLIB_ENABLE_EXAMPLES=OFF",
        "-DBUILD_SHARED_LIBS=OFF",
    ]
    build_lib("zlib",build_type,"Repos/zlib",options)


def build_sdl(build_type:str):
    options=[
        f"-DCMAKE_BUILD_TYPE={build_type}",
        f"-DCMAKE_INSTALL_PREFIX=Packages/{build_type}",
        "-DSDL_MSVC_STATIC_RUNTIME=ON",
        "-DSDL_LIBC=ON",
        "-DSDL_STATIC=ON",
        "-DSDL_SHARED=OFF",
        "-DSDL_TESTS=OFF",
        "-DSDL_TEST_LIBRARY=OFF",
        "-DSDL_EXAMPLES=OFF",
        "-DSDL_INSTALL=ON",
        "-DCMAKE_DEBUG_POSTFIX=d"
    ]
    build_lib("sdl",build_type,"Repos/SDL",options)

def build_JoltPhysics(build_type:str):
    options=[
        f"-DCMAKE_BUILD_TYPE={build_type}",
        f"-DCMAKE_INSTALL_PREFIX=Packages/{build_type}",
        "-DTARGET_UNIT_TESTS=OFF",
        "-DTARGET_HELLO_WORLD=OFF",
        "-DTARGET_PERFORMANCE_TEST=OFF",
        "-DTARGET_SAMPLES=OFF",
        "-DTARGET_VIEWER=OFF",
        "-DDOUBLE_PRECISION=ON",
    ]

    build_lib("JoltPhysics",build_type,"Repos/JoltPhysics/Build",options)


def build_tinyexr(build_type:str):
    cwd=os.getcwd()
    os.chdir("..")
    try:
        run_command(["make",f"--jobs={PARALLEL_JOBS}","-C","Repos/tinyexr","lib"])

        package_dir=os.path.join("Packages",build_type,"tinyexr")
        include_dir=os.path.join(package_dir,"include")
        lib_dir=os.path.join(package_dir,"lib")
        os.makedirs(include_dir,exist_ok=True)
        os.makedirs(lib_dir,exist_ok=True)

        for header in ("exr.h","exr_gpu.h","exr_vk.h"):
            shutil.copy2(os.path.join("Repos/tinyexr","include",header),include_dir)
        shutil.copy2("Repos/tinyexr/build/libtinyexr3.a",lib_dir)
    finally:
        os.chdir(cwd)

if platform.system() == "Windows":
    os.system("chcp 65001>nul")
build_no_dependencies("Debug")
build_zlib("Debug")
build_libpng("Debug")
build_msdfgen("Debug")
build_sdl("Debug")
build_JoltPhysics("Debug")
build_tinyexr("Debug")
