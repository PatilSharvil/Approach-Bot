import customtkinter as ctk
from gemini_connector import get_approach_from_gemini

# === Appearance ===
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

# === App Setup ===
app = ctk.CTk()
app.title("Approach Teller - Gemini AI")
app.geometry("1000x700")
app.resizable(False, False)

# === Fonts ===
font_title = ctk.CTkFont(family="Segoe UI", size=26, weight="bold")
font_normal = ctk.CTkFont(family="Segoe UI", size=15)
font_output = ctk.CTkFont(family="Segoe UI", size=14, weight="bold")
font_button = ctk.CTkFont(family="Segoe UI", size=16, weight="bold")

# === Centered Main Frame ===
main_frame = ctk.CTkFrame(app, width=860, height=620, fg_color="white", corner_radius=25)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# === Title ===
title = ctk.CTkLabel(main_frame, text="💡 Approach Teller", text_color="black", font=font_title)
title.pack(pady=(30, 20))

# === Input TextBox ===
input_box = ctk.CTkTextbox(main_frame, width=780, height=100, corner_radius=15,
                           font=font_normal, fg_color="#f8f9fa", text_color="black",
                           border_width=2, border_color="#d0d0d0", wrap="word")
input_box.pack(pady=(0, 30), padx=40)
input_box.insert("0.0", "Enter your coding question here...")
input_box.bind("<FocusIn>", lambda e: input_box.delete("0.0", "end") if input_box.get("0.0", "end").strip() == "Enter your coding question here..." else None)

# === Output TextBox ===
output_box = ctk.CTkTextbox(main_frame, width=780, height=280, corner_radius=15,
                            font=font_output, fg_color="#f1f3f4", text_color="black",
                            border_width=2, border_color="#d0d0d0", wrap="word")
output_box.pack(pady=(0, 40), padx=40)
output_box.insert("0.0", "You'll see the steps here...")
output_box.configure(state="disabled")

def show_output(text):
    output_box.configure(state="normal")
    output_box.delete("0.0", "end")
    output_box.insert("0.0", text)
    output_box.configure(state="disabled")

# === Button Action ===
def on_get_approach():
    problem = input_box.get("0.0", "end").strip()
    if problem and problem != "Enter your coding question here...":
        show_output("⏳ Generating approach...")
        try:
            answer = get_approach_from_gemini(problem)
        except Exception as e:
            answer = f"❌ Error: {str(e)}"
        show_output(answer)

# === Get Approach Button ===
get_btn = ctk.CTkButton(
    main_frame, text="Get Approach", command=on_get_approach,
    height=55, width=320, font=font_button,
    fg_color="#1a73e8", hover_color="#185abc", text_color="white", corner_radius=18
)
get_btn.pack(pady=(0, 20))

# === Run ===
app.mainloop()
