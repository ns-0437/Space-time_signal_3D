import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.markdown("<h1 style='text-align: center; color: lightskyblue;'>3D Representation of EM Waves "
                    "</h1>", unsafe_allow_html=True)
with st.form("my_form"):
    st.write("Inside the form")
    frequency = st.slider("Frequency:-")
    amplitude = st.slider("Amplitude:-")
    phase = st.slider("Phase:-")
    wavelength = st.slider("Wavelength:-")
#    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        x = np.linspace(0, 10, 100)  # spatial range in meters
        t = np.linspace(0, 1, 100)  # temporal range in seconds

        # Create a meshgrid
        X, T = np.meshgrid(x, t)

        # Calculate the wavefunction
        k = 2 * np.pi / wavelength
        omega = 2 * np.pi * frequency
        wavefunction = amplitude * np.sin(k * X - omega * T + phase)

        # Create a 3D plot
        fig = go.Figure(data=[go.Surface(z=wavefunction, x=t, y=x)])
        fig.update_layout(scene=dict(xaxis_title='Time (s)', yaxis_title='Space (m)', zaxis_title='Wave Amplitude (V)'),
                          title='Electromagnetic Wave in 3D')
        st.plotly_chart(fig)
# st.write("Outside the form")