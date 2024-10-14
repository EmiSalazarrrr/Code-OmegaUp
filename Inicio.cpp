#include <iostream>

using namespace std;
int main(){
    string Nombre;
    int NumeroControl;
    string Carrera;
    cout<<"Ingresa tu nombre: "<<endl;
    cin >> Nombre;
    cout<<"Ingresa tu número de control: "<<endl;
    cin >> NumeroControl;
    cout<<"Ingresa tu carrera: "<<endl;
    cin >> Carrera;
    cout << "¡¡Hola "<<Nombre<<"!!"<<endl;
    cout << "Tu número de control es "<<NumeroControl<<endl;
    cout << "Tu carrera es "<<Carrera<<endl;
    return 0;
}