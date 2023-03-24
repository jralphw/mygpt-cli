# myGPT-py

This is a very simple command line application to get chat completions from OpenAI's `gpt-3.5-turbo` model

## Usage
### Using executable(Windows only)
**Required:** Valid OpenAI API key stored under `OPENAI_API_KEY` environment variable
Either add the executable **(Located in /dist)** to a folder accessible through `PATH` or run from executable folder with "`.\`" prefix.
Run : `mygpt "Your prompt"`
### With script
Prerequisites;
 - Python 3 (Preferably latest version)
 - Valid OpenAI API key stored under `OPENAI_API_KEY` environment variable
 - `openai` pip package installed
When in script directory, simply run `python mygpt.py "Your prompt"` (Windows) or `python3 mygpt.py "Your prompt"` (Linux/macOS)

## Ref
 - [OpenAI](https://openai.com)