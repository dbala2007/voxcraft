import torch
import soundfile as sf

from transformers import AutoTokenizer, VitsModel


MODEL_NAME = "facebook/mms-tts-tam"


def main():
    print("Loading Tamil tokenizer...")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    print("Loading Tamil TTS model...")

    model = VitsModel.from_pretrained(MODEL_NAME)

    text = "வணக்கம்! இது வாக்ஸ்கிராஃப்ட் தமிழ் குரல் சோதனை."

    print(f"Generating speech for: {text}")

    inputs = tokenizer(
        text,
        return_tensors="pt",
    )

    with torch.no_grad():
        output = model(**inputs).waveform

    audio = output.squeeze().cpu().numpy()

    output_file = "tamil_test.wav"

    sf.write(
        output_file,
        audio,
        model.config.sampling_rate,
    )

    print(f"Generated: {output_file}")
    print(f"Sample rate: {model.config.sampling_rate}")


if __name__ == "__main__":
    main()