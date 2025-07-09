cd ..
cmake  -B Build -S .    -DCMAKE_BUILD_TYPE=Debug -G "Visual Studio 17 2022" -A x64   -DCMAKE_INSTALL_PREFIX=Packages -DGLSLANG_ENABLE_INSTALL=ON
cmake  -B DummyBuild -S .   -DCMAKE_EXPORT_COMPILE_COMMANDS=on -DCMAKE_BUILD_TYPE=Debug -G Ninja -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_C_COMPILER=clang 
cp DummyBuild/compile_commands.json .
cd Scripts
pause