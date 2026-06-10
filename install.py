import subprocess
import sys

def install_requirements(file_path):
    """
    Installs packages from a requirements.txt file. If a package fails to install,
    it installs the latest version of that package.
    """
    try:
        # Read the requirements.txt file
        with open(file_path, 'r') as file:
            packages = file.readlines()

        for package in packages:
            package = package.strip()
            if not package or package.startswith("#"):  # Skip empty lines and comments
                continue

            print(f"Installing {package}...")
            try:
                # Attempt to install the specified version of the package
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            except subprocess.CalledProcessError:
                print(f"Failed to install {package}. Attempting to install the latest version...")
                # Extract the package name (ignoring version constraints)
                pkg_name = package.split('==')[0] if '==' in package else package.split('<=')[0].split('>=')[0]
                try:
                    # Install the latest version of the package
                    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_name])
                except subprocess.CalledProcessError as e:
                    print(f"Failed to install {pkg_name}. Please check manually. Error: {e}")
        
        print("All packages processed.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Specify the path to your requirements.txt file
    requirements_file = "requirements.txt"
    install_requirements(requirements_file)