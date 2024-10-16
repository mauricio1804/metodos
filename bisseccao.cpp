#include <iostream>
#include <cmath>

using namespace std;

double func(double x){
    return 5*pow(x, 2);
}

double bissecacao(double x0, double x1, double precisao, int iteracao){
    int k =0;
    double final, div;
    while (fabs(x1-x0) > precisao && (k < iteracao))
    {
        div = (x0+x1)/2;
        if(func(div) < 0){
            x0 = div;
        } else{
            x1 = div;
        }
        k++;

        cout << "valor encontrado a cada iteracao: " << div << endl;
        cout << x1-x0 << endl;
    }
    cout << "numero de iteracoes necessarias: " << k << endl;
    return div;
}

int main(){
    double x0, x1, precisao;
    int iteracao;

    cout << "escolha o valor minimo" << endl;
    cin >> x0;
    cout << "escolha o valor maximo" << endl;
    cin >> x1;
    cout << "qual o numero maximo de interacoes" << endl;
    cin >> iteracao;
    cout << "qual a precisao" << endl;
    cin >> precisao;

    cout << bissecacao(x0, x1, precisao, iteracao);
}