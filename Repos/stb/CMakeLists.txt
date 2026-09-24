add_library(stb_vorbis STATIC
    src/stb/stb_vorbis.c
)
target_include_directories(stb_vorbis PUBLIC 
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src>
    $<INSTALL_INTERFACE:stb_vorbis/include>
)
add_library(stb_image_write STATIC
    src/stb/stb_image_write.c
)
target_include_directories(stb_image_write PUBLIC 
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src>
    $<INSTALL_INTERFACE:stb_image_write/include>
)

add_library(stb_image STATIC
    src/stb/stb_image.c
)
target_include_directories(stb_image PUBLIC 
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src>
    $<INSTALL_INTERFACE:stb_image/include>
)



# stb_vorbis 头文件
install(FILES "${CMAKE_CURRENT_SOURCE_DIR}/src/stb/stb_vorbis.h"
    DESTINATION stb_vorbis/include
)
install(FILES "${CMAKE_CURRENT_SOURCE_DIR}/src/stb/stb_vorbis.c"
    DESTINATION stb_vorbis/include
)

# stb_image_write 头文件
install(FILES "${CMAKE_CURRENT_SOURCE_DIR}/src/stb/stb_image_write.h"
    DESTINATION stb_image_write/include
)
# stb_image 头文件
install(FILES "${CMAKE_CURRENT_SOURCE_DIR}/src/stb/stb_image.h"
    DESTINATION stb_image/include
)


# 导出 stb_vorbis
set(MODULE_NAME stb_vorbis)
#==================install config=========================
install(TARGETS ${MODULE_NAME}
    EXPORT ${MODULE_NAME}Targets
    ARCHIVE DESTINATION ${MODULE_NAME}/lib
    LIBRARY DESTINATION ${MODULE_NAME}/lib
    RUNTIME DESTINATION ${MODULE_NAME}/bin
)

include(CMakePackageConfigHelpers)

# 2. 配置并生成 Config 文件
configure_package_config_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/CMake/${MODULE_NAME}Config.cmake.in"  # 需要你自己写
    "${CMAKE_CURRENT_BINARY_DIR}/${MODULE_NAME}Config.cmake"
    INSTALL_DESTINATION ${MODULE_NAME}/
)

# 3. 安装 Config  文件
install(FILES
    "${CMAKE_CURRENT_BINARY_DIR}/${MODULE_NAME}Config.cmake"
    DESTINATION ${MODULE_NAME}/
)

# 4. 安装导出 Targets
install(EXPORT ${MODULE_NAME}Targets
    FILE ${MODULE_NAME}Targets.cmake
    DESTINATION ${MODULE_NAME}
)



# 导出 stb_image
set(MODULE_NAME stb_image)
#==================install config=========================
install(TARGETS ${MODULE_NAME}
    EXPORT ${MODULE_NAME}Targets
    ARCHIVE DESTINATION ${MODULE_NAME}/lib
    LIBRARY DESTINATION ${MODULE_NAME}/lib
    RUNTIME DESTINATION ${MODULE_NAME}/bin
)

include(CMakePackageConfigHelpers)

# 2. 配置并生成 Config 文件
configure_package_config_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/CMake/${MODULE_NAME}Config.cmake.in"  # 需要你自己写
    "${CMAKE_CURRENT_BINARY_DIR}/${MODULE_NAME}Config.cmake"
    INSTALL_DESTINATION ${MODULE_NAME}/
)

# 3. 安装 Config  文件
install(FILES
    "${CMAKE_CURRENT_BINARY_DIR}/${MODULE_NAME}Config.cmake"
    DESTINATION ${MODULE_NAME}/
)

# 4. 安装导出 Targets
install(EXPORT ${MODULE_NAME}Targets
    FILE ${MODULE_NAME}Targets.cmake
    DESTINATION ${MODULE_NAME}
)


# 导出 stb_image_write
set(MODULE_NAME stb_image_write)
#==================install config=========================
install(TARGETS ${MODULE_NAME}
    EXPORT ${MODULE_NAME}Targets
    ARCHIVE DESTINATION ${MODULE_NAME}/lib
    LIBRARY DESTINATION ${MODULE_NAME}/lib
    RUNTIME DESTINATION ${MODULE_NAME}/bin
)

include(CMakePackageConfigHelpers)

# 2. 配置并生成 Config 文件
configure_package_config_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/CMake/${MODULE_NAME}Config.cmake.in"  # 需要你自己写
    "${CMAKE_CURRENT_BINARY_DIR}/${MODULE_NAME}Config.cmake"
    INSTALL_DESTINATION ${MODULE_NAME}/
)

# 3. 安装 Config  文件
install(FILES
    "${CMAKE_CURRENT_BINARY_DIR}/${MODULE_NAME}Config.cmake"
    DESTINATION ${MODULE_NAME}/
)

# 4. 安装导出 Targets
install(EXPORT ${MODULE_NAME}Targets
    FILE ${MODULE_NAME}Targets.cmake
    DESTINATION ${MODULE_NAME}
)
