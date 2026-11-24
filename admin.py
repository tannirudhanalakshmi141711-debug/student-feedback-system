# ---------------------------------
# ADMIN LOGIN
# ---------------------------------

elif menu == "🔐 Admin Login":

    st.subheader("Admin Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if username == "admin" and password == "1234":

            st.success("✅ Login Successful")

        else:

            st.error("❌ Invalid Credentials")