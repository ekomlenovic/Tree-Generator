# Tree Generator

This program is a simple tree generator that allows you to visualize the directory structure of a selected folder. It creates a tree-like representation of folders and files within the chosen directory and displays it in a graphical user interface (GUI).

## Presentation of Script

The script provides a GUI using the Tkinter library. The main window of the program includes several buttons and a text area where the generated tree will be displayed. Here's an overview of the available buttons:

1. **Choose Folder:** Clicking this button opens a file dialog that allows you to select the folder for which you want to generate the tree.

2. **Copy to Clipboard:** This button copies the generated tree to the clipboard, allowing you to easily paste it into other applications.

3. **Clear:** Clicking this button clears the text area, removing any previously generated tree.

4. **Stop:** This button is initially disabled and becomes active during the generation process. It allows you to stop the tree generation if needed.

## How It Works

When you click the **Choose Folder** button, a file dialog opens, enabling you to select a folder. Once a folder is selected, the program starts generating the tree structure recursively using the `generate_tree()` function.

The `generate_tree()` function takes the selected folder path as a parameter and recursively traverses the directory structure. It prints each file and folder encountered in the console and inserts them into the text area in the GUI.

During the generation process, a progress bar is displayed, indicating the progress of tree generation. The progress bar updates as each file and folder is processed.

If you click the **Stop** button while the tree generation is in progress, it will interrupt the process and stop further generation.

Once the tree generation is complete, the program disables the progress bar, releases the window lock, and enables the buttons to choose another folder, copy the tree to the clipboard, or clear the text area.

## Installation 
### Source Code
1. Clone the repository or download the `tree_generator.py` script.
2. Make sure you have Python installed on your system.
3. Install the required dependencies using the following command:

``` 
pip install -r requirements.txt
```

### .exe (on windows)
Grab the latest version from the GitHub releases tab.  
Run it and enjoy.

## Usage

To use the Tree Generator:

1. Run the `tree_generator.py` script in a Python environment with the required dependencies.
2. Click the **Choose Folder** button to select a folder for which you want to generate the tree.
3. The generated tree will be displayed in the text area.
4. You can click the **Copy to Clipboard** button to copy the tree for later use.
5. If needed, click the **Clear** button to remove the generated tree from the text area.
6. During the tree generation process, you can click the **Stop** button to interrupt and stop further generation.

Note: The program may take some time to generate the tree structure for large folders, depending on the size and complexity of the directory.

Feel free to modify and enhance the program according to your specific requirements. Happy tree generation!

