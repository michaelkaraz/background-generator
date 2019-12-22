from os import path,listdir,walk,mkdir
from os.path import isfile, join
import sys   
from PIL import Image 

# grab first and second arg
try:
    _from = sys.argv[1]
    _to = sys.argv[2]
    _format = sys.argv[3]
except:
    _from = ''
    _to = ''
    _format = ''
# check is new / exist folder
class Converter():
    def __init__(self,folder_from,folder_to,format):
        self.folder_from = folder_from
        self.folder_to = folder_to
        self.folderExists = False
        self.format = format
        
    def _folder_exists(self):
        try:
            return path.exists(self.folder_to)
        except IOError as err:
            return False
    
    def _create_new_folder(self):
        try:
            mkdir(self.folder_to)
            print("Directory " , self.folder_to ,  " Created ")
            return True
        except FileExistsError as err:
            print("Directory " , self.folder_to ,  " Already exists ")
            return False
    
    def _get_file_list(self,from_path):
        try:
            return listdir(from_path)
        except IOError as err:
            return []
        
    
    def Run_Image_Converter(self):
        if(not self._folder_exists()):
            self._create_new_folder()
            
        for (dirpath, dirnames, filenames) in walk(self.folder_from):
            for filename in filenames:
                self._image_convert_processor(filename)
 
        return True
        
    def _image_convert_processor(self,filename):
        try:
            img = Image.open(f'{self.folder_from}\{filename}')
            new_file = path.splitext(filename)[0] + self.format
            img.save(f'{self.folder_to}\{new_file}.{self.format}')
        except:
            print("error")
            

        
    
        
# loop through pokedex
#convert to png
#save to new folder
def Main(pathFrom,pathTo,format):
    imgcnv = Converter(pathFrom,pathTo,format)
    imgcnv.Run_Image_Converter()

if __name__ == "__main__":
    if(len(_from) > 0 and len(_to) > 0) and len(_format) > 0:
       Main(_from,_to,_format)
    else:
       _from = input("Please provide a path from: ")
       _to = input("Please provide a path to: ")
       _format = input("Please provide a format type: ")
       Main(_from,_to,_format)