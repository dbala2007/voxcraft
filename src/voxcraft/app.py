import streamlit as st

from voxcraft.tts import KokoroTTS

@st.cache_resource
def load_tts():
    return KokoroTTS()

st.set_page_config(
    page_title="VoxCraft",
    page_icon="🎙️",
    layout="centered",
)

st.title("🎙️ VoxCraft")
st.caption("Local AI Text-to-Speech Studio")

text = st.text_area(
    "Enter text",
    placeholder="Type something you want VoxCraft to speak...",
    height=150,
)

language = st.selectbox(
    "Language",
    options=[
        "English",
        "Tamil (Coming Soon)",
        "Tanglish (Coming Soon)",
    ],
)

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

    if st.button("Generate Speech", type="primary"):

        if not text.strip():
            st.warning("Please enter some text.")

        else:
            with st.spinner("Generating speech..."):

                tts = load_tts()

                files = tts.generate(
                    text=text,
                    voice=voice,
                    speed=speed,
                )

            st.success("Speech generated!")

            for file in files:
                st.audio(str(file))

                with open(file, "rb") as audio_file:
                    st.download_button(
                        label="Download WAV",
                        data=audio_file,
                        file_name=file.name,
                        mime="audio/wav",
                    )

else:
    st.info(
        f"{language} support is coming soon. "
        "We will add a dedicated Indian-language TTS engine."
    )