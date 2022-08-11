# Introduction 
Python Dash is a framework for developing highly customisable front end apps that enable both user interaction and visualisation. 
This README file describes the code and basic structure of how a Python Dash app looks like. From this scaffold code, a Dash app can be further developed according to more specific needs.

## Basic layout, design philosophy
This scaffolding departs from the practical experience that GUI-based apps tend to require a lot of code and can thus quickly grow out of control.
Furthermore there is always the possibility that code dealing with layout (the GUI itself) gets intermingled with code dealing with callbacks (the behind-the-scenes functions determining the app's behaviour).
Therefore this scaffolding groups the app's code in the following file structure:

```
dash-template
├── app.py
├── assets
│   ├── formatting.css
│   ├── OGD prompt RGB.png
│   └── Any other image or formatting file
├── callbacks
│   ├── cb_basic_callbacks.py
│   ├── cb_gui_callbacks.py
│   └── Any other Python script containing callback functions
├── functions
│   ├── data_construction.py
│   └── Any other Python script containing generic functions
├── layout
│   ├── layout.py
│   ├── tab_contents.py
│   ├── table_contents.py
│   └── Any other Python script containing (combinations of) layout elements
├── Future: possibly files containing Python classes helpful for Dash
│   └── Any Python script containing Python classes
├── requirements.txt
└── Any other file/directory dealing with things not directly involving the app (gitignore, virtual environment, this very README)
```

The following components make up this file structure:
- **App.py**: the main file calling all other components of the app and the app itself
- **Other root files**: mainly files dealing with other things than the app, except for requirements.txt, which holds a list of Python modules that need to be installed for the Dash app to run properly
- **Callbacks**: callbacks are functions dealing with the behaviour of the app (changing the UI elements, or passing data down from UI elements to other parts of the app)
- **Functions**: purpose-written functions that can help in providing often executed functionality, such as creating options for checkboxes and dropdowns, or for processing and manipulating data
- **Layout**: a description of UI elements, where a layout file can be nested in other layout files, which are eventually caught in layout.py, which contains the main layout

In the future Python class files can be added to this structure, but currently this scaffolding does not have them.

The file structure described above provides a clear separation of functionalities in the app, and encourages developers to adhere to a modular style of developing. The philosophy of modular developing is that specific functionalities are coded in separate smaller files, rather than in huge megafiles with thousands of lines of code that are unclear and hard to maintain.
For example, in this scaffold the behaviour of GUI elements is determined by callback functions that have been put in their own script (cb_gui_callbacks.py)

## Guidance
All files present in this scaffolding are accompanied by comments describing components and their functionalities. This is especially true for callback function, with which beginning developers might be unfamiliar.

# Getting Started
To be able to use this scaffold or develop another Dash app, the following steps should be taken:
1. Install Python 3.9 onto your system
2. Clone the repo containing this scaffold (or any other Dash app) onto your system on a convenient location
3. Open the repo folder in Visual Studio Code and open the terminal in Visual Studio Code
4. In the terminal type the command ```python -m venv venv``` to create a virtual environment if it is not there yet
5. Activite the virtual environment through the terminal with the command ```.\venv\Scripts\activate```
6. Run the command ```pip install -r requirements.txt``` in the terminal so that the required Python modules are installed in the virtual environment
7. Select app.py and from the Visual Studio Code menu click Run > Run Without Debugging to start the app
8. In the terminal an URL is displayed: visit this URL to open the app in your browser
9. After using the app, close your browser, and deactivate the virtual environment using the ```deactivate``` command

# Build and Test
- When developing locally, follow the steps in the previous section to build and test newly added or altered code
- Azure DevOps pipelines and an Azure web app will be used to provide deployment to a production environment in the cloud

# Contribute
You can contribute to Dash apps by having the desire to learn Python and by having a chat with Mark Versteegh to look at possibilities.

# Further reading on Python Dash
This README and the scaffolding cannot even nearly explain all topics that are handy and necessary for developing Dash apps. The following links are must-reads for developing Dash apps:
- The [official Python Dash website](https://dash.plotly.com/), providing detailed documentation on all Dash components
- A site on [Dash's nephew Dash Bootstrap](https://dash-bootstrap-components.opensource.faculty.ai/), which provides more possibilities of controlling the layout of your app