import subprocess
import sys
import time


Testing=True

def install_all_packs():
    def install_package(package_name):
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
            print(f"Package '{package_name}' installed successfully.")
        except subprocess.CalledProcessError:
            print(f"Error installing package '{package_name}'.")

        if __name__ == "__main__":
            package_to_install = "tk"  
            install_package(package_to_install)

        if __name__ == "__main__":
            package_to_install = "pillow"  
            install_package(package_to_install)

if Testing==False:
     install_all_packs()

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk, ImageSequence

overviews=[
    """This is the stellar nursery. A nebula is a massive cloud
      of gas (mostly hydrogen) and dust.
      When a disturbance like a nearby supernova or collision of
        galaxies occurs, it causes regions within
        the nebula to collapse under their gravity.
      These collapsing regions form Protostars.""",

      """As a region within the nebula collapses,
        the material heats up and forms a protostar. It's like a star embryo.
        During this stage, the protostar continues to gather mass from its surroundings. 
        Eventually, it reaches a temperature where nuclear fusion can ignite in its core,
          transitioning it to the next stage.""",

        """This is the longest phase of a star's life, lasting billions of years.
            During this stage, the star is in hydrostatic equilibrium,
            meaning the outward pressure from nuclear fusion in the core balances
              the inward pull of gravity.
            Stars in this phase fuse hydrogen into helium in their cores.
            The mass of the star determines its lifespan in the main sequence;
            more massive stars burn through their fuel faster.""",

            """When a star exhausts the hydrogen in its core, fusion stops,
              and the core contracts while the outer layers expand.
              For medium-sized stars (like our Sun), they become red giants.
              Massive stars become red or blue supergiants.
              During this stage, the star begins fusing heavier elements
              in its core, like helium into carbon and oxygen.""",

              """After a medium-sized star like the Sun exhausts its fuel,
                it sheds its outer layers, creating a planetary nebula.
                The core that's left behind, now a white dwarf,
                is about the size of Earth but with a mass similar to the Sun.
                White dwarfs are incredibly dense.
                  They don't undergo nuclear fusion, but radiate leftover heat.
                    Over time, they cool and become dimmer.""",

                    """When a massive star (at least eight times the mass of the Sun)
                      depletes its nuclear fuel, its core collapses under gravity.
                      This causes an explosive ejection of the outer layers.""",
]



def resize_image(image, new_width):# This function was created by Mr Holzer
    current_width = image.size[0]
    current_height = image.size[1]

    new_height = int((new_width / current_width) * current_height)
    image = image.resize((new_width, new_height))
    return image

def cards(stage):
    root=tk.Tk()
    root.title(stage)
    root.geometry("900x650")

    if stage=="Nebula":
        image_path="Q:\\Projects\\Code\\Python\\Universe Creation project\\assets\\nebula.png"
    elif stage=="Protostar":
        image_path="Q:\\Projects\\Code\\Python\\Universe Creation project\\assets\\protostar.jpg"
    elif stage=="Main Sequence":
        image_path="Q:\\Projects\\Code\\Python\\Universe Creation project\\assets\\main sequence.jpg"
    elif stage=="Red Giant":
        image_path="Q:\\Projects\\Code\\Python\\Universe Creation project\\assets\\red giant.jpg"
    elif stage=="White Dwarf":
        image_path="Q:\\Projects\\Code\\Python\\Universe Creation project\\assets\\white dwarf.jpg"
    elif stage=="Supernova":
        image_path="Q:\\Projects\\Code\\Python\\Universe Creation project\\assets\\supernova.webp"

    if stage=="Nebula":
        slide_position=1
    elif stage=="Protostar":
        slide_position=2
    elif stage=="Main Sequence":
        slide_position=3
    elif stage=="Red Giant":
        slide_position=4
    elif stage=="White Dwarf":
        slide_position=5
    elif stage=="Supernova":
        slide_position=6

    Modular_star_image1 = Image.open(image_path) 
    Modular_star_image1 = resize_image(Modular_star_image1, 520) 
    Modular_star_image1 = ImageTk.PhotoImage(Modular_star_image1) 
    Modular_star_label_image1 = tk.Label(image=Modular_star_image1) 
    Modular_star_label_image1.grid(row=3,column=2)

    desk_pos= slide_position-1
    desk= overviews[desk_pos]

    stage_desk=tk.Label(font=("helvetica", 12), fg="black", bg="silver", text=desk)
    stage_desk.grid(row=5, column=2)

    star_name=tk.Label(font=("Helvetica", 22), fg="black", bg="silver", text=stage)
    star_name.grid(row=4, column=2)

    def back_cmd():
        time.sleep(0.2)
        root.destroy()
        time.sleep(0.2)
        startup_gui()

    def forward_cmd(num):
        time.sleep(0.2)
        root.destroy()
        time.sleep(0.2)
        if num==1:
            cards("Protostar")
        elif num==2:
            cards("Main Sequence")
        elif num==3:
            cards("Red Giant")
        elif num==4:
            cards("White Dwarf")
        elif num==5:
            cards("Supernova")
        elif num==6:
            cards("Nebula")

    def backward_cmd(num):
        time.sleep(0.2)
        root.destroy()
        time.sleep(0.2)
        if num==1:
            cards("Supernova")
        elif num==2:
            cards("Nebula")
        elif num==3:
            cards("Protostar")
        elif num==4:
            cards("Main Sequence")
        elif num==5:
            cards("Red Giant")
        elif num==6:
            cards("White Dwarf")


    back_button=tk.Button(font=("impact", 25), fg="red", bg="gray", text="Back", command=lambda: back_cmd())
    back_button.grid(row=1, column=1)
    
    forward_button=tk.Button(font=("impact", 20), fg="pink", bg="silver", text="Next", command=lambda: forward_cmd(slide_position))
    forward_button.grid(row=8, column=8)

    backward_button=tk.Button(font=("impact", 20), fg="pink", bg="silver", text="Previous", command=lambda: backward_cmd(slide_position))
    backward_button.grid(row=8, column=1)

    root.mainloop()

def startup_gui():
    root=tk.Tk()
    root.title("Universe Creation Project")
    root.geometry("1250x600")

    image_sizes=150

    def button_break(item):
        time.sleep(0.2)
        root.destroy()
        time.sleep(0.2)
        if item=="Nebula":
            print(item)
            cards("Nebula")
        elif item=="Protostar":
            print(item)
            cards("Protostar")
        elif item=="Main Sequence":
            print(item)
            cards("Main Sequence")
        elif item=="Red Giant":
            print(item)
            cards("Red Giant")
        elif item=="White Dwarf":
            print(item)
            cards("White Dwarf")
        elif item=="Supernova":
            print(item)
            cards("Supernova")


    menu_chunk1_image1 = Image.open(f"Q:\\Projects\\Code\\Python\\Universe Creation project\\assets\\menu chunks\\image1x1.png") 
    menu_chunk1_image1 = resize_image(menu_chunk1_image1, image_sizes) 
    menu_chunk1_image1 = ImageTk.PhotoImage(menu_chunk1_image1) 
    menu_chunk1_label_image1 = tk.Label(image=menu_chunk1_image1) 
    menu_chunk1_label_image1.grid(row=3,column=1)
    

    menu_chunk2_image1 = Image.open(f"Q:\\Projects\\Code\\Python\\Universe Creation project\\assets\\menu chunks\\image2x1.png") 
    menu_chunk2_image1 = resize_image(menu_chunk2_image1, image_sizes) 
    menu_chunk2_image1 = ImageTk.PhotoImage(menu_chunk2_image1) 
    menu_chunk2_label_image1 = tk.Label(image=menu_chunk2_image1) 
    menu_chunk2_label_image1.grid(row=3,column=2)

    menu_chunk3_image1 = Image.open(f"Q:\\Projects\\Code\\Python\\Universe Creation project\\assets\\menu chunks\\image3x1.png") 
    menu_chunk3_image1 = resize_image(menu_chunk3_image1, image_sizes) 
    menu_chunk3_image1 = ImageTk.PhotoImage(menu_chunk3_image1) 
    menu_chunk3_label_image1 = tk.Label(image=menu_chunk3_image1) 
    menu_chunk3_label_image1.grid(row=3,column=3)

    menu_chunk4_image1 = Image.open(f"Q:\\Projects\\Code\\Python\\Universe Creation project\\assets\\menu chunks\\image4x1.png") 
    menu_chunk4_image1 = resize_image(menu_chunk4_image1, image_sizes) 
    menu_chunk4_image1 = ImageTk.PhotoImage(menu_chunk4_image1) 
    menu_chunk4_label_image1 = tk.Label(image=menu_chunk4_image1) 
    menu_chunk4_label_image1.grid(row=3,column=4)


    menu_chunk5_image1 = Image.open(f"Q:\\Projects\\Code\\Python\\Universe Creation project\\assets\\menu chunks\\image5x1.png") 
    menu_chunk5_image1 = resize_image(menu_chunk5_image1, image_sizes) 
    menu_chunk5_image1 = ImageTk.PhotoImage(menu_chunk5_image1) 
    menu_chunk5_label_image1 = tk.Label(image=menu_chunk5_image1) 
    menu_chunk5_label_image1.grid(row=3,column=5)

    menu_chunk6_image1 = Image.open(f"Q:\\Projects\\Code\\Python\\Universe Creation project\\assets\\menu chunks\\image6x1.png") 
    menu_chunk6_image1 = resize_image(menu_chunk6_image1, image_sizes) 
    menu_chunk6_image1 = ImageTk.PhotoImage(menu_chunk6_image1) 
    menu_chunk6_label_image1 = tk.Label(image=menu_chunk6_image1) 
    menu_chunk6_label_image1.grid(row=3,column=6)

    menu_chunk7_image1 = Image.open(f"Q:\\Projects\\Code\\Python\\Universe Creation project\\assets\\menu chunks\\image7x1.png") 
    menu_chunk7_image1 = resize_image(menu_chunk7_image1, image_sizes) 
    menu_chunk7_image1 = ImageTk.PhotoImage(menu_chunk7_image1) 
    menu_chunk7_label_image1 = tk.Label(image=menu_chunk7_image1) 
    menu_chunk7_label_image1.grid(row=3,column=7)

#//////////////////////////////////////////////////////////////////////////////

    nebula_image1 = Image.open(f"Q:\\Projects\\Code\\Python\\Universe Creation project\\assets\\nebula.png") 
    nebula_image1 = resize_image(nebula_image1, image_sizes) 
    nebula_image1 = ImageTk.PhotoImage(nebula_image1) 
    nebula_label_image1 = tk.Label(image=nebula_image1) 
    nebula_label_image1.grid(row=1,column=1)

    nebula_label=tk.Button(font=("helvetica",12), bg="silver", fg="black", text="Nebula", command=lambda: button_break("Nebula"))
    nebula_label.grid(row=2, column=1)
    
    protostar_image1 = Image.open(f"Q:\\Projects\\Code\\Python\\Universe Creation project\\assets\\protostar.jpg") 
    protostar_image1 = resize_image(protostar_image1, image_sizes) 
    protostar_image1 = ImageTk.PhotoImage(protostar_image1) 
    protostar_label_image1 = tk.Label(image=protostar_image1) 
    protostar_label_image1.grid(row=1,column=2)

    protostar_label=tk.Button(font=("helvetica",12), bg="silver", fg="black", text="Protostar", command=lambda: button_break("Protostar"))
    protostar_label.grid(row=2, column=2)

    main_sequence_image1 = Image.open(f"Q:\\Projects\\Code\\Python\\Universe Creation project\\assets\\main sequence.jpg") 
    main_sequence_image1 = resize_image(main_sequence_image1, image_sizes) 
    main_sequence_image1 = ImageTk.PhotoImage(main_sequence_image1) 
    main_sequence_label_image1 = tk.Label(image=main_sequence_image1) 
    main_sequence_label_image1.grid(row=1,column=4)

    main_sequence_label=tk.Button(font=("helvetica",12), bg="silver", fg="black", text="Main Sequence Star", command=lambda: button_break("Main Sequence"))
    main_sequence_label.grid(row=2, column=4)

    red_giant_image1 = Image.open(f"Q:\\Projects\\Code\\Python\\Universe Creation project\\assets\\red giant.jpg") 
    red_giant_image1 = resize_image(red_giant_image1, image_sizes) 
    red_giant_image1 = ImageTk.PhotoImage(red_giant_image1) 
    red_giant_label_image1 = tk.Label(image=red_giant_image1) 
    red_giant_label_image1.grid(row=1,column=6)

    red_giant_label=tk.Button(font=("helvetica",12), bg="silver", fg="black", text="Red Giant", command=lambda: button_break("Red Giant"))
    red_giant_label.grid(row=2, column=6)

    white_dwarf_image1 = Image.open(f"Q:\\Projects\\Code\\Python\\Universe Creation project\\assets\\white dwarf.jpg") 
    white_dwarf_image1 = resize_image(white_dwarf_image1, image_sizes) 
    white_dwarf_image1 = ImageTk.PhotoImage(white_dwarf_image1) 
    white_dwarf_label_image1 = tk.Label(image=white_dwarf_image1) 
    white_dwarf_label_image1.grid(row=4,column=6)

    white_dwarf_label=tk.Button(font=("helvetica",12), bg="silver", fg="black", text="White Dwarf", command=lambda: button_break("White Dwarf"))
    white_dwarf_label.grid(row=5, column=6)

    supernova_image1 = Image.open(f"Q:\\Projects\\Code\\Python\\Universe Creation project\\assets\\supernova.webp") 
    supernova_image1 = resize_image(supernova_image1, image_sizes) 
    supernova_image1 = ImageTk.PhotoImage(supernova_image1) 
    supernova_label_image1 = tk.Label(image=supernova_image1) 
    supernova_label_image1.grid(row=1,column=7)

    supernova_label=tk.Button(font=("helvetica",12), bg="silver", fg="black", text="Supernova", command=lambda: button_break("Supernova"))
    supernova_label.grid(row=2, column=7)

    root.mainloop()

startup_gui()