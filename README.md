# How many panels?

### This interactive simple scripts allows to computes the maximum number of rectangular panels that can fit inside a rectangular roof (without overlap)

### Constrains
- Panels must be axis-aligned (no diagonal placement)
- Panels cannot overlap
- Panels must be fully inside the roof
- Panels may be rotated (width ↔ height)
- No cutting or deformation of panels

## Code
### The code is intentionally divided in three files just for better readability, where:
__1.__ `main.py`
- Application entry point

__2.__ `scripts.py`
- Logic

__3.__ `utils.py`
- Helper functions

__4.__ `testa/test.py`
- Running aside cases (testing)

## Solution
### The code evaluates two mixed-orientation layouts and selects the best result, where ...
1. __Base Grid Placement__

    Panels are first placed in a regular grid using a single orientation
    - Normal orientation (width × height)
    - Rotated orientation (height × width)

2. __Leftover Space Utilization (Mixed Orientation)__

    After placing the base grid, unused space remains in the form of rectangular strips
    - __Right strip:__ unused width × full roof height
    - __Top strip:__ used width × unused height

    >The algorithm attempts to place rotated panels inside these leftover strips to increase the total count

3. __Both Orientations Are Tested__

    Two layouts are evaluated, where the return value is the maximum result of both layouts
    
    - Normal panels as base + rotated panels in leftovers
    - Rotated panels as base + normal panels in leftovers

## Execution

> For only __testing purposes__, run the next command
```
python -m tests.test
```

> To execute the __original script__ you just need to run the next command and type the dimensions (roof & panel)
```
python main.py
```