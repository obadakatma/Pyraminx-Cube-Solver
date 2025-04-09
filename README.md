# Pyraminx-Cube-Solver  
The Pyraminx Cube Solver is a Python program to solve the Pyraminx cube in the least amount of moves and uses a computer vision feature to input the colors of the cube. The project has been implemented on a Raspberry Pi 3B and uses a Raspberry Pi Camera V3 module.  
The program finds the solving state by searching backwards in a set of generated combinations of the Pyraminx cube.  

## Generating Combinations  
Run the code ["GenerateCombination.py"](https://github.com/obadakatma/Pyraminx-Cube-Solver/blob/main/GenerateCombination.py). It will create a JSON file that contains all 933,120 states starting from the solved state.  
The code uses the BFS algorithm to iterate over all possibilities, because the BFS algorithm works much better for finding the shortest path in these types of puzzles.  

## How to Run the Code  
To run the code without using the computer vision feature, run ["solve.py"](https://github.com/obadakatma/Pyraminx-Cube-Solver/blob/main/solve.py).  
To use the computer vision feature, run ["vision.py"](https://github.com/obadakatma/Pyraminx-Cube-Solver/blob/main/vision.py).  

## Project Video  
[![Pyraminx Solver Demo](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)
