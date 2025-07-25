cmake_minimum_required(VERSION 3.14)
project(AetherDependencies)
set(CMAKE_CXX_STANDARD 23)
# 关闭严格别名和整数环绕优化
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    add_compile_options(-fno-strict-overflow -fno-strict-aliasing)
endif()
# 禁止cmake查找系统中安装的包，但是使用find_package(xx REQUIRED) 不指定CONFIG时 还是会从系统中查找包
# 需要使用find_package(xx REQUIRED CONFIG) 来从指定的目录中查找包
set(CMAKE_MODULE_PATH "") 
set( CMAKE_PREFIX_PATH  "${AETHER_DEPENDENCIES_PACKAGES_DIR}")#只从指定文件夹中查找包
add_subdirectory("glfw-3.4")
add_subdirectory("freetype")
add_subdirectory("glslang")
add_subdirectory("tinyxml2")
add_subdirectory("nativefiledialog")
add_subdirectory("lua-5.4.8")
add_subdirectory("miniaudio")
add_subdirectory("stb")
add_subdirectory("RectangleBinPack")
add_subdirectory("fribidi")
add_subdirectory("harfbuzz")