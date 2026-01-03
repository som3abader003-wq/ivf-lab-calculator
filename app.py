import streamlit as st

st.title("IVF Lab Calculator 🧪")
st.caption("Simple daily lab calculators (no patient data).")

tool = st.selectbox(
    "Choose a calculator",
    [
        "Dilution Calculator (C1V1 = C2V2)",
        "Media / Plate Volume Calculator",
        "Percentage Solution Calculator (% w/v)"
    ],
)

st.divider()

# 1) Dilution: C1V1 = C2V2
if tool == "Dilution Calculator (C1V1 = C2V2)":
    st.subheader("Dilution Calculator (C1V1 = C2V2)")

    c1 = st.number_input("C1 (Stock concentration)", min_value=0.0, value=100.0, step=0.1)
    c2 = st.number_input("C2 (Desired concentration)", min_value=0.0, value=10.0, step=0.1)
    v2 = st.number_input("V2 (Final volume)", min_value=0.0, value=1.0, step=0.1)

    unit = st.selectbox("Units for volume", ["mL", "µL"])

    if st.button("Calculate Dilution"):
        if c1 <= 0 or c2 <= 0 or v2 <= 0:
            st.warning("Please enter values > 0.")
        elif c2 > c1:
            st.error("C2 cannot be greater than C1 (desired concentration cannot exceed stock).")
        else:
            v1 = (c2 * v2) / c1
            diluent = v2 - v1

            st.success("Results")
            st.write(f"**V1 (Stock volume)** = {v1:.4f} {unit}")
            st.write(f"**Diluent volume** = {diluent:.4f} {unit}")

            st.info("Tip: If you are working in µL, enter V2 in µL and results will be in µL.")

# 2) Media / Plate Volume
elif tool == "Media / Plate Volume Calculator":
    st.subheader("Media / Plate Volume Calculator")

    num_plates = st.number_input("Number of dishes / wells", min_value=1, value=10, step=1)
    vol_each = st.number_input("Volume per dish/well", min_value=0.0, value=0.5, step=0.1)
    unit = st.selectbox("Unit", ["mL", "µL"])
    extra_percent = st.number_input("Extra (%) for loss (recommended 5–15%)", min_value=0.0, value=10.0, step=1.0)

    if st.button("Calculate Total Volume"):
        total = num_plates * vol_each
        total_with_extra = total * (1 + extra_percent / 100)

        st.success("Results")
        st.write(f"**Total volume** = {total:.4f} {unit}")
        st.write(f"**Total + extra** = {total_with_extra:.4f} {unit}")

# 3) % w/v Solution
else:
    st.subheader("Percentage Solution Calculator (% w/v)")
    st.caption("w/v means grams per 100 mL.")

    percent = st.number_input("Desired % (w/v)", min_value=0.0, value=1.0, step=0.1)
    final_ml = st.number_input("Final volume (mL)", min_value=0.0, value=100.0, step=1.0)

    if st.button("Calculate grams needed"):
        if percent <= 0 or final_ml <= 0:
            st.warning("Please enter values > 0.")
        else:
            grams = (percent * final_ml) / 100
            st.success("Results")
            st.write(f"**Grams needed** = {grams:.4f} g")
            st.info("Example: 1% w/v = 1 g in 100 mL.")
