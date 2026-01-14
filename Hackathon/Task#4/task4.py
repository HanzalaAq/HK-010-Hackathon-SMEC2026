import streamlit as st
import requests
st.set_page_config(page_title="Shopping Cart")
if "cart" not in st.session_state:
    st.session_state.cart = {}
st.title("shopping Cart")
response = requests.get("https://fakestoreapi.com/products")
products = response.json()
st.subheader("Products")
for product in products:
    st.write(product["title"])
    st.write("price:", product["price"])

    if st.button("Addto Cart", key=product["id"]):
        if product["id"] in st.session_state.cart:
            st.session_state.cart[product["id"]]["qty"] += 1
        else:
            st.session_state.cart[product["id"]] = {
                "title": product["title"],
                "price": product["price"],
                "qty": 1
            }
st.divider()
st.subheader("Cart")
total = 0
for pid in list(st.session_state.cart.keys()):
    item = st.session_state.cart[pid]
    col1, col2, col3, col4 = st.columns(4)
    col1.write(item["title"])
    col2.write(item["price"])
    qty = col3.number_input(
        "Qty",
        min_value=1,
        value=item["qty"],
        key=f"qty_{pid}"
    )
    st.session_state.cart[pid]["qty"] = qty

    if col4.button("Remove", key=f"remove_{pid}"):
        del st.session_state.cart[pid]
        st.rerun()
    total += item["price"] * item["qty"]
st.divider()
st.write("Total Amount:", total)
