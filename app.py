from src import create_app
from pathlib import Path

# Creating the path of the static folder
static_folder = Path(__file__).parent.joinpath("static")

# Creating the App instance with the static folder configuration
app = create_app(static_folder=static_folder)


def main():
    app.run()


if __name__ == "__main__":
    main()
