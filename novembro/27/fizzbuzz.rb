
class FizzBuzz

    def initialize(numero)
        @numero = numero
        @resultado = self.regra_de_negocio
    end

    def regra_de_negocio
        resultado = ""

        resultado << 'fizz' if @numero % 3 == 0        
        resultado << 'buzz' if @numero.modulo(5) == 0
        
        if resultado.empty?
            resultado << @numero.to_s
        end

        resultado
    end

    def imprimir
        @resultado
    end

end
