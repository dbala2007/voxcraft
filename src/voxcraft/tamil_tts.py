from datetime import datetime
from pathlib import Path
import wave

from piper import PiperVoice


class TamilTTS:
    def __init__(
        self,
        model_path: str = "models/piper-tamil/ta_IN-ValluvarNeural-medium.onnx",
    ):
        self.model_path = Path(model_path)

        if not self.model_path.exists():
            raise FileNotFoundError(
                f"Tamil voice model not found: {self.model_path}"
            )

        print("Loading Piper Tamil voice...")
        self.voice = PiperVoice.load(str(self.model_path))

    def generate(
        self,
        text: str,
        output_dir: str = "outputs",
    ) -> Path:

        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = output_path / f"tamil_{timestamp}.wav"

        with wave.open(str(file_path), "wb") as wav_file:
            self.voice.synthesize_wav(
                text,
                wav_file,
            )

        return file_path