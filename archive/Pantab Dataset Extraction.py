# Script by Steven Au
# Special thanks to the Pantab author!
import pathlib as pl
import platform as pf

import pantab as pt
import pandas as pd

def script_path():
    # a decorator is possible here - for future refactoring
    """ Edit these paths accordingly - this can be used for debugging and testing purposes.
        Rather than setting this as a global variable, this is set as a local variable for further modular uses
    """
    SCRIPT_FILE_PATH = r'REDACTED FILE PATH'
    return SCRIPT_FILE_PATH

def pathing_library_mojo(some_file, file_convert='csv'):
    """ Parse the file string and extract all necessawry elements to breakdown and conert a file to a desired format name.
        Note: This function's purposes is only taking an input file and return the original path and newly converted file path
        Parameters:
            OPTIONAL File_convert
                csv is the default file extension. For any other file extensions, just add what is needed
                Note:
                    Do not add a "." to any desired file extension when using this function
        Returns:
            orig_file_path:
                The direct file path like "c:"
            new_export:
                This is the new file name - default is CSV
        You need to import two standard libraries: pathlib and platform
            pathlib is the bread and butter of the function
            platform is just to check the operating system and perform a simple conversion
    """
    orig_file_path = pl.Path(some_file)
    parent_path = str(orig_file_path.parent)
    new_filename = orig_file_path.stem + '.' + file_convert

    directory_pathing = '/'
    if pf.system().lower() == 'windows':
        directory_pathing = '\\'

    new_export = parent_path + directory_pathing + new_filename

    return orig_file_path, new_export


def path_choice():
    """ Output the files for conversion uses
    
        Returns:
            hyper_file:
                Tableau Dataset path
            new_export:
                Export dataset path
    """
    monologue()
    while True:
        try:
            dragged_file = input("Press enter to use the file paths hard saved in this script\n> ")
            break
        except:
            print("Unfortunately, an error occured. Perhaps you have quote marks. Delete those!")
            continue
    if len(dragged_file) != 0:
        evaluate_file_path = dragged_file
    else:
        evaluate_file_path = script_path()

    the_file, new_filename = pathing_library_mojo(evaluate_file_path)

    hyper_file = the_file
    new_export = new_filename

    return hyper_file, new_export

def hyper_to_csv(hyper_file, csv_export):
    """ Conversion from tableauhyperapi table "Dictionary" to a Pandas Dataframe
        Parameters: 
            hyper_file:
                File path for the hyper file import
            csv_export:
                File path for the csv file export
        Steps:
            1. Load the hyper tables in aggregate via pantab's "frames" from hyper to bypass the need for knowing individual table names
            2. Run the dictionary items() and save the dataframe as a Pandas object
        
        Returns:
            df.to_csv(csv_export, index=None) 
                THe expected output to file path with no index, feel free to adjust as needed
    """
    hyperdb = pt.frames_from_hyper(hyper_file)
    for key, pandas_df in hyperdb.items():
        df = pandas_df
    return df.to_csv(csv_export, index=None) 

def monologue():
    print("You can choose to drag and drop a file path here!")
    print("Otherwise, if the paths are hard coded into this script, ")
    print("then do not type anything and simply just press enter")

def main():
    hyper_file, csv_export = path_choice()
    hyper_to_csv(hyper_file, csv_export)

if __name__ == "__main__":
    main()
