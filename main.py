import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard de Preços do Cimento")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        # Contêiner de preços
        preco_frame = ttk.LabelFrame(self, text="Preços do Cimento")
        preco_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Adicione seus widgets de preços aqui, por exemplo, uma lista ou uma tabela

        # Contêiner do gráfico
        grafico_frame = ttk.LabelFrame(self, text="Evolução dos Preços")
        grafico_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Botão para gerar o gráfico
        btn_gerar_grafico = ttk.Button(grafico_frame, text="Gerar Gráfico", command=self.plotar_grafico)
        btn_gerar_grafico.pack(pady=10)

        # Área para exibir o gráfico
        self.fig, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=grafico_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()

    def plotar_grafico(self):
        # Aqui você deve substituir os dados fictícios pelos seus próprios dados de preços ao longo do tempo
        dados = {
            'Meses': ['Jan', 'Feb', 'Mar', 'Mar', 'Abr', 'Abr', 'Mai', 'Mai', 'Jun', 'Jun', 'Jul', 'Jul', 'Ago', 'Set', 'Out', 'Out', 'Out', 'Nov', 'Nov', 'Dez', 'Dez'],
            'Preços': [29.50, 31.00, 31.00, 29.50, 29.50, 29.00, 29.00, 30.00, 30.00, 29.50, 28.50, 28.00, 28.00, 28.00, 28.00, 29.50, 28.50, 28.00, 28.50, 28.00, 30.00]
        }

        self.ax.clear()  # Limpar a área do gráfico antes de plotar novamente
        self.ax.plot(dados['Meses'], dados['Preços'], marker='o', label='Preços do Cimento')
        self.ax.set_xlabel('Meses')
        self.ax.set_ylabel('Preços')
        self.ax.set_title('Evolução dos Preços do Mizu 40kg ao Longo de 2023')
        self.ax.legend()

        # Atualizar o gráfico na tela
        self.canvas.draw_idle()

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()
