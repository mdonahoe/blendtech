scripts for Blender
===================

###My understanding of how blender works


1. The blender renderer and game engine are written in C++ for speed.
    OpenGL is used for fast rendering,
    but I don't know what tools are used for photo-realistic rendering

2. Blender has a complicated user-interface of panels that can be reconfigured at will.
    I am frequently confused by it.

3. Blender has a python API, and bundles python3.3 with its own source.

4. I suspect the entire UI for blender is written in python

5. The Game Logic of blender has a Sensors -> Controllers -> Actuators -> Render loop.
    This is written in C++, with a python API.
    It supports hand-crafted games,
    but the visual interface seems limiting for dynmically generated simulations.
    I hope I can control it entirely from python.

6. The file format (.blend) is binary.
    I vaguely remember reading that it was desired for rapid serialization.


###Goals

1. grid of blocks
2. grid of blocks with heights set to a function
3. block simulation
4. clickable blocks?
5. attach to the live enviroment and write python while it is running
