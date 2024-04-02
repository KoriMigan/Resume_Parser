# Resume Parser

This project is a resume parser whoch extracts the contact information such as the candidates names, phone numbers and their email addresses from their resumes whether it be in PDF, text or Word docs format. The extracted data is then saved as a CSV file for easy access and analysis.

## Features

* Parse resumes in PDF, text or docs format.
* Exract candidate names, phone numbers and email addresses using regular expressions.
* Save extracted contact information to a CSV file.
* Handle variations in resume formatting and layout.
* Provide error handling mechanisms for parsing failures.
* Test the parser with a diverse set of sample resumes.

## Installation

To run the resume parser, ensure you have Python installed. Clone this repository and install the required dependencies using the following command:

`pip install -r requirements.txt`

## Usage

1. Create a 'sample_resumes' directory and move into it by running commands below:

   `mkdir sample_resumes`

   `cd sample_resumes`
2. Run the 'app.py' script to parse the resumes and extract contact information.

   `python app.py`
3. The parsed data will be saved to a CSV file named 'Contact_information.csv' in the project directory.

## Project Structure

* 'app.py': Main script for parsing the resumes and saving the contact information to CSV.
* '.gitignore': File that contains sensitive information extracted from the sample_resumes file after extraction not tracked.
* 'requirements.txt': File listing the required Python dependencies for the project.
* 'README.md': Documentation file providing instructions and information about the project.
* 'LICENSE.md': Documentation containing MIT license for project.

## Dependencies

* 'pdfplumber': Library for extracting text from PDF files.
* 'python-docx': Library for extracting text from DOCX files.

## Contributing

Contributions are welcome! If you ahve suggestions, feature requests or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
