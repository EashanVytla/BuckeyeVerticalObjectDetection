import pyunity as pu
import os


    # for i in range(48, 3490):


    #     try:

    #         temp_str = str(i)

    #         while len(temp_str) < 4:
    #             temp_str = "0" + temp_str


    #         guid = findGUID2(temp_str)

    #         replace_guid("C:\Data\Buckeye Vertical\BV-Domain-Randomization-Unity-Project\Assets\Resources\Images\\Materials\\" + temp_str + ".mat.meta", guid)

    #     except:
    #         pass




# Load the image as a texture
texture = pu.files.Texture2D("0053.png")

# Create a new material
material = pu.StandardMaterial()
material.set_texture("_MainTex", texture)

# Create a GameObject and assign the material to it
game_object = pu.GameObject()
renderer = game_object.add_component(pu.MeshRenderer)
renderer.materials.append(material)

# You can also set other material properties if needed
material.set_color("_Color", pu.Color.red)

# Save the scene with the created object
pu.save("MyScene")

# Quit the application (optional)
pu.quit()