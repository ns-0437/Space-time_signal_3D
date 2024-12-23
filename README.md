
# 3D Representation of Electromagnetic Waves

This project visualizes the 3D representation of electromagnetic (EM) waves using Streamlit and Plotly. The application allows users to input parameters such as frequency, amplitude, phase, and wavelength to generate a dynamic 3D plot of the wave.

## Features
- **Interactive Inputs**: Customize wave parameters (frequency, amplitude, phase, wavelength) through an intuitive form.
- **3D Plotting**: Visualizes EM waves using Plotly's surface plot.
- **Dynamic Updates**: Generates the wave based on user input in real time.

## Requirements

- Python 3.9 or above
- `streamlit`
- `numpy`
- `plotly`

## Installation

1. **Clone the repository**:
   ```bash
   git clone <https://github.com/ns-0437/Space-time_signal_3D>
   cd <Space-time_signal_3D>
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python -m venv env
   source env/bin/activate # On Windows, use `env\\Scripts\\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

2. **Open the application**:
   - The application will open in your default web browser, or you can access it at `http://localhost:8501`.

3. **Interact with the application**:
   - Input the desired values for **frequency**, **amplitude**, **phase**, and **wavelength**.
   - Click the "Submit" button to generate the 3D visualization.

## File Structure

- `app.py`: Main Streamlit application file.
- `requirements.txt`: Python dependencies for the project.

## Parameters

- **Frequency**: Determines the oscillation rate of the wave.
- **Amplitude**: Sets the peak value of the wave.
- **Phase**: Adjusts the initial phase of the wave.
- **Wavelength**: Defines the spatial period of the wave.

## Visualization Details

The application computes and displays the wavefunction based on the formula:

\\[
Wavefunction = Amplitude \\times \\sin(kX - \\omega T + Phase)
\\]

Where:
- \\(k = \\frac{2\\pi}{\\text{wavelength}}\\) (wave number)
- \\(\\omega = 2\\pi \\times \\text{frequency}\\) (angular frequency)
- \\(X\\) is the spatial range
- \\(T\\) is the temporal range

The wave is visualized as a 3D surface plot with:
- **X-axis**: Time (seconds)
- **Y-axis**: Space (meters)
- **Z-axis**: Wave amplitude (volts)

## Example Output
The application generates a 3D surface plot of the electromagnetic wave based on the user-defined parameters.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue to discuss changes or new features.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- [Streamlit](https://streamlit.io/) for the interactive UI framework.
- [Plotly](https://plotly.com/python/) for the dynamic 3D plotting.
- [NumPy](https://numpy.org/) for numerical computations.
```
