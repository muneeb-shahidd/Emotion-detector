# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk
# from deepface import DeepFace
# import traceback
#
#
# def select_image():
#     path = filedialog.askopenfilename(
#         title="Select a picture",
#         filetypes=[("Images", "*.jpg *.jpeg *.png")]
#     )
#     if not path:
#         return
#
#     img = Image.open(path)
#     img.thumbnail((350, 350))
#     photo = ImageTk.PhotoImage(img)
#     image_label.config(image=photo)
#     image_label.image = photo
#
#     result_label.config(text="Detecting...", fg="gray")
#     root.update()
#
#     try:
#         result = DeepFace.analyze(
#             img_path=path,
#             actions=["emotion"],
#             enforce_detection=True
#         )
#         emotions = result[0]["emotion"]
#         happy = emotions["happy"]
#         sad = emotions["sad"]
#
#         if happy >= sad:
#             text = f"Happy 😊\n(Happy: {happy:.1f}%  |  Sad: {sad:.1f}%)"
#             color = "green"
#         else:
#             text = f"Sad 😢\n(Happy: {happy:.1f}%  |  Sad: {sad:.1f}%)"
#             color = "red"
#         result_label.config(text=text, fg=color)
#
#     except Exception as e:
#         traceback.print_exc()
#         result_label.config(text=f"Error: {str(e)[:80]}", fg="orange")
#
#
# root = tk.Tk()
# root.title("Happy or Sad Detector")
# root.geometry("450x550")
#
# tk.Label(root, text="Happy or Sad Detector",
#          font=("Arial", 18, "bold")).pack(pady=10)
#
# tk.Button(root, text="Select Image", font=("Arial", 13),
#           command=select_image).pack(pady=5)
#
# image_label = tk.Label(root)
# image_label.pack(pady=10)
#
# result_label = tk.Label(root, text="", font=("Arial", 15, "bold"))
# result_label.pack(pady=10)
#
# root.mainloop()
