from src import create_app
from pathlib import Path

static_folder = Path(__file__).parent.joinpath("static")

app = create_app(static_folder=static_folder)


def main():
    app.run()


if __name__ == "__main__":
    main()
