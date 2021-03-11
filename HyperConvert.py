# Script by Steven Au
# Special thanks to the Pantab author!
# Converts a Tableau Hyper Data Export to a CSV file.
import pathlib as pl
import platform as pf

import pantab as pt
import pandas as pd


def monologue(func):
    """ Monologue Decorator"""
    def wrapped(*args, **kwargs):
        """ Wrapper per decorator"""
        print("You can choose to drag and drop a file path here!")
        print("Otherwise, if the paths are hard coded into this script, ")
        print("then do not type anything and simply just press enter")
        func(*args, **kwargs)
    return wrapped


class HyperConvert:
    """ Hyper Dataset conversion object."""

    def __init__(self, script_path=None, file_type='csv'):
        """ Initiator - all variables are optional"""
        self._script_path = script_path
        self._file_type = file_type

    def set_script_path(self, script_path):
        """ Sets the script path."""
        self._script_path = script_path

    def get_script_path(self):
        """ Returns the script path."""
        return self._script_path

    def set_file_type(self, file_type):
        """ Manually set the data file as desired."""
        self._file_type = file_type

    def library_pathing(self, some_file):
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
        new_filename = orig_file_path.stem + '.' + self._file_type

        directory_pathing = '/'
        if pf.system().lower() == 'windows':
            directory_pathing = '\\'

        new_export = parent_path + directory_pathing + new_filename

        return orig_file_path, new_export

    @monologue
    def path_choice(self):
        """ Output the files for conversion uses

            Returns:
                hyper_file:
                    Tableau Dataset path
                new_export:
                    Export dataset path
        """
        if self._script_path is not None:
            evaluate_file_path = self._script_path

        while True:
            try:
                dragged_file = input("Press enter to use the file path pre-set in this script\n> ")
                if len(dragged_file) != 0:
                    evaluate_file_path = dragged_file
                    self.set_script_path(dragged_file)  # Set the variable to the manually inputted file path.
                break
            except:
                print("Unfortunately, an error occurred. Perhaps you have quote marks. Delete those!")
                continue

        the_file, new_filename = self.library_pathing(evaluate_file_path)

        hyper_file = the_file
        new_export = new_filename

        return (hyper_file, new_export)

    def hyper_to_csv(self, hyper_file, csv_export):
        """ Primary method to convert a hyperfile's path to the CSV file's path.
            Conversion from tableauhyperapi table "Dictionary" to a Pandas Dataframe
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


if __name__ == "__main__":
    # If ran as a standalone.
    hc = HyperConvert()
    pathing = hc.path_choice()
    hc.hyper_to_csv(pathing[0], pathing[1])
