import tkinter as tk
import customtkinter as ctk

from PIL import ImageTk  #Its able too render the imgage from the stable diffusion 
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

app = tk.Tk()
app.geometry("532x632")
app.title("Stable Bud")
ctk.set_appearance_mode("dark")

prompt = ctk.CTkEntry(app, height = 40, width = 512, font = ("Arial", 20), text_color="black", fg_color="white")
prompt.place(x=10,y=10)

lmain = ctk.CTkLabel(app, height=512, width=512,)
lmain.place(x = 10, y = 110)

modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision = "fp16", torch_dtype = torch.float16, auth_token = "Put the stable diffusion token id here")
pipe.to(device)


def generate():
    with autocast(device):
        image = pipe(prompt.get(), guidance_scale=8.5)["samaple"][0]

    image.save('generatedimage.png')
    img = ImageTk.PhotoImage(image)
    lmain.configure(image=img)

button = ctk.CTkButton(app, height = 40, width = 120, font = ("Arial", 20), text_color="black", fg_color="blue", command = generate)
button.configure(text = 'Generate')
button.place(x = 206, y = 60)


app.mainloop()
