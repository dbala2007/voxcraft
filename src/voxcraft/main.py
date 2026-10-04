import argparse

from voxcraft.tts import KokoroTTS


def main():
    parser = argparse.ArgumentParser(
        description="VoxCraft - AI Text-to-Speech"
    )

    parser.add_argument(
        "text",
        help="Text to convert to speech",
    )

    parser.add_argument(
        "--voice",
        default="am_adam",
        help="Kokoro voice to use",
    )

    parser.add_argument(
        "--speed",
        type=float,
        default=0.85,
        help="Speech speed",
    )

    args = parser.parse_args()

    tts = KokoroTTS()

    files = tts.generate(
        text=args.text,
        voice=args.voice,
        speed=args.speed,
    )

    for file in files:
        print(f"Generated: {file}")


if __name__ == "__main__":
    main()