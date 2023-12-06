# Differential Equation Solver App

This repository contains a Python script (`main.py`) that serves as an interactive app for solving ordinary differential equations (ODEs) using the `sympy` library. The app relies on a custom module (`module.py`), which includes a function called `solving_differential_equation` for solving ODEs.

#### Files

- **main.py**: The main Python script for the interactive differential equation solver app.
- **module.py**: Python module providing the `solving_differential_equation` function.
- **test.py**: Python script with tests for the functionality (optional).
- **Project.ipynb**: Jupyter Notebook demonstrating the usage and examples (optional).

#### Usage

1. **Running the App:**
    - Ensure that you have the necessary dependencies installed, including `sympy`.
    - Run the app using the command: `python main.py`.

2. **Using the App:**
    - Upon running the app, a welcome message is displayed, and the user enters a loop for continuous interaction.
    - The user is prompted to input the left-hand side and right-hand side of the differential equation.
    - Optionally, the user can provide initial conditions (y and x values). If not applicable, they can enter -1 for both.
    - The entered function and initial conditions are displayed for confirmation.
    - The script calls the `solving_differential_equation` function to solve the equation.
    - The solving techniques applicable to the equation and the resulting solution are displayed.

3. **Example Usage:**
    - For the differential equation `dy/dx = x**2`, enter `diff(f(x), x) = x**2` when prompted.
    - If initial conditions are applicable, enter the corresponding values when prompted.
    - The script will then display the solving techniques and the solution.

4. **Exiting the App:**
    - To exit the app, use the appropriate exit command provided by your environment (e.g., pressing Ctrl+C).

#### Dependencies

- Ensure you have the necessary dependencies installed, including `sympy`.

### Contributors
- Abdelrahman Khaled
