import streamlit as st
import math

def calculate_kvar(pf_before, pf_after, load_kw):
    s1 = load_kw / pf_before
    q1 = math.sqrt(s1**2 - load_kw**2)

    s2 = load_kw / pf_after
    q2 = math.sqrt(s2**2 - load_kw**2)

    return round(q1 - q2, 2)

def calculate_current(kvar, system_type, voltage):
    if system_type == "Single-phase (230V)":
        current = (kvar * 1000) / voltage
    else:
        current = (kvar * 1000) / (math.sqrt(3) * voltage)
    return round(current, 2)

# Streamlit UI
st.set_page_config(page_title="Capacitor Calculator", page_icon="⚡")

st.title("⚡ Capacitor Size & Current Calculator")
st.markdown("Calculate required capacitor rating (kVAR) and capacitor current based on your load & power factor.")

with st.form("input_form"):
    pf_before = st.number_input("Enter Current Power Factor", min_value=0.1, max_value=1.0, value=0.39, step=0.01)
    pf_after = st.number_input("Enter Desired Power Factor", min_value=0.1, max_value=1.0, value=0.95, step=0.01)
    load_kw = st.number_input("Enter Load (kW)", min_value=0.1, value=8.0, step=0.1)

    system_type = st.selectbox("System Type", ["Single-phase (230V)", "Three-phase (415V)"])
    submitted = st.form_submit_button("Calculate")

if submitted:
    voltage = 230 if system_type.startswith("Single") else 415

    kvar = calculate_kvar(pf_before, pf_after, load_kw)
    current = calculate_current(kvar, system_type, voltage)

    st.success("✅ Calculation Results:")
    st.write(f"🔹 **Required Capacitor Size**: `{kvar} kVAR`")
    st.write(f"🔹 **Capacitor Current** at `{voltage}V`: `{current} A`")

    st.info("💡 Tip: Choose the nearest standard capacitor bank size (like 16 or 17.5 kVAR), and use proper protection devices.")

