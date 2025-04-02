import tkinter as tk
from tkinter import filedialog, messagebox
import xml.etree.ElementTree as ET
import os

def combine_kml_files_chronologically(file_paths):
    combined_kml = None
    combined_doc = None
    all_placemarks = []

    for file_path in file_paths:
        tree = ET.parse(file_path)
        root = tree.getroot()
        ns = {'ns': 'http://www.opengis.net/kml/2.2'}

        if combined_kml is None:
            combined_kml = ET.Element('kml', xmlns="http://www.opengis.net/kml/2.2")
            combined_doc = ET.SubElement(combined_kml, 'Document')

        placemarks = root.findall('.//ns:Placemark', ns)
        all_placemarks.extend(placemarks)

    for pm in all_placemarks:
        combined_doc.append(pm)

    return ET.ElementTree(combined_kml)

def save_combined_kml(tree, output_path):
    tree.write(output_path, encoding='utf-8', xml_declaration=True)

def main():
    root = tk.Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames(
        title="Select KML Files to Combine",
        filetypes=[("KML files", "*.kml")]
    )

    if not file_paths:
        messagebox.showinfo("No Files Selected", "No KML files were selected.")
        return

    output_path = filedialog.asksaveasfilename(
        title="Save Combined KML File As",
        defaultextension=".kml",
        filetypes=[("KML files", "*.kml")]
    )

    if not output_path:
        messagebox.showinfo("No Output File", "No output file was specified.")
        return

    try:
        combined_tree = combine_kml_files_chronologically(file_paths)
        save_combined_kml(combined_tree, output_path)
        messagebox.showinfo("Success", f"Combined KML file saved to:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

if __name__ == '__main__':
    main()