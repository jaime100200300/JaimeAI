import customtkinter as ctk
import ai2

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x600")
        self.title("Jaime AI 2.0")

        self.ai = ai2.AI()

        # --- Chat display ---
        self.chatbox = ctk.CTkTextbox(self, width=480, height=500, wrap="word")
        self.chatbox.pack(pady=10)

        # --- User input ---
        self.entry = ctk.CTkEntry(self, placeholder_text="Ask Jaime AI!")
        self.entry.pack(fill="x", padx=10, pady=(0,5))

        # Bind Enter key to send_message
        self.entry.bind("<Return>", self.send_message_event)

        self.button = ctk.CTkButton(self, text="Send", command=self.send_message)
        self.button.pack(pady=(0,10))

        self.entry.focus()

        self.mainloop()

    def send_message_event(self, event):
        self.send_message()

    def send_message(self):
        user_text = self.entry.get().strip()
        if not user_text:
            return

        # Display user message
        self.chatbox.insert("end", f"You: {user_text}\n")

        # Get AI response
        ai_response = self.ai.ask_history(user_text)

        # Display AI message
        self.chatbox.insert("end", f"JaimeAI: {ai_response}\n\n")

        # Auto-scroll to bottom
        self.chatbox.see("end")

        # Clear entry
        self.entry.delete(0, "end")

App()
