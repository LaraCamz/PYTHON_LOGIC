#Atividade 4 - Desenhe 2 quadrados, um dentro do outro. As linhas dos quadrados não devem se conectar.
import turtle 
# Cria a janela e a tartaruga 
janela = turtle.Screen() 
tartaruga = turtle.Turtle() 

turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.right(90)

turtle.penup()
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.pendown()

turtle.forward(110)
turtle.right(90)
turtle.forward(110)
turtle.right(90)
turtle.forward(110)
turtle.right(90)
turtle.forward(110)

janela.mainloop() # Mantém a janela aberta até ser fechada.