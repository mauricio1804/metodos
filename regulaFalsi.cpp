#include <iostream>
#include <cmath>

using namespace std;

double func(double x){
    return 5*x;
}

double regulaFalsi(double x0, double x1, double precisao, int iteracao){
    int k = 0;
    double novo;
    while ((k < iteracao) && ((fabs(func(x0)) > precisao)) && ((fabs(func(x1)) > precisao)))
    {
        novo = ((x0*func(x1)-x1*func(x0))/(func(x1)-func(x0)));
        if(func(novo) < 0){
            x0 = novo;
        } else{
            x1 = novo;
        }
        k++;
        cout << "valor encontrado a cada iteracao: " << novo << endl;
        cout << func(novo) << endl;
    }
    cout << "numero de iteracoes necessarias: " << k << endl;
    return novo;
}

int main(){
    double x0, x1, final, div, precisao;
    int iteracao, k = 0;

    cout << "escolha o valor minimo" << endl;
    cin >> x0;
    cout << "escolha o valor maximo" << endl;
    cin >> x1;
    cout << "qual o numero maximo de interacoes" << endl;
    cin >> iteracao;
    cout << "qual a precisao" << endl;
    cin >> precisao;

    cout << regulaFalsi(x0, x1, precisao, iteracao);
}