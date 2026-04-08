# Generadores de energía
# https://www.facebook.com/photo?fbid=1494414332182152&set=a.722929239330669
# 
# Una instalación eléctrica debe generar 6500 megawatts de electricidad.
# Cuenta con cinco generadores. Si un generador dado produce electricidad,
# se le debe iniciar y entonces incurre en un costo fijo de preparación.
# Existe un costo adicional por cada megawatt producido por un generador.
# Estos costos, así como la capacidad máxima de cada uno, se muestran en
# la tabla siguiente. El objetivo es determinar el plan de costos mínimos
# que satisfaga las necesidades eléctricas actuales.
#
#                             Generador
#                     |  A    B    C    D    E
#                     |-------------------------
# Costo fijo          | 3000 2000 2500 1500 1000
# Costo por megaWatt  |    5    4    6    6    7
# Capacidad máxima MW | 2100 1800 2500 1500 3000

class Solution:
    def __init__(self, fixedCost, costPerMW, maxCapacity, expectedCapacity):
        self.fixedCost = fixedCost
        self.costPerMW = costPerMW
        self.maxCapacity = maxCapacity
        self.expectedCapacity = expectedCapacity

    def getGeneratorCost(self, megaWatts, generatorIndex):
        if megaWatts == 0:
            return 0
        return self.fixedCost[generatorIndex] + megaWatts * self.costPerMW[generatorIndex]

    def getOperationCost(self, x1, x2, x3, x4, x5):
        return self.getGeneratorCost(x1, 1) + \
            self.getGeneratorCost(x2, 2) + \
            self.getGeneratorCost(x3, 3) + \
            self.getGeneratorCost(x4, 4) + \
            self.getGeneratorCost(x5, 5)

    def isExpectedCapacityBeingMet(self, expectedCapacity, x1, x2, x3, x4, x5):
        return x1 <= maxCapacity[1] and \
            x2 <= maxCapacity[2] and \
            x3 <= maxCapacity[3] and \
            x4 <= maxCapacity[4] and \
            x5 <= maxCapacity[5] and \
            expectedCapacity <= x1 + x2 + x3 + x4 + x5

    def solve(self):
        bestOperationCost = float("inf")
        bestGenerationPlan = []

        for x1 in range(maxCapacity[1] + 1):
            for x2 in range(maxCapacity[2] + 1):
                for x3 in range(maxCapacity[3] + 1):
                    for x4 in range(maxCapacity[4] + 1):
                        for x5 in range(maxCapacity[5] + 1):
                            if self.isExpectedCapacityBeingMet(self.expectedCapacity, x1, x2, x3, x4, x5):
                                operationCost = self.getOperationCost(x1, x2, x3, x4, x5)
                                if operationCost < bestOperationCost:
                                    bestOperationCost = operationCost
                                    bestGenerationPlan= [x1, x2, x3, x4, x5]
                                    # print(bestOperationCost, sum(bestGenerationPlan), bestGenerationPlan)

        return bestGenerationPlan

if __name__=="__main__":
    fixedCost   = [0, 3000, 2000, 2500, 1500, 1000]
    costPerMW   = [0,    5,    4,    6,    6,    7]
    maxCapacity = [0, 2100, 1800, 2500, 1500, 3000]
    expectedCapacity = 6500

    # Normalizar problema
    maxCapacity = [c // 100 for c in maxCapacity]
    expectedCapacity = expectedCapacity // 100

    # Inicializar modelo
    solution = Solution(fixedCost, costPerMW, maxCapacity, expectedCapacity)

    # Obtener y denormalizar solución
    bestGenerationPlan = [x * 100 for x in solution.solve()]
    bestOperationCost = solution.getOperationCost(*bestGenerationPlan)
    expectedCapacity = 100 * expectedCapacity

    # Imprimir solución
    totalCost = 0
    print(f"Plan óptimo para producir {expectedCapacity} MW:")
    for i in range(len(bestGenerationPlan)):
        if bestGenerationPlan[i]:
            mW = bestGenerationPlan[i]
            generator = f"Generador {i + 1}"
            generatorCost = fixedCost[i + 1] + costPerMW[i + 1] * mW
            totalCost += generatorCost
            print(f"{generator}: {mW} MW a ${generatorCost}")

    print(f"Costo total: ${totalCost}")