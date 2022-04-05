a = input("Informe um valor para a variável a: ")
b = input("Informe um valor para a variável b: ")

if (a>b):
    aux=a;
    a=b;
    b+aux;

print("O valor da variável a agora é : ", a);
print("O valor da variável b agora é : ", b);