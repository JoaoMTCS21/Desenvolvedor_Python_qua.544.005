# classe

class Pessoa:

    def __init__(self, telefone, email):
        self.__telefone = telefone
        self.__email = email

    # Métodos set e get

    @property # método get
    def telefone(self): 
     return self.__telefone

    @telefone.setter # método set
    def telefone(self, telefone):
      self.__telefone = telefone

    @property # método get
    def email(self):
     return self.__email

    @email.setter # método set
    def email(self, email):
     self.__email = email

# subclasses / classes-filha
class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, email, telefone):
        self.__nome = nome
        self.__cpf = cpf
        super().__init__(email=email, telefone=telefone)

    @property # método get
    def nome(self):
         return self.__nome
    
    @nome.setter # método set
    def nome(self, nome):
        self.__nome = nome

    @property # método get
    def cpf(self):
        return self.__cpf
    
    @cpf.setter # método set
    def cpf(self, cpf):
        self.__cpf = cpf

class PessoaJuridica(Pessoa):
    def __init__(self, cnpj, razao_social, nome_fantasia, email, telefone):
        self.__cnpj = cnpj
        self.__razao_social = razao_social
        self.__nome_fantasia = nome_fantasia
        super().__init__(email=email, telefone=telefone,)

    @property # método get
    def razao_social(self):
        return self.__razao_social

    @razao_social.setter # método set
    def razao_social(self, razao_social):
        self.__razao_social = razao_social