import re

# def main():

#     guid = findGUID()
#     replace_guid("C:\Data\Buckeye Vertical\Buckeye Vertical Dataset Creation\Assets\Resources\Images\Materials\\"+"0050.mat.meta", guid)
#     #if guid != "-":
        

def replace_guid(filename, new_guid):

    # with open(filename, 'w') as f:
    #     pass

    # with open(filename, 'r') as f:
    #     lines = f.readlines()

    # guid_count = 0
    # for i, line in enumerate(lines):
    #     # if 'guid:' in line:
    #     #     guid_count += 1
    #     #     if guid_count == 3:
    #     #         lines[i] = '        m_Texture: {fileID: 2800000, guid: ' + new_guid + ', type: 3}\n'
    #     #         break

    #     if 'm_Texture: {fileID: 2800000, guid:' in line:
    #         guid_count += 1
    #         if guid_count == 3:
    #             lines[i] = '        m_Texture: {fileID: 2800000, guid: ' + new_guid + ', type: 3}\n'
    #             break 

    # with open(filename, 'w') as f:
    #     f.writelines(lines)

    print("test 0")
    f = open("C:\\Data\\Buckeye Vertical\\Buckeye Vertical Dataset Creation\\Assets\\Resources\\Images\\Materials\\0.mat", "r")
    print("test: " + filename)
    copy = open(filename, "x")  # added x since we're creating a new file

    print("test 1")
    for line in f:
        if 'm_Texture: {fileID: 2800000, guid:' in line:
            print("test 2")
            copy.write('        m_Texture: {fileID: 2800000, guid: ' + new_guid + ', type: 3}\n')
        else:
            print("test 3")
            copy.write(line)
    f.close()
    copy.close()
        


# def findGUID():
#     # open the text file for reading
#     with open("C:\\Data\\Buckeye Vertical\\Buckeye Vertical Dataset Creation\\Assets\\Resources\\Images\\" + "1288.png.meta", 'r') as file:
#         # read the contents of the file into a string variable
#         file_contents = file.read()

#         # search for the "guid:" in the file contents
#         guid_start_index = file_contents.find("guid:")

#         # if the "guid:" is found, extract the GUID and print it
#         if guid_start_index != -1:
#             guid_end_index = file_contents.find("\n", guid_start_index)
#             guid = file_contents[guid_start_index + len("guid:"):guid_end_index]
#             print("GUID found: " + guid)
#             return guid
#         else:
#             print("No GUID found in the file.")
#             return "-"



def findGUID2(name):

    # open the text file for reading
    with open("C:\Data\Buckeye Vertical\BV-Domain-Randomization-Unity-Project\Assets\Resources\Images\\" + name + ".png.meta", 'r') as file:
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
            
   




def create_textures():
    for i in range(48, 3490):
        try:
            temp_str = str(i)

            while len(temp_str) < 4:
                temp_str = "0" + temp_str


            guid = findGUID2(temp_str)

            replace_guid("C:\\Data\\Buckeye Vertical\\Buckeye Vertical Dataset Creation\\Assets\\Resources\\Images\\Materials\\" + temp_str + ".mat", guid)
        except:
            pass

# main()

create_textures()