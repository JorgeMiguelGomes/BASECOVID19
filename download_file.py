from urllib.request import urlretrieve
import os # we want python to be able to read what we have in our hard drive


def download_file(file_link: str, output_file: str='file.csv'):
    """
    Downloads a file from an URL into your hard drive.
    
    Parameters
    ------------
    file_link: str
        A string containing the link to the file you wish to download.
    output_file: str
        A string containing the name of the output file. The default value is 'file.csv'
        at the location you are running the function.
        
    Returns
    ---------
    Nothing
    
    
    Example
    ---------
    download_file("https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip", output_file='student.zip')
    """
    
    # If file doesn't exist, download it. Else, print a warning message.
    if not os.path.exists(output_file):
        urlretrieve(file_link, filename=output_file)
    else:
        print("File already exists!")
 