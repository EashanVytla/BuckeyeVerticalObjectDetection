import re

def main():
    guid = findGUID()
    replace_guid("C:\Data\Buckeye Vertical\Buckeye Vertical Dataset Creation\Assets\Resources\Images\Materials", guid)
    #if guid != "-":
        

def replace_guid(filename, new_guid):
    with open(filename, 'r') as f:
        lines = f.readlines()

    guid_count = 0
    for i, line in enumerate(lines):
        if 'guid:' in line:
            guid_count += 1
            if guid_count == 3:
                lines[i] = '        m_Texture: {fileID: 2800000, guid: ' + new_guid + ', type: 3}\n'
                break

    with open(filename, 'w') as f:
        f.writelines(lines) 

def findGUID():
    # open the text file for reading
    with open("C:\\Data\\Buckeye Vertical\\Buckeye Vertical Dataset Creation\\Assets\\Resources\\Images\\1288.png.meta", 'r') as file:
        # read the contents of the file into a string variable
        file_contents = file.read()

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

main()