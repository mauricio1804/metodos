#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double func(double x){
    return pow(x, 3) - 9*x + 3;
}

double sec(double x1, double x0, double precisao, double iteracao){
    int k = 0;
    double novo;
    while ((k < iteracao) && (fabs(func(x1)) > precisao) && (fabs(x1-x0) > precisao))
    {
        novo = x1 - ((func(x1)*(x1-x0))/(func(x1)-func(x0)));
        x0 = x1;
        x1 = novo;
        cout << "valor encontrado a cada iteracao: " << setprecision(6) << novo << endl;
        cout << fixed << setprecision(6) << func(novo) << endl;
        k++;
    }
    cout << "numero de iteracoes necessarias: " << k << endl;
    cout << x1 - x0 << endl;
    cout << func(novo) << endl;
    return x1;
}

int main(){
    double x0, x1, fx0, final, div, precisao;
    int iteracao, k = 0;

    cout << "escolha o valor minimo" << endl;
    cin >> x0;
    cout << "escolha o valor maximo" << endl;
    cin >> x1;
    cout << "qual o numero maximo de interacoes" << endl;
    cin >> iteracao;
    cout << "qual a precisao" << endl;
    cin >> precisao;

    cout << sec(x0, x1, precisao, iteracao);
}