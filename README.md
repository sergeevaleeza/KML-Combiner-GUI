# 📜 KML Combiner GUI

A simple Python desktop tool to combine multiple KML files into one, maintaining chronological order of Placemarks. Built with `tkinter` for an easy file-picking experience.

---

## Features

- 📁 Select multiple `.kml` files from your computer  
- 📌 Merges all `<Placemark>` entries into a single KML file  
- 🗽 Retains original order (as selected by the user)  
- 💾 Save your combined KML to a new file  
- ❌ Simple error handling and user-friendly GUI dialogs

---

## How It Works

This tool:
1. Opens a file dialog to select multiple `.kml` files  
2. Parses and collects all `<Placemark>` elements  
3. Creates a new combined KML structure  
4. Prompts for a save location  
5. Writes the combined file to disk

---

## Requirements

- Python 3.x  
- No external packages required — uses built-in `tkinter` and `xml.etree.ElementTree`

---

## Usage

```bash
python combine_kml_gui.py
```

Then just follow the file dialogs to:
1. Select your KML files  
2. Choose where to save the combined output

---

## License

This project is open-source and free to use under the MIT License.

