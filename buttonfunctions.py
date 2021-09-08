# Function for opening the 
# file explorer window
from tkinter import Text
from ltdl import get_title_all_methods
import re
import os
import time

def convertLinks(input_widg: Text, status_widg: Text, output_widg: Text):

    status_widg.delete("1.0",'end')
    status_widg.update_idletasks()
    output_widg.delete("1.0",'end')
    output_widg.update_idletasks()

    # Input Handler
    # Get range of text from line 1 char 0 till ending character minus the newline character that text boxes add by default.
    input_str = input_widg.get("1.0",'end-1c')
    lines = input_str.split("\n")

    # Driver Code
    inf_lines = lines

    status_widg.insert("end", "Input taken in.")

    output_lines = []

    total_links = len(inf_lines)
    link_counter = 1
    status_widg.insert("end", "\nAttempting to process %d lines." % (total_links))
    status_widg.update_idletasks()
    for line in inf_lines:
        line=line.rstrip()
        # The search() function returns a Match object:
        matches = re.search("^(https:\/\/)", line)
        if matches:
            url = line
            if url == "" :
                continue
            
            
            # Get title
            title_final = get_title_all_methods(url)

            dkline = "[[" + url + "|" + title_final + "]] \\\\"
            # TODO: Add timer to pause iff used
            time.sleep(0.5)
        else:
            dkline = line
        
        output_lines.append(dkline)

        status_widg.insert("end", "\nLine %d/%d processed." % (link_counter,total_links))
        status_widg.see('end')
        link_counter += 1
        status_widg.update_idletasks()

    # Output
    for output_line in output_lines:
        output_widg.insert("end", "%s\n" % output_line)

# TODO: Convert to exe with installer