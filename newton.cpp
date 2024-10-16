#include <iostream>
#include<iomanip>
#include <cmath>

using namespace std;

double func(double x){
    return 2*pow(x, 3) - 5*pow(x, 2) - sin(x) - 30;
}

double derivadaFunc(double x){
    return 6*pow(x, 2) - 10*x - cos(x);
}

double newton(double x0, double precisao, int iteracao){
    int k = 0;
    double novo;
    while ((k < iteracao) && (fabs(func(x0)) > precisao))
    {
        novo = x0 - ((func(x0)/derivadaFunc(x0)));
        x0 = novo;
        cout << "valor encontrado a cada iteracao: " << setprecision(6) << novo << endl;
        cout << fixed << setprecision(6) << func(novo) << endl;
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

    cout << newton(x0, precisao, iteracao);
}