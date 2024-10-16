#include <iostream>
#include <cmath>

using namespace std;

double func(double x){
    return 1/pow(2, exp(x/2));
}

double mil(double x0, double precisao, int iteracao){
    int k = 0;
    double novo, x1=0;
    while ((k < iteracao) && fabs(x0-x1) > precisao)
    {
        novo = func(x0);
        x1 = x0;
        x0 = novo;
        cout << "valor encontrado a cada iteracao: " << novo << endl;
        k++;
    }
    cout << "numero de iteracoes necessarias: " << k << endl;
    return novo;
}

int main(){
    double x0, precisao;
    int iteracao;

    cout << "escolha o valor de x0" << endl;
    cin >> x0;
    cout << "qual o numero maximo de interacoes" << endl;
    cin >> iteracao;
    cout << "qual a precisao" << endl;
    cin >> precisao;

    cout << mil(x0, precisao, iteracao);
}