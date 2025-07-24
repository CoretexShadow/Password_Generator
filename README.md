# Password Generator

Welcome to the **Password Generator** project! This Python application allows you to generate secure passwords in two modes: a **command-line interface (CLI)** and an interactive **web-based GUI** powered by Streamlit. The project supports three types of password generation: Random Passwords, Memorable Passwords, and Pin Codes, each implemented as a class inheriting from a base `PasswordGenerator` class.

In this project, you will be expected to apply your knowledge of Streamlit and python to create a user-friendly dashboard interface for these password generators, or edit the password generators

## Features
- **RandomPasswordGenerator**: Generates a random password of a specified length, with optional inclusion of numbers and symbols.
- **MemorablePasswordGenerator**: Creates a password by combining a specified number of words from an English vocabulary (default: NLTK words corpus), with options for custom separators and random capitalization.
- **PinCodeGenerator**: Produces a numeric PIN of a specified length.
- **Two Interfaces**:
  - **CLI Mode**
  - **GUI Mode**

## Project Structure
```
password-generator/
├── src/
│   ├── MemorablePasswordGenerator.py
│   └── Random_Password_Generator.py
│   └── Pin_Generator.py
├── gui/
│   ├── Dashboard.py
└── README.md  # Project documentation
```

## Requirements
- **Python 3.7+**
- **Streamlit** for the GUI
- **NLTK** (Natural Language Toolkit) for word corpus
## Install dependencies using:
`pip install nltk streamlit `

## Download the NLTK 'words' corpus:
```python
 import nltk

nltk.download('words')
```
## Running the Project

Make sure you've installed all the required dependencies. You can then set your PYTHONPATH, navigate to the 'src' directory and run the project using Python:

```bash
export PYTHONPATH="${PYTHONPATH}:/your/path/to/main/directory"
cd src
python filename
```

Be sure to replace `/your/path/to/main/directory` with the actual path to the directory containing your project.

You can run the Streamlit web app using the following command:
```sh
streamlit run gui/Dashboard.py
```
This will run the web page at localhost. You can view this by opening your web browser and navigating to `http://localhost:8501/`.

# Contributing
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature).
3. Commit your changes (git commit -m "Add your feature").
4. Push to the branch (git push origin feature/your-feature).
5. Open a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for details.
