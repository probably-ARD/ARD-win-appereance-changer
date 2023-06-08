import st_start_win_config as conf
import customtkinter as ctk


class stStartWin(ctk.CTk):
    # все виджеты окна
    def __init__(self):
        super().__init__()

        # настройка темы
        ctk.set_appearance_mode('system')
        ctk.set_default_color_theme('green')

        # настройки окна
        self.geometry('600x400')
        self.title(conf.WIN_NAME)
        self.resizable(False, False)

        # текст над пользовательским соглашением
        self.user_agree_caption = ctk.CTkLabel(master=self, text=conf.USER_AGREEMENT_CAPTION, 
                                               width=590, height=20, anchor='w')
        self.user_agree_caption.place(x=5, y=5)

        # текст самого пользовательского сочинения
        self.user_agreement_txt = ctk.CTkTextbox(master=self, width=590, height=320)
        self.user_agreement_txt.grid(padx=5, pady=30, sticky='nsew')
        self.user_agreement_txt.insert('0.0', conf.USER_AGREEMENT_TXT)
        self.user_agreement_txt.configure(state='disabled')

        # чекбокс
        self.chekbox= ctk.CTkCheckBox(master=self, text=conf.USER_AGREEMENT_CHEKBOX_CAPTION,
                                      width=20, height=30)
        self.chekbox.place(x=5, y=365)

        # кнопка продолжения
        self.btn = ctk.CTkButton(master=self, text=conf.USER_AGREEMENT_BTN_TXT,
                                 width=20, height=30, state=ctk.DISABLED)
        self.btn.place(x=505, y=365)


stStartWin().mainloop()