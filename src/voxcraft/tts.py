from pathlib import Path

import soundfile as sf
from kokoro import KPipeline

from datetime import datetime


class KokoroTTS:
    def __init__(self, lang_code: str = "a"):
        print("Loading Kokoro...")
        self.pipeline = KPipeline(lang_code=lang_code)

    def generate(
        self,
        text: str,
        voice: str = "am_adam",
        speed: float = 0.85,
        output_dir: str = "outputs",
    ) -> list[Path]:

        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)

        generator = self.pipeline(
            text,
            voice=voice,
            speed=speed,
        )

        generated_files = []
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        for index, (_, _, audio) in enumerate(generator):
            file_path = output_path / f"speech_{timestamp}_{index}.wav"

            sf.write(
                file_path,
                audio,
                24000,
            )

            generated_files.append(file_path)

        return generated_files