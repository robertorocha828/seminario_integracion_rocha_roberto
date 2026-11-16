from abc import ABC, abstractmethod

class Evaluador(ABC):
    @abstractmethod
    def calificar(self):
        pass

class EvaluadorEntrevista(Evaluador):
    def calificar(self):
        return "Roberto Rocha obtiene 9.5 sobre 10 en la entrevista"

class EvaluadorExamen(Evaluador):
    def calificar(self):
        return "Hernán Varas obtiene 8.5 sobre 10 en el examen"

entrevista = EvaluadorEntrevista()
print(entrevista.calificar())
examen = EvaluadorExamen()
print(examen.calificar())

try:
    evaluador = Evaluador()
except TypeError:
    print("No se puede crear un objeto de la clase abstracta Evaluador")
