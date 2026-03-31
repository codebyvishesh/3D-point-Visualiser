#  3D Point Reflection Across a Plane Visualizer

##  Overview
This Python project calculates and visually represents the reflection of an arbitrary three-dimensional point, $P(x, y, z)$, across a general plane defined by the equation $ax + by + cz + d = 0$. The script takes the point coordinates and the plane coefficients as input, computes the reflected point $P'(x', y', z')$, and generates an interactive 3D plot to demonstrate the geometric relationship. The project aligns with concepts from Analytical Geometry and Visualization (Simulation or visualization).

##  Features
* **Calculation Module:** Accurately computes the reflected point $P'$ using the vector geometry formula derived from the point-plane relationship.
* **Input/Output Structure:** Clear command-line prompts for receiving the point coordinates and plane coefficients[cite: 22].
* **Error Handling:** Implements robust validation to check for non-numerical inputs and handles the case where the plane coefficients $a, b, c$ are all zero, which does not define a valid reflection plane[cite: 54, 41].
* **3D Visualization Module:** Generates an interactive 3D plot [cite: 31] showing:
    * The **Original Point** (Blue)
    * The **Reflected Point** (Red)
    * The **Reflection Plane** (Green semi-transparent surface)
    * A dashed line connecting $P$ to $P'$.

##  Technologies/Tools Used
**Language:** Python 3.13 
* **Libraries:**
    * `numpy`: Used for efficient numerical operations and creating the mesh grid for the plane plot.
    * `matplotlib`: Specifically `mpl_toolkits.mplot3d` for rendering the geometric visualization.

##  Steps to Install & Run the Project

### 1. Prerequisites
Ensure you have Python 3 installed on your system.

### 2. Install Dependencies
This project requires the `matplotlib` and `numpy` libraries. Install them using pip:
```bash
pip install matplotlib numpy
