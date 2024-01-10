# RemoveText Script

The RemoveText script is a Python tool that allows you to remove a specified text string from the names of files in the same directory as the script.

## Usage

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/adrianwez/remove-text.git
    cd remove-text
    ```

2. **Run the Script:**
    ```bash
    python RemoveText.py
    ```

3. **Enter the Text to Be Removed:**
    - The script will prompt you to enter the text that you want to remove from the file names.

4. **Review the Renamed Files:**
    - The script will go through the files in the same directory and remove the specified text from their names. It will print the old and new file names.

5. **Exit the Script:**
    - After processing the files, press Enter to exit the script.

## Example

Let's say you have the following files in your directory:

- `example_file_1.txt`
- `example_file_2.txt`
- `example_file_3.txt`

You run the script and enter `file_` as the text to be removed. The script will then rename the files as follows:

- `example_1.txt`
- `example_2.txt`
- `example_3.txt`

## Note

- Make sure to run the script in the same directory where your files are located.

- Be cautious when using this script, as it will modify file names in the current directory.

- Always review the changes before confirming the removal of text from file names.

Feel free to customize the script to suit your specific use case!
