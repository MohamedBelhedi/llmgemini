import google.generativeai as genai
import streamlit as st
from PIL import Image

response = ''

def ChatPrompt(api_key, user_input):
    global response
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-1.5-flash')

    # Übergabe des Bildes als PIL.Image.Image Objekt
    response = model.generate_content([user_input])
    return response.text

def ImagePropmt(api_key, user_input, image):
    global response
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-1.5-flash')

    # Übergabe des Bildes als PIL.Image.Image Objekt
    response = model.generate_content([user_input, image])
    return response.text

def main():
    st.title("Bildanalyse und Chatbot")

    api_key = st.text_input(label='API Key', type='password')
    user_input = st.text_input(label='Chat')
    pic = st.camera_input('Fotoaufnahme')
    if st.button(label='ChatPrompt'):
        if api_key and user_input:
            # Sende das Bild und die Benutzereingabe an das Modell
            chat_response = ChatPrompt(api_key, user_input)
            st.write(chat_response)
    output_image = None
    if pic is not None:
        image = Image.open(pic)
        output_image = image
        st.image(image, caption='Aufgenommenes Bild', use_column_width=True)

        if st.button(label='Chat'):
            if api_key and user_input:
                # Sende das Bild und die Benutzereingabe an das Modell
                chat_response = ImagePropmt(api_key, user_input, image)
                st.write(chat_response)
                if output_image:  # Zeige das Bild erneut an, falls verfügbar
                    st.image(output_image, caption='Aufgenommenes Bild', use_column_width=True)
            else:
                st.warning("Es fehlt dein API Key oder deine Chat-Nachricht.")
    else:
        st.write("Bitte gib mir ein Bild, damit ich dir sagen kann, was ich darauf sehe! 🖼️")

if __name__ == '__main__':
    main()
