import streamlit as st

from voxcraft.tts import KokoroTTS
from voxcraft.tamil_tts import TamilTTS


@st.cache_resource
def load_tts():
    return KokoroTTS()


@st.cache_resource
def load_tamil_tts():
    return TamilTTS()


st.set_page_config(
    page_title="VoxCraft",
    page_icon="🎙️",
    layout="centered",
)

st.title("🎙️ VoxCraft")
st.caption("Local AI Text-to-Speech Studio")


# -------------------------
# Text Input
# -------------------------

text = st.text_area(
    "Enter text",
    placeholder="Type something you want VoxCraft to speak...",
    height=150,
)


# -------------------------
# Language Selection
# -------------------------

language = st.selectbox(
    "Language",
    options=[
        "English",
        "Tamil",
        "Tanglish (Coming Soon)",
    ],
)


# -------------------------
# English TTS
# -------------------------

if language == "English":

    voices = {
        "Adam — Male": "am_adam",
        "Heart — Female": "af_heart",
    }

    selected_voice = st.selectbox(
        "Voice",
        options=voices.keys(),
    )

    voice = voices[selected_voice]

    speed = st.slider(
        "Speech speed",
        min_value=0.5,
        max_value=1.5,
        value=0.85,
        step=0.05,
    )

    if st.button(
        "Generate Speech",
        type="primary",
        key="generate_english",
    ):

        if not text.strip():
            st.warning("Please enter some text.")

        else:
            with st.spinner("Generating English speech..."):

                tts = load_tts()

                files = tts.generate(
                    text=text,
                    voice=voice,
                    speed=speed,
                )

            st.success("English speech generated!")

            for file in files:

                st.audio(str(file))

                with open(file, "rb") as audio_file:
                    st.download_button(
                        label="Download WAV",
                        data=audio_file,
                        file_name=file.name,
                        mime="audio/wav",
                        key=f"download_english_{file.name}",
                    )


# -------------------------
# Tamil TTS
# -------------------------

elif language == "Tamil":

    if st.button(
        "Generate Speech",
        type="primary",
        key="generate_tamil",
    ):

        if not text.strip():
            st.warning("Please enter some Tamil text.")

        else:
            with st.spinner("Generating Tamil speech..."):

                tts = load_tamil_tts()

                file = tts.generate(
                    text=text,
                )

            st.success("Tamil speech generated!")

            st.audio(str(file))

            with open(file, "rb") as audio_file:
                st.download_button(
                    label="Download WAV",
                    data=audio_file,
                    file_name=file.name,
                    mime="audio/wav",
                    key=f"download_tamil_{file.name}",
                )


# -------------------------
# Tanglish
# -------------------------

else:
    st.info("Tanglish support is coming soon.")