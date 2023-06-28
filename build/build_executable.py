import os
import shutil
import subprocess


def build_executable():
    try:
        subprocess.run(["pyinstaller", "--onefile", "--distpath", "../executable","../src/main.py"], check=True)
        os.remove("main.spec")
        shutil.rmtree("build")

        print("Executable build completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during executable build: {e}")


if __name__ == "__main__":
    build_executable()
