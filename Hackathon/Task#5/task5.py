import streamlit as st
import qrcode
from PIL import Image
import cv2
from pyzbar.pyzbar import decode
import tempfile

st.set_page_config(page_title="QR Friend Connect")
st.title("Friend Connection App")
st.write("Connect by scanning QR codes")
st.divider()
user_id = st.text_input("Enter Your User ID", placeholder="e.g. hanzala_123")
if user_id:
    st.subheader("your QR Code")

    qr = qrcode.make(user_id)
    qr.save("my_qr.png")

    st.image("my_qr.png", width=250)
    st.success("Share this QR code with your friend")
st.divider()
st.subheader("Scan Friend QR Code")

uploaded_file = st.file_uploader("Upload QR Image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name
    img = cv2.imread(temp_path)
    decoded_objects = decode(img)
    if decoded_objects:
        friend_id = decoded_objects[0].data.decode("utf-8")
        st.success(f"Connected with **{friend_id}**")
    else:
        st.error("QR Code not detected")
st.divider()

