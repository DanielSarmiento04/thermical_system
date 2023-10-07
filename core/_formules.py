
class ThermoFormules:

    @staticmethod
    def nusselt(Re, Pr):
        '''
            Nusselt number for laminar flow in a circular tube

            Args:
                Re (float): Reynolds number
                Pr (float): Prandtl number
        '''

        return 0.3 + (0.62 * Re**(1/2) * Pr**(1/3)) / (1 + (0.4 / Pr)**(2/3))**(1/4) * (1 + (Re / 282000)**(5/8))**(4/5)

    @staticmethod
    def reynolds(velocity, diameter, viscosity):
        '''
        '''
        return velocity * diameter / viscosity
    
    def h(k, diametro, nusselt):
        return (k / diametro) * nusselt
# def 