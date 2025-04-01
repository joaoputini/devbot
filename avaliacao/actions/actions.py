from typing import Any, Text, Dict, List  
from rasa_sdk import Action, Tracker  
from rasa_sdk.executor import CollectingDispatcher  

class ActionFornecerSuporte(Action):  
    def name(self) -> Text:  
        return "action_fornecer_suporte"  

    def run(self, dispatcher: CollectingDispatcher,  
            tracker: Tracker,  
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:  

        
        problema = tracker.get_slot("problema")  
        informacoes = self.obter_informacoes_suporte(problema)  

        if informacoes:  
            dispatcher.utter_message(text=f"Para o problema '{problema}', aqui estão algumas soluções: {', '.join(informacoes)}.")  
        else:  
            dispatcher.utter_message(text=f"Desculpe, não encontrei informações específicas para o problema '{problema}'. Vou encaminhar você para um atendente.")  

        return []  

    def obter_informacoes_suporte(self, problema: Text) -> List[Text]:  
        solucoes_por_problema = {  
            "acesso": [
                "Verifique se suas credenciais estão corretas (e-mail e senha).", 
                "Tente redefinir sua senha caso tenha esquecido.", 
                "Se o problema persistir, tente acessar o serviço em outro navegador ou dispositivo."
            ],  
            "plano": [
                "Para alterar seu plano, acesse sua conta e vá até a seção 'Planos e Pagamentos'.", 
                "Caso você queira trocar de plano, basta selecionar o novo plano e confirmar a alteração."
            ],  
            "tecnico": [
                "Tente reiniciar o aplicativo e verificar sua conexão com a internet.",
                "Se o problema continuar, tente desinstalar e reinstalar o aplicativo.",
                "Você também pode verificar se há atualizações disponíveis para o app."
            ],  
            "erro de pagamento": [
                "Verifique se o seu cartão de crédito está com dados atualizados.",
                "Confira se há saldo suficiente na sua conta para realizar o pagamento."
            ],
            "outra dúvida": [
                "Entre em contato com nosso suporte via chat ou e-mail para uma solução mais específica."
            ]
        }  

        return solucoes_por_problema.get(problema.lower(), [])  
