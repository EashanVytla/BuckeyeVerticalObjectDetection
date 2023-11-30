import re

#CHANGE THIS TO THE DIRECTORY OF THE UNITY PROJECT        
#C:\Data\Buckeye Vertical\BV-Domain-Randomization-Unity-Project\Assets\Resources
strDirectory = 'C:\Data\Buckeye Vertical\BV-Domain-Randomization-Unity-Project\Assets\Resources\Images\\'
strDirectoryMaterials = 'C:\Data\Buckeye Vertical\BV-Domain-Randomization-Unity-Project\Assets\Resources\Images\Materials\\'
def replace_guid(filename, mat_name, new_guid):
    f = open(strDirectoryMaterials + "0.mat", "r")
    copy = open(filename, "w")  # added x since we're creating a new file

    for line in f:
        if 'm_Texture: {fileID: 2800000, guid:' in line:
            copy.write('        m_Texture: {fileID: 2800000, guid: ' + new_guid + ', type: 3}\n')
        elif 'm_Name:' in line:
            copy.write('  m_Name: ' + mat_name + '\n')
        else:
            copy.write(line)
    f.close()
    copy.close()

def findGUID2(name):

    # open the text file for reading
    with open(strDirectory + name + ".png.meta", 'r') as file:
        # read the contents of the file into a string variable
        file_contents = file.read()
        print("here1")
        # search for the "guid:" in the file contents
        guid_start_index = file_contents.find("guid:")

        # if the "guid:" is found, extract the GUID and print it
        if guid_start_index != -1:
            guid_end_index = file_contents.find("\n", guid_start_index)
            guid = file_contents[guid_start_index + len("guid:"):guid_end_index]
            print("GUID found: " + guid)
            return guid
        else:
            print("No GUID found in the file.")
            return "-"

def create_textures():
    
    for i in range(48, 7791):
        try:
            temp_str = str(i)

            while len(temp_str) < 4:
                temp_str = "0" + temp_str

           
            guid = findGUID2(temp_str)

            replace_guid(strDirectoryMaterials + temp_str + ".mat", temp_str, guid)
        except:
            pass

create_textures()