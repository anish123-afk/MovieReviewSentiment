import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import prediction

root = tk.Tk()
root.title("Movie Review Sentiment Analyzer")
root.geometry("680x780")
root.minsize(680, 780)
root.configure(bg="#1e1e1e")
root.resizable(True, True)

def on_predict():
    review = review_text.get("1.0", tk.END).strip()
 
    if not review:
        messagebox.showwarning("Empty Review", "Please enter a movie review first!")
        return
 
    try:
        label, confidence = prediction.predict_sentiment(review)
    except Exception as e:
        messagebox.showerror("Prediction Error", f"Something went wrong:\n{e}")
        return

 
    if label == "positive":
        kind, tint, accent, badge_text = "positive", "#123a25", "#22c55e", "POSITIVE"
    else:
        kind, tint, accent, badge_text = "negative", "#3a1414", "#ef4444", "NEGATIVE"

    # draw_icon(kind, tint)

    badge_label.config(
        text=badge_text,
        fg=accent,
        bg="#2d2d2d"
    )

    confidence_value_label.config(
        text=f"Confidence : {confidence}%",
        fg="white"
    )
    
    # draw_icon(kind, tint)
    # badge_label.config(text=badge_text, bg=accent, fg="white")
    # confidence_value_label.config(text=f"{confidence_pct:.1f}%", fg=accent)
 
    # progress_bar.config(
    #     style="Positive.Horizontal.TProgressbar" if is_positive else "Negative.Horizontal.TProgressbar"
    # )
    # progress_bar["value"] = confidence_pct

def clear_review():
    review_text.delete("1.0", tk.END)
    reset_result()

def reset_result():
    # draw_icon("neutral", "#242424")
    badge_label.config(
        text="AWAITING INPUT",
        fg="#8a8a8a",
        bg="#2d2d2d"
    )
    confidence_value_label.config(
        text="Confidence : --",
        fg="#cfcfcf"
    )

heading_label = tk.Label(
    root,
    text="SENTIMENT ANALYZER",
    font=("Segoe UI", 24, "bold"),
    fg="#00d4ff",
    bg="#1e1e1e",
)
heading_label.pack(pady=(30, 0))

heading_label.pack(pady=(30, 0))
 
subheading_label = tk.Label(
    root,
    text="AI-powered movie review classifier",
    font=("Segoe UI", 11),
    fg="#8a8a8a",
    bg="#1e1e1e",
)
subheading_label.pack(pady=(4, 20))

input_card = tk.Frame(root, bg="#2d2d2d")
input_card.pack(padx=30, pady=10, fill="x")
 
input_label = tk.Label(
    input_card,
    text="Enter Your Review",
    font=("Segoe UI", 12, "bold"),
    fg="#ffffff",
    bg="#2d2d2d",
    anchor="w",
)
input_label.pack(fill="x", padx=20, pady=(18, 8))

review_text = tk.Text(
    input_card,
    height=7,
    font=("Segoe UI", 11),
    bg="#242424",
    fg="white",
    insertbackground="white",
    relief="flat",
    wrap="word",
    highlightthickness=2,
    highlightbackground="#3a3a3a",
    highlightcolor="#3a3a3a",
    padx=12,
    pady=10,
)
review_text.pack(fill="x", padx=20, pady=(0, 15))

button_row = tk.Frame(input_card, bg="#2d2d2d")
button_row.pack(fill="x", padx=20, pady=(0, 20))

predict_button = tk.Button(
    button_row,
    text="🔍  Analyze Sentiment",
    command=on_predict,
    font=("Segoe UI", 11, "bold"),
    bg="#00d4ff",
    fg="black",
    activebackground="#00b8e6",
    activeforeground="black",
    relief="flat",
    padx=15,
    pady=8,
    cursor="hand2",
)
predict_button.pack(side="left")
 
clear_button = tk.Button(
    button_row,
    text="Clear",
    command=clear_review,
    font=("Segoe UI", 11, "bold"),
    bg="#3a3a3a",
    fg="white",
    activebackground="#4a4a4a",
    activeforeground="white",
    relief="flat",
    padx=15,
    pady=8,
    cursor="hand2",
)
clear_button.pack(side="left", padx=(10, 0))


result_card = tk.Frame(root, bg="#2d2d2d")
result_card.pack(padx=30, pady=20, fill="x")

result_title = tk.Label(
    result_card,
    text="Prediction Result",
    font=("Segoe UI", 13, "bold"),
    fg="white",
    bg="#2d2d2d"
)
result_title.pack(pady=(20,15))

result_canvas = tk.Canvas(
    result_card,
    width=100,
    height=100,
    bg="#2d2d2d",
    highlightthickness=0
)
result_canvas.pack()

badge_label = tk.Label(
    result_card,
    text="AWAITING INPUT",
    font=("Segoe UI", 18, "bold"),
    fg="#8a8a8a",
    bg="#2d2d2d"
)
badge_label.pack(pady=(15,5))

confidence_value_label = tk.Label(
    result_card,
    text="Confidence : --",
    font=("Segoe UI", 13),
    fg="#cfcfcf",
    bg="#2d2d2d"
)
confidence_value_label.pack(pady=(0,20))

# tk.Label(root, text="Enter your review:").pack()
# entry = tk.Text(root, height=5, width=40)
# entry.pack()


# tk.Button(root, text="Predict", command=on_predict).pack()
# result_label = tk.Label(root, text="")
# result_label.pack()

root.mainloop()